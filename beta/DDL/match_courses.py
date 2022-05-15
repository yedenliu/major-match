################################################################################
#   Import Modules
################################################################################
import cs304dbi as dbi
import csv

################################################################################
#   Helper Functions 
################################################################################
    
def find_cid(conn, abbrev, cnum):
    '''
    Given the dept abbreviation and course number, find the course ID
    
    Param - connection object, dept abbrev, course number
    Return - course ID (cid)
    '''
    curs = dbi.cursor(conn)
    # prepared query
    sql =   ''' select cid from courses
                where dept = %s and cnum = %s
            '''
    curs.execute(sql, [abbrev, cnum])
    return curs.fetchone()

def find_dept_id(conn, dept_name):
    '''
    Finds a dept ID based on the department name
    
    Param - connection object, department name
    Return - dept ID
    '''
    curs = dbi.cursor(conn)
    sql = '''   select dept_id from programs
                where `name` = %s
            '''
    curs.execute(sql, [dept_name])
    row = curs.fetchone()
    return row

################################################################################
#   Table Functions 
################################################################################
   
def update_freq(conn, freq, cid):
    '''
    Update the major frequency attribute of a given course
    (i.e., how many majors it counts towards)
    
    Param - connection oject, major frequency, course ID
    '''
    curs = dbi.cursor(conn)
    # prepared query
    sql =   ''' update courses
                set major_freq = %s
                where cid = %s
            '''
    curs.execute(sql, [freq, cid])
    conn.commit()
    
def insert_pair(conn, dept_id, cid):
    '''
    Adds a pair of dept ID and course ID to the major pairs table 
    
    Param - connection object, department ID, course ID
    '''
    curs = dbi.cursor(conn)
    sql = '''   insert into major_pairs(dept_id, cid)
                values (%s, %s)
            ''' 
    curs.execute(sql, [dept_id, cid])
    conn.commit()

################################################################################
#   Matching for major_pairs table 
################################################################################

def match(conn):
    '''
    Every row in the imported tsv is a course with information on the majors it
    counts towards. We parse through each row and make relevant changes to our 
    database tables
    
    Param - connection object
    '''
    with open('completeMajorTable.tsv', 'r') as file:
        # 'buggy_courses.tsv' // 'completeMajorTable.tsv'
        tsv_reader = csv.reader(file, delimiter='\t')
        for row in tsv_reader:
            abbrev = row[1]
            cnum = row[2]
            freq = row[3]
            majors = row[4]
            # clean major column
            majors = majors.strip('[').strip(']')
            majors = majors.split(',')
            
            # update the courses table with the major freq
            cid = find_cid(conn, abbrev, cnum)
            update_freq(conn, freq, cid)
            
            for major in majors:
                dept_name = major.strip().strip("'").strip()
                try:
                    # insert into major_pairs table
                    dept_id = find_dept_id(conn, dept_name)
                    insert_pair(conn, dept_id, cid)
                except:
                    print("FAIL: " + str(abbrev) + str(cnum))

################################################################################
#   Running the functions
################################################################################

dbi.cache_cnf()
dbi.use('majormatch_db')
conn = dbi.connect()

match(conn)