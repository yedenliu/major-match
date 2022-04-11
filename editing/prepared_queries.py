################################################################################
#   Import Modules
################################################################################
from tkinter import ttk
import cs304dbi as dbi
from flask import flash

################################################################################
#   Helpers for courses table 
################################################################################

def insert_course(conn, dept, cnum, name, units, max_enroll, 
                  prereq, instruct, dr, sem_offered, year_offered):
    curs = dbi.cursor(conn)
    # prepared query
    sql = '''   insert into course(dept, cnum, `name`, units, max_enroll, 
                prereq, instruct, dr, sem_offered, year_offered)
                values (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s)
            '''
    curs.execute(sql,   [dept, cnum, name, units, max_enroll, 
                        prereq, instruct, dr, sem_offered, year_offered])
    conn.commit()

def get_course_info(conn, cid):
    curs = dbi.cursor(conn)
    sql = '''   select * from courses
                where cid = %s
            '''
    curs.execute(sql, [cid])
    return curs.fetchone()

def update_course(conn, cid, dept, cnum, name, units, max_enroll, prereq, 
instruct, dr, sem_offered, year_offered, type, type_notes, major_freq):
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

################################################################################
#   Helpers for programs table 
################################################################################

def get_departments(conn):
    curs = dbi.cursor(conn)
    sql = 'select * from programs'
    curs.execute(sql)
    return curs.fetchall()

def find_dept_name(conn, dept_id):
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
    '''
    curs = dbi.cursor(conn)
    
    sql = '''   select dept, cnum, courses.name, courses.cid 
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

# function to add major/course pair
def add_pair(conn, dept_id, cid):
    curs = dbi.cursor(conn)
    sql = '''   insert into major_pairs(dept_id, cid)
                values (%s, %s)
            ''' 
    curs.execute(sql, [dept_id, cid])
    conn.commit()


# function to remove major/course pair 
def remove_pair(conn, dept_id, cid):
    curs = dbi.cursor(conn)
    sql = '''   delete from major_pairs
                where dept_id = %s and cid = %s
            '''
    curs.execute(sql, [dept_id, cid])
    conn.commit()

# function to find majors that a course counts towards given its cid
def find_pairs(conn, cid):
    curs = dbi.cursor(conn)
    sql = '''   select `name` from programs 
                inner join major_pairs using(dept_id)
                where major_pairs.cid = %s
            '''
    curs.execute(sql, [cid])
    return curs.fetchall()


def find_cid(conn, dept, cnum):
    curs = dbi.cursor(conn)
    print(repr(dept))
    print(repr(cnum))
    sql = '''   select cid from courses
                where dept = %s and cnum = %s
            '''
    curs.execute(sql, [dept, cnum])
    row = curs.fetchone()
    print(repr(row[0]))
    return row[0]