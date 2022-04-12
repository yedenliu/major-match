################################################################################
#   Import Modules
################################################################################
import cs304dbi as dbi
import os

################################################################################
#   Create 
################################################################################
def load_data(conn, dept_id):
    curs = dbi.cursor(conn)
    # prepared query
    sql = """   load data local infile 'tsv_files/%s_courses.tsv'
                into table courses 
                fields terminated by '\t' 
                enclosed by ''''
                lines terminated by '\n'
                (dept, cnum, `name`, units, max_enroll, prereq, instruct, dr, sem_offered, year_offered);
            """
    curs.execute(sql, [dept_id])
    conn.commit()

def parse_folder(conn):
    folder = '/students/majormatch/project/DDL/tsv_files'
    for filename in os.listdir(folder):
        dept_id = filename[:2]
        print(dept_id)
        load_data(conn, dept_id)

dbi.cache_cnf()
dbi.use('majormatch_db')
conn = dbi.connect()
parse_folder(conn)