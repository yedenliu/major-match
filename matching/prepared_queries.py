from tkinter import ttk
import cs304dbi as dbi

<<<<<<< HEAD
=======
'''
1. Accept the dept abbr and course number from form data --> put into DB 
2. Match course to database courses 
Get majors on matched courses 
Get count of each major that is listed the most 
'''

def get_depts(conn):
    curs = dbi.cursor(conn)
    sql = '''select distinct dept from courses where dept <> '' '''
    curs.execute(sql)
    deptsTups = curs.fetchall()
    deptsList = [i[0] for i in deptsTups]
    return deptsList

>>>>>>> origin/hannah
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