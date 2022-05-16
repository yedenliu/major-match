################################################################################
#   Import modules
################################################################################
from pdb import find_function
from flask import (Flask, render_template, make_response, url_for, request,
                   redirect, flash, session, send_from_directory, jsonify)
from werkzeug.utils import secure_filename
app = Flask(__name__)

import cs304dbi as dbi
import random
from prepared_queries import *
import bcrypt
# git hub
################################################################################
app.secret_key = 'your secret here'
# replace that with a random key
app.secret_key = ''.join([ random.choice(('ABCDEFGHIJKLMNOPQRSTUVXYZ' +
                                          'abcdefghijklmnopqrstuvxyz' +
                                          '0123456789'))
                           for i in range(20) ])

# This gets us better error messages for certain common request errors
app.config['TRAP_BAD_REQUEST_ERRORS'] = True

################################################################################
#   Routing functions
################################################################################
@app.route('/')
def index():
    if (not session) or (session.get('user') != 'admin'):
        flash('Unauthorized. Log in to access page.')
        return redirect( url_for('login') )
    else:
        return render_template('index.html',
                                page_title='Mainpage')
################################################################################

@app.route('/insert/', methods=['GET','POST'])
def insert():
    if (not session) or (session.get('user') != 'admin'):
        flash('Unauthorized. Log in to access page.')
        return redirect( url_for('login') )
    else:
        conn = dbi.connect()
        if request.method == 'GET':
            return render_template('insert.html',page_title='Insert New Course')
        else:
            dept = request.form.get('dept') # required
            cnum = request.form.get('cnum') # required
            name = request.form.get('name') # required
            units = request.form.get('units')
            max_enroll = request.form.get('max_enroll')
            prereq = request.form.get('prereq')
            instruct = request.form.get('instruct')
            dr = request.form.get('dr')
            sem_offered = request.form.get('sem_offered')
            year_offered = request.form.get('year_offered')
            
            # all required fields must be filled out
            if len(dept) == 0 or len(cnum) == 0 or len(name) == 0:
                flash('Missing required field(s)')
                return render_template('insert.html',page_title='Insert New Course')
            if not (course_name_exists(conn, dept, cnum)): # if course doesn't exist
                insert_course(conn, dept, cnum, name, units, max_enroll, prereq, 
                            instruct, dr, sem_offered, year_offered)
                cid = get_cid(conn, dept, cnum)
                return redirect(url_for('update', cid=cid))
            flash('Course already exists')
            return render_template('insert.html',page_title='Insert New Course')

################################################################################

@app.route('/select/', methods=['GET','POST'])
def select():
    '''
    on GET shows a menu of incomplete courses 
    on POST redirects to the /update/<cid> page for that course.
    Incomplete means missing required fields
    Unmatched means they have yet to be assigned to a major
    '''
    if (not session) or (session.get('user') != 'admin'):
        flash('Unauthorized. Log in to access page.')
        return redirect( url_for('login') )
    else:
        conn = dbi.connect()
        if request.method == 'GET':
            course_list = get_incomplete(conn)
            unassigned = get_unassigned(conn)
            return render_template('select.html',
                                    page_title='Select Incomplete Courses', 
                                    course_list = course_list,
                                    unassigned = unassigned)
        else: 
            print(request.form)
            cid = request.form['majorless_cid']
            return redirect(url_for('update', cid=cid))
################################################################################

@app.route('/departments/')
def departments():
    if (not session) or (session.get('user') != 'admin'):
        flash('Unauthorized. Log in to access page.')
        return redirect( url_for('login') )
    else:
        conn = dbi.connect()
        departments = get_departments(conn)
        return render_template('departments.html',
                                page_title='Departments',
                                departments = departments)
################################################################################

@app.route('/departments/<dept_id>', methods=['GET', 'POST'])
def department_page(dept_id):
    if (not session) or (session.get('user') != 'admin'):
        flash('Unauthorized. Log in to access page.')
        return redirect( url_for('login') )
    else:
        conn = dbi.connect()
        departments = get_departments(conn)
        name = get_dept_name(conn, dept_id) 
        courses = get_dept_courses(conn, dept_id) # dept, cnum, name, cid
        if request.method == 'POST':
            dept = request.form.get('dept')
            cnum = request.form.get('cnum')
            cid = get_cid(conn, dept, cnum)
            add_pair(conn, dept_id, cid)
            flash('Course successfully paired to this major!')
            return redirect(url_for('department_page', dept_id = dept_id))
        return render_template('department_page.html',
                                page_title = name + ' Department Page',
                                name = name,
                                courses = courses,
                                depts = departments)
################################################################################

@app.route('/update/<cid>', methods=['GET','POST'])
def update(cid):
    if (not session) or (session.get('user') != 'admin'):
        flash('Unauthorized. Log in to access page.')
        return redirect( url_for('login') )
    else:
        conn = dbi.connect()
        depts = get_departments(conn)
        if course_exists(conn, cid)==False:
            flash('This course does not exist')
            return redirect(url_for('index'))
        if request.method == 'GET':
            info = get_course_info(conn, cid)
            _,dept,cnum,name,units,max_enroll,prereq,instruct,dr,sem_offered,year_offered = info
            majors = get_pairs(conn, cid)
            return render_template('update.html',
                                    page_title='Update Course',
                                    dept = dept,
                                    cnum = cnum,
                                    name = name,
                                    units = units,
                                    max_enroll = max_enroll,
                                    prereq = prereq,
                                    instruct = instruct,
                                    dr = dr,
                                    sem_offered = sem_offered,
                                    year_offered = year_offered,
                                    cid = cid,
                                    majors = majors,
                                    depts = depts)
        else:
            if request.form['submit'] == 'update':
                dept = request.form.get('dept')
                cnum = request.form.get('cnum')
                name = request.form.get('name')
                units = request.form.get('units')
                max_enroll = request.form.get('max_enroll')
                prereq = request.form.get('prereq')
                instruct = request.form.get('instruct')
                dr = request.form.get('dr')
                sem_offered = request.form.get('sem_offered')
                year_offered = request.form.get('year_offered')
                majors = get_pairs(conn, cid)
        
                update_course(conn, cid, dept, cnum, name, units, max_enroll, 
                prereq, instruct, dr, sem_offered, year_offered)

                flash('Successfully updated!')
                return render_template('update.html',
                                    page_title='Update Course',
                                    dept = dept,
                                    cnum = cnum,
                                    name = name,
                                    units = units,
                                    max_enroll = max_enroll,
                                    prereq = prereq,
                                    instruct = instruct,
                                    dr = dr,
                                    sem_offered = sem_offered,
                                    year_offered = year_offered,
                                    cid = cid,
                                    majors = majors,
                                    depts = depts)
            elif request.form['submit'] == 'delete':
                delete_course(conn, cid)
                flash("Course successfully deleted!")
                return redirect(url_for('index'))
            elif 'delete-pair' in request.form['submit']:
                value = request.form['submit']
                # get dept id
                dept_id = value.strip('delete-pair-')
                # delete pair
                remove_pair(conn, dept_id, cid)
                flash("Course pairing deleted")
                return redirect(url_for('update', cid=cid))
            
            elif request.form['submit'] == 'add':
                # takes department name 
                new_dept = request.form.get('new_dept')
                # finds dept ID
                new_dept_id = get_dept_id(conn, new_dept)
                add_pair(conn, new_dept_id, cid)
                flash("Matched to department successfully!")
                info = get_course_info(conn, cid)
                dept = info[1]
                cnum = info[2]
                name = info[3]
                units = info[4]
                max_enroll = info[5]
                prereq = info[6]
                instruct = info[7]
                dr = info[8]
                sem_offered = info[9]
                year_offered = info[10]
                majors = get_pairs(conn, cid)
                return render_template('update.html',
                                    page_title='Update Course',
                                    dept = dept,
                                    cnum = cnum,
                                    name = name,
                                    units = units,
                                    max_enroll = max_enroll,
                                    prereq = prereq,
                                    instruct = instruct,
                                    dr = dr,
                                    sem_offered = sem_offered,
                                    year_offered = year_offered,
                                    cid = cid,
                                    majors = majors,
                                    depts = depts)
            else:
                flash("Error")

################################################################################

@app.route('/login', methods=["GET", "POST"])
def login():
    if request.method=="GET":
        return render_template('login.html',
        page_title='Login')
    else:
        user = request.form.get('user')
        pw = request.form.get('pw')
        conn = dbi.connect()
        curs = dbi.dict_cursor(conn)
        curs.execute("select hashedpw from account where user=%s", [user])
        stored = curs.fetchone().get('hashedpw')
        hashed = bcrypt.hashpw(pw.encode('utf-8'), stored.encode('utf-8'))
        hashedStr = hashed.decode('utf-8')
        if hashedStr != stored:
            flash("Login attempt failed.")
            return redirect( url_for('login') )
        else:
            session['Logged in'] = True
            session['user'] = user
            return redirect( url_for('index') )

################################################################################ 

@app.route('/logout/')
def logout():
    if 'user' in session:
        session.pop('user')
        flash('You are logged out.')
        return redirect( url_for('login') )
    else:
        flash('You are not logged in. Please log in.')
        return redirect( url_for('login') )

 ################################################################################ 
           
@app.before_first_request
def init_db():
    dbi.cache_cnf()
    # set this local variable to 'wmdb' or your personal or team db
    db_to_use = 'majormatch_db' 
    dbi.use(db_to_use)
    print('will connect to {}'.format(db_to_use))

if __name__ == '__main__':
    import sys, os
    if len(sys.argv) > 1:
        # arg, if any, is the desired port number
        port = int(sys.argv[1])
        assert(port>1024)
    else:
        port = os.getuid()
    app.debug = True
    app.run('0.0.0.0',port)
