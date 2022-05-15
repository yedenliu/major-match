################################################################################
#   Import Modules
################################################################################
from pdb import find_function
from re import split
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
#   Routing functions
################################################################################
@app.route('/', methods=['GET','POST'])
def index():
    conn = dbi.connect()
    if request.method == 'GET':
        depts = get_depts(conn)
        return render_template('index.html',page_title='Home', depts=depts)
    else:
        classes = []
        results = []
        course_matches = []
        for n in range(0, 32): # range is the number of total courses they can input
            dept = request.form.get('dept-'+str(n))
            cnum = request.form.get('cnum-'+str(n))
            if dept not in [None, ''] and cnum not in [None, '']:
                cnum = cnum.upper().strip()
                
                # if course doesnt exist
                if not check_course_exists(conn, dept, cnum):
                    flash(str(dept) + ' ' + str(cnum) + 
                          " doesn't exist in our database")

                classes.append((dept,cnum))
                insert_data(conn, dept, cnum)
                results = major_match(conn)
                course_matches = matched_courses(conn)
        delete_form_data(conn)
        
        # get all the courses in each department
        dept_courses = [(get_dept_courses(conn, results[i][2])) for i in range(len(results))]
        courses_to_take_dict = {results[i][0]:dept_courses[i] for i in range(len(results))}
        for i in range(len(dept_courses)):
            course_list = []
            for j in range(len(dept_courses[i])):
                course_list.append(dept_courses[i][j][2])
            courses_to_take_dict[list(courses_to_take_dict.keys())[i]] = course_list
        
        # find the percentage of courses that have been taken for each matched major
        percentage = [format((results[i][1] / len(dept_courses[i])), '.0') for i in range(len(results))]
        p = [(int((float(x)*100)),'') for x in percentage]
        # results = (major, count matched courses, dept_id, percent courses taken, empty string)
        results = [results[i]+ tuple(p[i]) for i in range(len(results))]

        # put the courses with the majors they fulfill 
        courses_taken_dict = {course_matches[i][1]:[] for i in range(len(course_matches))}
        for i in range(len(course_matches)):
            courses_taken_dict[course_matches[i][1]].append(course_matches[i][0])

        # subtract courses taken from dept courses and put dept courses still needed into dict

        
        # for major in courses_to_take_dict:
            # print(major)
            # get the taken courses and subtract from the dept courses
            # print((courses_to_take_dict[major]),'\n', (courses_taken_dict[major]))
            # toTake = list(set(courses_to_take_dict[major]) - set(courses_taken_dict[major]))
            # print('totake: ',len(toTake))
            # put the leftover courses into dict
            # courses_to_take_dict[major] = toTake
            # print(len(courses_to_take_dict[major]))

        # print(courses_to_take_dict['Computer Science'])
        

        return render_template('results.html',
                                page_title='Results',
                                classes = classes,
                                results = results,
                                course_matches = course_matches,
                                )
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
