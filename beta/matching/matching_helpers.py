# ------------------------------------------------------------------------------
# Import Modules
# ------------------------------------------------------------------------------
import pandas as pd
import os
import cs304dbi as dbi

# ------------------------------------------------------------------------------
# Making Paths Generalizable for Users
# ------------------------------------------------------------------------------
cwd = os.getcwd()
parent_dir = os.path.abspath(os.path.join(cwd, os.pardir))
majorReqs = os.path.join(parent_dir, 'DDL', 'majorReqsDF.tsv')
coursesToMajors =  os.path.join(parent_dir, 'DDL', 'coursesToMajors.tsv')

# ------------------------------------------------------------------------------
# Getter Functions
# ------------------------------------------------------------------------------
def grabMajors(conn):
    ''' 
    Determines which majors a user has made progress towards 
    (so they don't need to check all)
    
    Param - connection object
    Return - list of majors that we need to check
    '''
    curs = dbi.cursor(conn)
    sql = '''   select programs.name, programs.dept_id from form_data
                inner join major_pairs using(cid)
                inner join programs using(dept_id)
            '''
    curs.execute(sql)
    return curs.fetchall()

def grabAllCourses(conn):
    ''' 
    Getter for all courses in database
    
    Return - connection object, course number, and dept abbrev.
    '''
    curs = dbi.cursor(conn)
    sql =   ''' select dept, cnum from courses
            '''
    curs.execute(sql)
    return curs.fetchall() # allCoursesList

def grabMajorCourses(conn, major_name):
    ''' 
    Getter for all courses in database
    
    Return - connection object, course number, and dept abbrev.
    '''
    curs = dbi.cursor(conn)
    sql =   ''' select dept, cnum from courses
                inner join major_pairs using(cid)
                inner join programs using(dept_id)
                where programs.name = %s
            '''
    curs.execute(sql, [major_name])
    elements = curs.fetchall() 
    courses = []
    for e in elements:
        courses.append(str(e[0]) + ' ' + str(e[1]))
    return courses # majorCourses
# ------------------------------------------------------------------------------
# Course Sorting Functions
# ------------------------------------------------------------------------------
def findElectives(requiredList, allCoursesList):
    ''' 
    Param - two lists   (1) the courses that are required for a major, 
                        (2) and the courses that count towards that major. 
    Return - list of the courses that count as elective courses for that major.
    '''
    electiveList = []
    for element in allCoursesList:
        if element not in requiredList:
            electiveList.append(element)
    return electiveList

def courseLevelUntangler(electiveList, level):
    ''' 
    Param - a list and a course level. 
    Return - list of electives at the designated level, 
    i.e. will take a list of the CS electives, returns only the 300-levels
    '''
    levelElectives = []
    for elective in electiveList:
        courseLevel = elective[1][0]
        if courseLevel == level: # ex: if 3 == 3
            levelElectives.append(elective)
    return levelElectives

# ------------------------------------------------------------------------------
# Printing/ Formatting/ Debugging Functions
# ------------------------------------------------------------------------------
def compareUserAndReqs(user, reqList, reqName, needed):
    '''
    Compares the courses a user has taken against the courses they need to take 
    for a specific course type within a major.
    
    ??? need help w/ this
    Param - user: 
            reqList:
            reqName:
            needed:
    Return - 
    '''
    # TODO: try just popping courses
    has = len(user)
    count = 1
    for course in user:
        print(course, 'fulfills', count, 'of', needed, reqName, 'requirements')
        count += 1
    if needed <= has:
        print("You've fulfilled all", reqName, "requirements for the major!\n")
    else:
        print('You need', (needed - has), 'more courses to fulfill all', reqName, "requirements for the major!\n")

def suggestComplete(taken, neededNum, options, core, pathNum):
    ''' 
    suggestComplete() will print out a list of courses each user could or
    should take if they wanted to complete a major. This is mostly useful for
    testing purposes.
    '''
    if len(taken) < neededNum:
        for course in taken:
            if course in options:
                options.remove(course)
        if core and (len(options) != 0):
            if pathNum == 0:
                print('\tYou must take these course(s):')
                for course in options:
                    print('\t\t', course)
                print('')
            elif pathNum != 0:
                print('\tAnd wish to complete core path #', pathNum, ',you must take these course(s):')
                for course in options:
                    print('\t\t', course)
                print('') 
        elif not core and (len(options) != 0):
            print('\tYou should select', neededNum, 'course(s) from the following list:')
            for course in options:
                print('\t\t', course)
            print('')

def completedPath(taken, path):
    '''
    Only needed for complex, multi-path majors 
    Ex: Chem, Bio
    '''
    for course in taken:
        if taken in path:
            path.remove(taken)
    if len(path) == 0:
        return(True)
    else:
        return(False)