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

@app.route('/')
def index():
    return render_template('index.html',page_title='Mainpage')

@app.route('/departments/')
def departments():
    conn = dbi.connect()
    departments = get_departments(conn)
    return render_template('departments.html',
                            page_title='Departments',
                            departments = departments)

@app.route('/departments/<dept_id>')
def department_page(dept_id):
    conn = dbi.connect()
    name = find_dept_name(conn, dept_id) 
    courses = find_dept_courses(conn, dept_id) # dept, cnum, courses.name, cid
    print(repr(courses))
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
                                cid = cid)
    else:
        if request.form['submit'] == 'update':
            # must be able to update TT but must be a unique cid
            tt = request.form.get('movie-tt')
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
            type = request.form.get('type')
            type_notes = request.form.get('type_notes')
            major_freq = request.form.get('major_freq')

            update_course(conn, cid, dept, cnum, name, units, max_enroll, 
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
                                cid = cid)
        elif request.form['submit'] == 'delete':
            delete_course(conn, cid)
            flash("Movie successfully deleted!")
            return redirect(url_for('index'))
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
