################################################################################
#   Import Modules
################################################################################
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
#   Routing functions
################################################################################
@app.route('/', methods=['GET','POST'])
def index():
    conn = dbi.connect()
    if request.method == 'GET':
        return render_template('index.html',page_title='Home')
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
        delete_form_data(conn) # DELETE WHEN CAS IS IMPLEMENTED
        return render_template('results.html',
                                page_title='Results',
                                classes = classes,
                                results = results)

@app.route('/results/')
def departments():
    classes = []
    return render_template('results.html',
                            page_title='Results',
                            classes = classes)

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
