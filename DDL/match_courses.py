################################################################################
#   Import Modules
################################################################################
import cs304dbi as dbi
import os, csv

################################################################################
#   Create 
################################################################################

def insert_cid(conn, abbrev):
    curs = dbi.cursor(conn)
    # prepared query
    sql =   ''' insert into major_pairs(cid, dept)
                select cid, dept from courses
                where dept = 'AFR' or dept = %s
            '''
    curs.execute(sql, [abbrev])
    conn.commit()

def update_dept(conn, dept_id, abbrev):
    curs = dbi.cursor(conn)
    # prepared query
    sql =   ''' update major_pairs
                set dept_id = %s
                where dept = %s
            '''
    curs.execute(sql, [dept_id, abbrev])
    conn.commit()

def match(conn):
    with open('abbrev.tsv', 'r') as file:
        tsv_reader = csv.reader(file, delimiter='\t')
        for row in tsv_reader:
            dept_id = row[0]
            abbrev = row[1]
            try:
                insert_cid(conn, abbrev)
                update_dept(conn, dept_id, abbrev)
                print("SUCCESS! Dept: " + abbrev + " worked!")
            except:
                print("Department " + abbrev + " did not work")
    drop_col(conn)

dbi.cache_cnf()
dbi.use('majormatch_db')
conn = dbi.connect()

match(conn)