################################################################################
#   Import Modules
################################################################################
import pymysql 
import cs304dbi as dbi
from tkinter import ttk
import os

################################################################################
#   Create 
################################################################################
def load_data(conn, filename):
    curs = dbi.cursor(conn)
    # prepared query
    sql = """   load data local infile '%s'
                into table courses
                fields terminated by '\t'
                enclosed by ''''
                lines terminated by '\n'
                (dept, cnum, `name`, units, max_enroll, prereq, instruct, dr, sem_offered, year_offered)
            """
    curs.execute(sql, [filename])
    print("Success for " + filename)
    conn.commit()

def parse_folder(conn):
    folder = '/students/yl9/cs304/major-match/DDL/tsv_files' #'/students/majormatch/project/DDL/tsv_files'
    for filename in os.listdir(folder):
        dept_id = filename[:2].strip('_')
        file = os.path.join('tsv_files', dept_id+'_courses.tsv')
        print(file)
        load_data(conn, file)

dbi.cache_cnf()
dbi.use('majormatch_db')
conn = dbi.connect()

parse_folder(conn)