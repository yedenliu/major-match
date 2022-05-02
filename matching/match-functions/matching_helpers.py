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
# Helper Functions
# ------------------------------------------------------------------------------
def get_majors(userInput):
    ''' 
    Determines which majors a user has made progress towards 
    (so they don't need to check all)
    
    Param - User input
    Return - list of majors that we need to check
    '''
    tempMajors = []
    with open(coursesToMajors, "r") as ctm:
        for row in ctm:
            rho = row.split('\t')
            if rho[1] in userInput:
                for item in rho[2:]:
                    if len(item) > 2:
                        tempMajors.append(item)
    majorsToCheck = []
    [majorsToCheck.append(x) for x in tempMajors if x not in majorsToCheck]
    majorsToCheck.sort()
    return(majorsToCheck)

def get_all_courses(conn):
    ''' 
    Getter for all courses in database
    
    Param - department abbreviation, course number
    Return - connection object, course ID
    '''
    curs = dbi.cursor(conn)
    sql = ''' select cnum, dept from courses '''
    curs.execute(sql)
    return curs.fetchall()

def findElectives(requiredList, allCoursesList):
    ''' 
    findElectives() takes two lists: the courses that are required for a
    major, and the courses that count towards that major. It returns a list of
    the courses that count as elective courses for that major.
    '''
    electiveList = []
    for element in allCoursesList:
        if len(element) < 6:
            pass
        elif element == '\n':
            pass
        elif element not in requiredList:
            electiveList.append(element)
    return(electiveList)

def courseLevelUntangler(electiveList, level):
    ''' 
    courseLevelUntangler() takes a list and a course level. It returns a list
    of electives at the designated level, i.e. will take a list of the CS electives
    and will return only the 300 level electives.
    '''
    levelElectives = []
    for elective in electiveList:
        courseNum = int(elective.split(" ")[1][0])
        if courseNum == level:
            levelElectives.append(elective)
    return(levelElectives)

def compareUserAndReqs(user, reqList, reqName, needed):
    '''
    compareUserAndReqs() compares the courses a user has taken against the
    courses they need to take for a specific course type within a major. For
    example, it would compare the list of courses taken... wait, maybe I can
    just pop the courses in the nested if statements 
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
    for course in taken:
        if taken in path:
            path.remove(taken)
    if len(path) == 0:
        return(True)
    else:
        return(False)

def multilistedSatisfied(courseToCompare, coursesToCompareTo):
    if courseToCompare in coursesToCompareTo:
        return(True)
    else:
        return(False)