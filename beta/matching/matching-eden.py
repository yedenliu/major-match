
################################################################################
# Import Modules
################################################################################
from asyncio import subprocess
from matching_helpers import *

################################################################################
# Major Functions
################################################################################

def polisci(userInput):
    conn = dbi.connect()
    # --------------------------------------------------------------------------
    # MAJOR REQUIREMENTS -------------------------------------------------------
    # Listing out categories of courses
    intro = ['POL 100'] # needs to be in this formt -> 'CS111'
    core = [] # i think there is no strictly required courses 

    # Courses 
    majorCourses = grabMajorCourses(conn, 'Political Science')
    electives = findElectives(core, majorCourses)
    threes = courseLevelUntangler(electives, 3)
    twos = courseLevelUntangler(electives, 2)
    # --------------------------------------------------------------------------
    # USER INPUT ---------------------------------------------------------------
    taken = 0 
    allTaken = [] 
    threesTaken = []
    twosTaken = []
    electivesTaken = []
    
    # Sorting through user input
    for course in userInput:
        allTaken.append(course)
        taken += 1
        if course in intro: # 100-levels
            electivesTaken.append(course)
        if course in twos:
            twosTaken.append(course)
        if course in threes:
            threesTaken.append(course)
    # --------------------------------------------------------------------------
    ''''
    REQUIREMENTS
    1. One 200/300 level course in each subfields (4)
    2. Two 300-level courses in two diff subfields, one must be seminar (2)
    3. additional courses, in any subfield (3+)
    '''
    # --------------------------------------------------------------------------
    # DEAL WITH 300-LEVELS -----------------------------------------------------
    # Requirement 1: at least two 300 level in diff subfields
    req1 = False
    # Requirement 2: at least 1 seminar DEBUG --> HOW DO WE CHECK IF SEMINAR??
    # if Sem: or Seminar: in name 
    req2 = False 
    
    if len(threes) > 1: # if more than one 300 level has been taken
        sub1 = threes[0][3]
        sub2 = threes[1][3]
        req1 = sub1 != sub2 # true if diff
        
    if req1 == True:
        print('SATISFIED: at least two 300 level in different subfields')
    else:
        print('FAILED: at least two 300 level in different subfields')
        print('You have completed: ' + str(len(threes)) + ' 300-levels')
        subs = [course[3] for course in threes]
        print('In these subfields: ' + str(subs))
        
    if req2 == True:
        print('SATISFIED: at least one 300-level is a seminar')
    else:
        print('FAILED: at least one 300-level is a seminar')
    # --------------------------------------------------------------------------
    # DEAL WITH SUBFIELD DISTRIBUTIONS -----------------------------------------
    req3 = False
 
    subfields = twos + threes
    subCount = []
    for course in subfields:
        # course ex: (POL1, 100)
        subCount.append(course[0][4]) # should append number
    subSet = set(subCount) # sets only take unique
    unique_val = len(subSet)
    
    if len(unique_val) == 4: # there are 4 distinct subfields
        req3 = True
    
    if req3 == True:
        print('SATISFIED: One 200/300 level course in each of the 4 subfields')
    else:
        print('FAILED: One 200/300 level course in each of the 4 subfields')
        print('Your have completed only:' + unique_val)
    # --------------------------------------------------------------------------
    # DEAL WITH ELECTIVES ------------------------------------------------------
    req4 = False
    if course in allTaken and course not in subfields:
        electivesTaken.append(course)
    
    req4 = len(electivesTaken) >= 3 # true if 3+ electives
    
    if req4 == True:
        print('SATISFIED: 3+ electives')
    else:
        print('FAILED: 3+ electives')
        print('You have completed only:' + len(electivesTaken))
    
# ------------------------------------------------------------------------------
def masterCheck(userInput):
    majorsToCheck = grabMajors(userInput)
    if 'Political Science' in majorsToCheck:
        polisci(userInput)

# ------------------------------------------------------------------------------
# Implementing
# ------------------------------------------------------------------------------
dbi.cache_cnf()
dbi.use('majormatch_db')
conn = dbi.connect()

# insert temp data 

# TESTING
## user input should look like a list of (dept, cnum)
a = ['POL1 200','WRIT 166']

polisci(a)
