
################################################################################
# Import Modules
################################################################################
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
    1. One 200/300 level course in each subfields (4)
    2. Two 300-level courses in two diff subfields, one must be seminar (2)
    3. additional courses, in any subfield (3+)
    '''
    # --------------------------------------------------------------------------
    # DEAL WITH 300-LEVELS -----------------------------------------------------
    # Requirement 1: at least two 300- levels
    req1 = False
    # Requirement 2: at least two 300 level in diff subfields
    req2 = False
    # Requirement 3: at least 1 seminar DEBUG --> HOW DO WE CHECK IF SEMINAR??
    # if Sem: or Seminar: in name 
    req3 = False 
    
    if len(threes) > 1: # if more than one 300 level has been taken
        req1 = True
        req2 = threes[0][3] != threes[1][3] # true if diff
    # --------------------------------------------------------------------------
    # DEAL WITH SUBFIELD DISTRIBUTIONS -----------------------------------------
    req4 = False
 
    subfields = twos + threes
    subCount = []
    for course in subfields:
        # course ex: (POL1, 100)
        subCount.append(course[0][4]) # should append number
    subSet = set(subCount) # sets only take unique
    unique_val = len(subSet)
    
    if len(unique_val) == 4: # there are 4 distinct subfields
        req4 = True
    # --------------------------------------------------------------------------
    # DEAL WITH ELECTIVES ------------------------------------------------------
    req5 = False
    if course in allTaken and course not in subfields:
        electivesTaken.append(course)
    
    req5 = len(electivesTaken) >= 3 # true if 3+ electives
    
    print('''For the requirement of "One 200/300 level course in each subfields"
            , you have have completed''' + unique_val)
    if req1 == True:
        print('You have completed this requirement: One 200/300 level course in each subfields')
    else:
        print('You have taken this many')
# ------------------------------------------------------------------------------
def masterCheck(userInput):
    majorsToCheck = grabMajors(userInput)
    print(majorsToCheck)
    if 'Political Science' in majorsToCheck:
        pass

# ------------------------------------------------------------------------------
# Testing
# ------------------------------------------------------------------------------
## user input should look like a list of (dept, cnum)
a = [('POL1 100')]
masterCheck(a)