from pdb import find_function
from flask import (Flask, render_template, make_response, url_for, request,
                   redirect, flash, session, send_from_directory, jsonify)
from werkzeug.utils import secure_filename
app = Flask(__name__)

import cs304dbi as dbi
import random
from prepared_queries import *
from flask_cas import CAS 

CAS(app)

app.config['CAS_SERVER'] = 'https://login.wellesley.edu:443'
app.config['CAS_LOGIN_ROUTE'] = '/module.php/casserver/cas.php/login'
app.config['CAS_LOGOUT_ROUTE'] = '/module.php/casserver/cas.php/logout'
app.config['CAS_VALIDATE_ROUTE'] = '/module.php/casserver/serviceValidate.php'
app.config['CAS_AFTER_LOGIN'] = 'logged_in'
# the following doesn't work :-(
app.config['CAS_AFTER_LOGOUT'] = 'after_logout'

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
@app.route('/', methods=['GET','POST'])
def index():
    conn = dbi.connect()
    username = None
    print(request.cookies.keys())
    if 'CAS_USERNAME' in session:
        username = session['CAS_USERNAME']
        print(('CAS_USERNAME is: ',username))
    else:
        print('CAS_USERNAME not in session')
    if request.method == 'GET':
        resp = make_response( render_template('index.html',
                                              username=username,
                                              page_title='Home') )
        return resp
    else:
        classes = []
        for n in range(33): # range is the number of total courses they can input
            dept = request.form.get('dept-'+str(n))
            cnum = request.form.get('cnum-'+str(n))
            
            if dept not in [None, ''] and cnum not in [None, '']:
                dept = dept.upper().strip()
                cnum = cnum.upper().strip()
                classes.append((dept,cnum))
                insert_data(conn, dept, cnum)
                results = major_match(conn)
        delete_form_data(conn)
        resp = make_response(render_template('results.html',
                                page_title='Results',
                                classes = classes,
                                results = results))
        # resp.set_cookie('testkey', 'testval')
        return resp

@app.route('/results/')
def departments():
    classes = []
    return render_template('results.html',
                            page_title='Results',
                            classes = classes)

@app.route('/logged_in/')
def logged_in():
    flash('successfully logged in!')
    return redirect( url_for('index') )

@app.route('/after_logout/')
def after_logout():
    flash('successfully logged out!')
    return redirect( url_for('index') )
    
################################################################################
@app.before_first_request
def init_db():
    dbi.cache_cnf()
    # set this local variable to 'wmdb' or your personal or team db
    db_to_use = 'majormatch_db' 
    dbi.use(db_to_use)
    print('will connect to {}'.format(db_to_use))
    print('Run with http://cs.wellesley.edu:port where port in 1943-1952')

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
