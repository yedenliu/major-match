from tkinter import ttk
import cs304dbi as dbi

'''
1. Accept the dept abbr and course number from form data --> put into DB 
2. Match course to database courses 
3. Get majors on matched courses 
4. Get count of each major that is listed the most 
'''

def get_depts(conn):
    curs = dbi.cursor(conn)
    sql =   ''' select distinct dept 
                from courses 
                where dept <> '' 
            '''
    curs.execute(sql)
    deptsTups = curs.fetchall()
    deptsList = [i[0] for i in deptsTups]
    return deptsList

def find_cid(conn, dept, cnum):
    curs = dbi.cursor(conn)
    sql = '''   select cid from courses
                where dept = %s and cnum = %s
            '''
    curs.execute(sql, [dept, cnum])
    return curs.fetchone()

def insert_data(conn, dept, cnum):
    curs = dbi.cursor(conn)
    if dept != None and cnum != None:
        cid = find_cid(conn, dept, cnum)
        sql = '''   insert into form_data(dept, cnum, cid)
                    values (%s, %s, %s)
                ''' 
        curs.execute(sql, [dept, cnum, cid])
        conn.commit()

def check_course_exists(conn, dept, cnum):
    curs = dbi.cursor(conn)
    sql = '''   select cid from courses
                where dept = %s and cnum = %s
            '''
    curs.execute(sql, [dept, cnum])
    return len(curs.fetchall()) > 0

def major_match(conn):
    curs = dbi.cursor(conn)
    sql = '''   select programs.name, count(major_pairs.dept_id) 
                from programs
                inner join major_pairs using(dept_id)
                inner join form_data using(cid)
                group by major_pairs.dept_id
                order by count(major_pairs.dept_id) DESC
                limit 5
            ''' 
    curs.execute(sql)
    return curs.fetchall()

# FOR DEBUGGING
def matched_courses(conn):
    curs = dbi.cursor(conn)
    sql = '''   select courses.name, programs.name from courses
                inner join form_data using(cid)
                inner join major_pairs using(cid)
                inner join programs using(dept_id)
                order by programs.name
            ''' 
    curs.execute(sql)
    return curs.fetchall()

def delete_form_data(conn):
    curs = dbi.cursor(conn)
    sql = 'delete from form_data'
    curs.execute(sql)
    conn.commit()