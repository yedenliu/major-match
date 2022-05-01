from pdb import find_function
from flask import (Flask, render_template, make_response, url_for, request,
                   redirect, flash, session, send_from_directory, jsonify)
from werkzeug.utils import secure_filename
app = Flask(__name__)

import cs304dbi as dbi
import random
from prepared_queries import *

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
################################################################################
# Note : must use a port from 1943 to 1952.
# bash install-scott-routing.sh doesn't install into our venv
# new for CAS
from flask_cas import CAS

CAS(app)

app.config['CAS_SERVER'] = 'https://login.wellesley.edu:443'
app.config['CAS_LOGIN_ROUTE'] = '/module.php/casserver/cas.php/login'
app.config['CAS_LOGOUT_ROUTE'] = '/module.php/casserver/cas.php/logout'
app.config['CAS_VALIDATE_ROUTE'] = '/module.php/casserver/serviceValidate.php'
app.config['CAS_AFTER_LOGIN'] = 'logged_in'
# the following doesn't work :-(
app.config['CAS_AFTER_LOGOUT'] = 'after_logout'


@app.route('/logged_in/')
def logged_in():
    flash('successfully logged in!')
    return redirect( url_for('index') )

@app.route('/after_logout/')
def after_logout():
    flash('successfully logged out!')
    return redirect( url_for('index') )

application = app
################################################################################

@app.route('/')
def index():
    print('Session keys: ',list(session.keys()))
    for k in list(session.keys()):
        print(k,' => ',session[k])
    if '_CAS_TOKEN' in session:
        token = session['_CAS_TOKEN']
    if 'CAS_NAME' in session:
        username = session['CAS_USERNAME']
        print(('CAS_USERNAME is: ',username))
    else:
        username = None
        print('CAS_USERNAME is not in the session')
    return render_template('index.html',
                            page_title='Mainpage',
                            username=username)

@app.route('/insert/', methods=['GET','POST'])
def insert():
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
        if not (course_exists(conn, dept, cnum)): # if movie doesn't exist
            insert_course(conn, dept, cnum, name, units, max_enroll, prereq, 
                          instruct, dr, sem_offered, year_offered)
            cid = find_cid(conn, dept, cnum)
            return redirect(url_for('update', cid=cid))
        flash('Course already exists')
        return render_template('insert.html',page_title='Insert New Course')


@app.route('/select/', methods=['GET','POST'])
def select():
    '''
    on GET shows a menu of incomplete courses 
    on POST redirects to the /update/<cid> page for that course.
    Incomplete means as either the director or the release date is null
    '''
    conn = dbi.connect()
    if request.method == 'GET':
        course_list = find_incomplete(conn)
        return render_template('select.html',
                                page_title='Select Incomplete Courses', 
                                course_list = course_list)
    else: 
        cid = request.form['cid']
        return redirect(url_for('update', cid=cid))

@app.route('/departments/')
def departments():
    conn = dbi.connect()
    departments = get_departments(conn)
    return render_template('departments.html',
                            page_title='Departments',
                            departments = departments)

@app.route('/departments/<dept_id>', methods=['GET', 'POST'])
def department_page(dept_id):
    conn = dbi.connect()
    name = find_dept_name(conn, dept_id) 
    courses = find_dept_courses(conn, dept_id) # dept, cnum, courses.name, cid
    if request.method == 'GET':
        pass
    else:
        dept = request.form.get('dept')
        cnum = request.form.get('cnum')
        cid = find_cid(conn, dept, cnum)
        add_pair(conn, dept_id, cid)
        flash('Course successfully paired to this major!')
        return redirect(url_for('department_page', dept_id = dept_id))
    return render_template('department_page.html',
                            page_title = name + ' Department Page',
                            name = name,
                            courses = courses)

@app.route('/update/<cid>', methods=['GET','POST'])
def update(cid):
    conn = dbi.connect()
    if request.method == 'GET':
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
        type = info[11]
        type_notes = info[12]
        major_freq = info[13]
        majors = find_pairs(conn, cid)
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
                                type = type,
                                type_notes = type_notes,
                                major_freq = major_freq,
                                cid = cid,
                                majors = majors)
    else:
        if request.form['submit'] == 'update':
            # must be able to update TT but must be a unique cid
            old_cid = cid
            dept = request.form.get('dept')
            cnum = request.form.get('cnum')
            new_cid = find_cid(conn, dept, cnum)

            if old_cid != new_cid and course_exists(conn, dept, cnum): # if course already exists
                flash("The Department & Course Number pair you entered already exists")
                return redirect(url_for('update', cid=old_cid))

            name = request.form.get('name')
            units = request.form.get('units')
            max_enroll = request.form.get('max_enroll')
            prereq = request.form.get('prereq')
            instruct = request.form.get('instruct')
            dr = request.form.get('dr')
            sem_offered = request.form.get('sem_offered')
            year_offered = request.form.get('year_offered')
            type = request.form.get('type')
            type_notes = request.form.get('type_notes')
            major_freq = request.form.get('major_freq')
            majors = find_pairs(conn, cid)
    
            update_course(conn, new_cid, dept, cnum, name, units, max_enroll, 
            prereq, instruct, dr, sem_offered, year_offered, type, 
            type_notes, major_freq)

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
                                type = type,
                                type_notes = type_notes,
                                major_freq = major_freq,
                                cid = cid,
                                majors = majors)
        elif request.form['submit'] == 'delete':
            delete_course(conn, cid)
            flash("Movie successfully deleted!")
            return redirect(url_for('index'))
        elif request.form['submit'] == 'add':
            new_dept = request.form.get('new_dept')
            new_dept_id = find_dept_id(conn, new_dept)
            print(str(new_dept) + ' id: ' + str(new_dept_id))
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
            type = info[11]
            type_notes = info[12]
            major_freq = info[13]
            majors = find_pairs(conn, cid)
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
                                type = type,
                                type_notes = type_notes,
                                major_freq = major_freq,
                                cid = cid,
                                majors = majors)
        else:
            flash("Error")
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
