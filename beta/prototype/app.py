# ==============================================================================
#   Import Modules
# ==============================================================================
from pdb import find_function
from re import split
from flask import (Flask, render_template, make_response, url_for, request,
                   redirect, flash, session, send_from_directory, jsonify)
from werkzeug.utils import secure_filename
app = Flask(__name__)

import cs304dbi as dbi
from prepared_queries import *

# ==============================================================================
#   Routing functions
# ==============================================================================
@app.route('/', methods=['GET','POST'])
def index():
    conn = dbi.connect()
    if request.method == 'GET':
        return render_template('index.html', page_title='Add Rule')
    else:
        arg = []
        description = request.form.get('description') 
        nfrom = request.form.get('op')
        op = 'nfrom-' + nfrom

        if request.form['submit'] == 'add': # BUGGY!
            abbrev = request.form.get('abbrev')
            cnum = request.form.get('cnum')
            # need to create arg 
            arg.append([str(abbrev) + ' ' + str(cnum)])
            return render_template('index.html', page_title='Add Rule',
                               arg = arg)
        
        # abbrev = request.form.get('abbrev')
        # cnum = request.form.get('cnum')
        # # need to create arg 
        # arg = [str(abbrev) + ' ' + str(cnum)]

        
        # 1) construct a dictionary in the browser (front-end), serialize it 
        # 2) hidden form input, normal 
        # <input type="hidden" value="" name="course_list">
        #
        
        # Create JSON
        json = dict()
        json['description'] = description
        json['op'] = op
        json['arg'] = arg
        return render_template('index.html', page_title='Add Rule',
                               json = json,
                               arg = arg)


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
