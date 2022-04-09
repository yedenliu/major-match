from tkinter import ttk
import cs304dbi as dbi
from flask import flash

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

## DEPARTMENTS #################################################################

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
    curs = dbi.cursor(conn)
    
    sql = '''   select dept, cnum, courses.name, courses.cid 
                from courses 
                inner join major_pairs using(cid)
                inner join programs using (dept_id)
                where dept_id = %s
            '''
    curs.execute(sql, [dept_id])
    return curs.fetchall()
