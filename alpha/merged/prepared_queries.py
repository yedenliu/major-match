from tkinter import ttk
import cs304dbi as dbi

################################################################################
#   Helpers Matching front-end
################################################################################

def find_cid(conn, dept, cnum):
    ''' 
    Finds course id number based on department and course number from db
    
    Param - department abbreviation, course number
    Return - connection object, course ID
    '''
    curs = dbi.cursor(conn)
    sql = '''   select cid from courses
                where dept = %s and cnum = %s
            '''
    curs.execute(sql, [dept, cnum])
    return curs.fetchone()

def insert_data(conn, dept, cnum):
    '''
    Inserts user's inputted form data into a semi-temporary table
    (when we implement CAS, course data will be saved for each user)
    
    Param - connection object, department abbreviation, course number 
    '''
    curs = dbi.cursor(conn)
    if dept != None and cnum != None:
        cid = find_cid(conn, dept, cnum)
        sql = '''   insert into form_data(dept, cnum, cid)
                    values (%s, %s, %s)
                ''' 
        curs.execute(sql, [dept, cnum, cid])
        conn.commit()

def major_match(conn):
    '''
    Getting top five major matches for courses user has inputted
    Ordered by count
    
    Param - connection object
    '''
    curs = dbi.cursor(conn)
    sql = '''   select programs.name, count(major_pairs.dept_id) from programs
                inner join major_pairs using(dept_id)
                inner join form_data using(cid)
                group by major_pairs.dept_id
                order by count(major_pairs.dept_id) DESC
                limit 5
            ''' 
    curs.execute(sql)
    return curs.fetchall()

def delete_form_data(conn):
    '''
    TEMPORARY FUNCTION (until CAS is implemented)
    Deletes data from form_data table
    '''
    curs = dbi.cursor(conn)
    sql = 'delete from form_data'
    curs.execute(sql)
    conn.commit()
    
################################################################################
#   Helpers for courses table 
################################################################################

def insert_course(conn, dept, cnum, name, units, max_enroll, 
                  prereq, instruct, dr, sem_offered, year_offered):
    '''
    Insert course into the major match database

    Param - connection object + all the course information from catalog 
    '''
    curs = dbi.cursor(conn)
    # prepared query
    sql = '''   insert into courses(dept, cnum, `name`, units, max_enroll, 
                prereq, instruct, dr, sem_offered, year_offered)
                values (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s)
            '''
    curs.execute(sql,   [dept, cnum, name, units, max_enroll, 
                        prereq, instruct, dr, sem_offered, year_offered])
    conn.commit()

def course_exists(conn, dept, cnum):
    '''
    Checks if course already exists in database

    Param - connection ojbect, department abbreviation + course number
    Return - true if course already exists
    '''
    curs = dbi.cursor(conn)
    sql = ''' select * from courses where dept = %s and cnum = %s '''
    curs.execute(sql, [dept, cnum])
    movie = curs.fetchall()
    return len(movie) > 0

def get_course_info(conn, cid):
    '''
    Getter for course info based on the course ID

    Param - connection ojbect, course ID 
    Return - course info (in list object)
    '''
    curs = dbi.cursor(conn)
    sql = '''   select * from courses
                where cid = %s
            '''
    curs.execute(sql, [cid])
    return curs.fetchone()

def update_course(conn, cid, dept, cnum, name, units, max_enroll, prereq, 
instruct, dr, sem_offered, year_offered, type, type_notes, major_freq):
    '''
    Checks if course already exists in database

    Param - connection object + all the course information from catalog 
    Return - true if course already exists
    '''
    curs = dbi.cursor(conn)
    # prepared query
    sql = '''   update courses
                set 
                dept = %s, 
                cnum = %s, 
                name = %s, 
                units = %s, 
                max_enroll = %s, 
                prereq = %s, 
                instruct = %s, 
                dr = %s, 
                sem_offered = %s, 
                year_offered = %s, 
                type = %s, 
                type_notes = %s, 
                major_freq = %s
                where cid = %s
            '''
    curs.execute(sql, [ dept, 
                        cnum, 
                        name, 
                        units, 
                        max_enroll, 
                        prereq, 
                        instruct, 
                        dr, 
                        sem_offered, 
                        year_offered, 
                        type, 
                        type_notes, 
                        major_freq,
                        cid])
    conn.commit()

def delete_course(conn, cid):
    curs = dbi.cursor(conn)
    # prepared query
    sql = '''   delete from courses
                where cid = %s
            '''
    curs.execute(sql, [cid])
    conn.commit()

def find_incomplete(conn):
    '''
    Finds incomplete courses, where they have NULL fields

    Param - connection object
    Return - List of courses with incomplete information
    ''' 
    # prepared query
    curs = dbi.cursor(conn)
    sql = '''   select dept, cnum, cid from courses 
                where dept is NULL 
                or `name` is NULL
                or units is NULL
                or max_enroll is NULL
                or prereq is NULL
                or instruct is NULL
                or dr is NULL
                or sem_offered is NULL
                or year_offered is NULL
                or type is NULL
                or type_notes is NULL'''
    curs.execute(sql)
    return curs.fetchall()

################################################################################
#   Helpers for programs table 
################################################################################

def get_departments(conn):
    '''
    Finds the courses that count towards majors in a department 
    
    Param - connection object
    Return - list of departments 
    '''
    curs = dbi.cursor(conn)
    sql = 'select * from programs'
    curs.execute(sql)
    return curs.fetchall()

def find_dept_name(conn, dept_id):
    '''
    Finds a department's name from their department ID
    
    Param - connection object, department ID
    Return - department name 
    '''
    curs = dbi.cursor(conn)
    sql = '''   select name from programs
                where dept_id = %s
            '''
    curs.execute(sql, [dept_id])
    row = curs.fetchone()
    return row[0]

def find_dept_courses(conn, dept_id):
    '''
    Finds the courses that count towards majors in a department 
    
    Param - connection object, department 
    Return - list of courses 
    '''
    curs = dbi.cursor(conn)
    
    sql =   ''' select dept, cnum, courses.name, courses.cid 
                from courses 
                inner join major_pairs using(cid)
                inner join programs using (dept_id)
                where dept_id = %s
            '''
    curs.execute(sql, [dept_id])
    return curs.fetchall()

################################################################################
#   Helpers for major_pairs table 
################################################################################

def add_pair(conn, dept_id, cid):
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

def remove_pair(conn, dept_id, cid):
    '''
    Removes a pair of dept ID and course ID to the major pairs table
    
    Param - connection object, department ID, course ID
    '''
    curs = dbi.cursor(conn)
    sql = '''   delete from major_pairs
                where dept_id = %s and cid = %s
            '''
    curs.execute(sql, [dept_id, cid])
    conn.commit()

def find_pairs(conn, cid):
    '''
    Finds majors that a course counts towards given its cid
    
    Param - connection object, course ID
    Return - tuple of department name and dept ID
    '''
    curs = dbi.cursor(conn)
    sql =   ''' select `name`, dept_id from programs 
                inner join major_pairs using(dept_id)
                where major_pairs.cid = %s
            '''
    curs.execute(sql, [cid])
    majors = []
    for major in curs.fetchall():
        majors.append(major)
    return majors

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
