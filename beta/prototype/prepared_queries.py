import cs304dbi as dbi

def get_abbrev(conn):
    curs = dbi.cursor(conn)
    sql =   ''' select distinct dept 
                from courses 
                where dept <> ""
                order by dept asc 
            '''
    curs.execute(sql)
    deptsTups = curs.fetchall()
    deptsList = [i[0] for i in deptsTups]
    return deptsList

def check_course_exists(conn, dept, cnum):
    curs = dbi.cursor(conn)
    sql = '''   select cid from courses
                where dept = %s and cnum = %s
            '''
    curs.execute(sql, [dept, cnum])
    return len(curs.fetchall()) > 0


def get_dept_courses(conn, abbrev):
    '''
    Finds courses given an department abbreviation
    
    Param - connection object, department abbreviation 
    Return - list of courses (in form CS 111)
    '''
    curs = dbi.cursor(conn)
    
    sql =   ''' select dept, cnum from courses 
                where dept = %s
            '''
    curs.execute(sql, [abbrev])
    return curs.fetchall()
