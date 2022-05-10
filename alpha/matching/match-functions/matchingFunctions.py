import pandas as pd
import csv

majorReqs = '/students/kswint/major-match/DDL/majorReqsDF.tsv'
coursesToMajors = '/students/kswint/major-match/DDL/coursesToMajors.tsv'

''' grabMajors() determines which majors a user has made progress towards.
This lets us avoid checking every single major against every course a user
has taken.

Goes into the coursesToMajors.tsv file, reads each line, and determines whether
or not the course on the given line is one the user has taken. If the user
*has* taken that course, it appends the majors that course contributes towards
to a temporary list. That list is then cleaned and sorted before being returned.'''
def grabMajors(userInput):
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

def cleanCrosslisted(course1, course2):
    print('hi')

def grabCourses(dept):
    allCourses = []
    with open(majorReqs, "r") as courses:
        for row in courses:
            rho = row.split('\t')
            if (dept).__eq__(rho[0]):
                allCourses = list(set(rho[1:]))
                allCourses.sort()
    for item in allCourses:
        if len(item) <= 6:
            allCourses.remove(item)
    return(allCourses)

''' findElectives() takes two lists: the courses that are required for a
major, and the courses that count towards that major. It returns a list of
the courses that count as elective courses for that major.'''
def findElectives(requiredList, allCoursesList):
    electiveList = []
    for element in allCoursesList:
        if len(element) < 6:
            pass
        elif element == '\n':
            pass
        elif element not in requiredList:
            electiveList.append(element)
    return(electiveList)

''' courseLevelUntangler() takes a list and a course level. It returns a list
of electives at the designated level, i.e. will take a list of the CS electives
and will return only the 300 level electives.'''
def courseLevelUntangler(electiveList, level):
    levelElectives = []
    if len(electiveList) != 0:
        for elective in electiveList:
            try:
                courseNum = int(elective.split(" ")[1][0])
                if courseNum == level:
                   levelElectives.append(elective)
            except IndexError:
                print('*******', elective, '*******')
    return(levelElectives)


'''compareUserAndReqs() compares the courses a user has taken against the
courses they need to take for a specific course type within a major. For
example, it would compare the list of courses taken... wait, maybe I can
just pop the courses in the nested if statements '''
# TODO: try just popping courses
def compareUserAndReqs(user, reqList, reqName, needed):
    has = len(user)
    count = 1
    for course in user:
        print(course, 'fulfills', count, 'of', needed, reqName, 'requirements')
        count += 1
    if needed <= has:
        print("You've fulfilled all", reqName, "requirements for the major!\n")
    else:
        print('You need', (needed - has), 'more courses to fulfill all', reqName, "requirements for the major!\n")

''' suggestComplete() will print out a list of courses each user could or
should take if they wanted to complete a major. This is mostly useful for
testing purposes.'''
def suggestComplete(taken, neededNum, options, core, pathNum):
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

def cs(userInput):
    print('Checking your requirements against the Computer Science major...')
    needed = 10
    has = 0
    introductory = ['CS 111','CS 230']
    math = ['MATH 225']
    core = ['CS 231','CS 235','CS 240']
    required = introductory + math + core
    allCourses = grabCourses('Computer Science')
    electives = findElectives(required, allCourses)
    threes = courseLevelUntangler(electives,3)
    numThrees = 0
    numElectives = 0
    introsTaken = []
    mathTaken = []
    coresTaken = []
    threesTaken = []
    electivesTaken = []
    for course in userInput:
        if course in introductory:
            introsTaken.append(course)
            has += 1
        elif course in math:
            mathTaken.append(course)
            has += 1
        elif course in core:
            coresTaken.append(course)
            has += 1
        elif (course in threes) and (numThrees < 2):
            threesTaken.append(course)
            has += 1
            numThrees += 1
        elif (course in electives) and (numElectives < 2):
            electivesTaken.append(course)
            has += 1
            numElectives += 1

    compareUserAndReqs(introsTaken, introductory, 'introductory',2)
    compareUserAndReqs(mathTaken, math, 'math',1)
    compareUserAndReqs(coresTaken, core, 'core',3)
    compareUserAndReqs(threesTaken, threes, '300-level elective',2)
    compareUserAndReqs(electivesTaken, electives, '200 or 300-level elective',2)

    print('You have completed', has, '/', needed, 'requirements for the Computer Science major.')

    taken = coresTaken + threesTaken + electivesTaken
    if has != needed: 
        print('If you would like to complete the Computer Science major, you need to take:\n')
        suggestComplete(introsTaken, int(len(introductory) - len(introsTaken)), introductory, True, 0)
        suggestComplete(mathTaken, int(len(math) - len(mathTaken)), math, True, 0)
        suggestComplete(coresTaken, int(len(core) - len(coresTaken)), core, True, 0)
        suggestComplete(threesTaken, int(2 - numThrees), threes, False, 0)
        suggestComplete(electivesTaken, int(2 - numElectives), electives, False, 0)

def econ(userInput):
    print('Checking your requirements against the Economics major...')
    coreNeeded = 6
    threesNeeded = 2
    electivesNeeded = 1
    needed = coreNeeded + threesNeeded + electivesNeeded
    has = 0
    allCourses = grabCourses('Economics')
    core = ['ECON 101','ECON 102','ECON 103','SOC 190','ECON 201','ECON 202','ECON 203']
    electives = findElectives(core, allCourses)
    threes = courseLevelUntangler(electives,3)
    coresTaken = []
    threesTaken = []
    electivesTaken = []
    numThrees = 0
    numElectives = 0
    for course in userInput:
        if course in core:
            coresTaken.append(course)
            has += 1
        if (course in threes) and (numThrees < 2):
            threesTaken.append(course)
            has += 1
            numThrees += 1
        if (course in electives) and (numElectives < 1):
            electivesTaken.append(course)
            has += 1
            numElectives += 1

    compareUserAndReqs(coresTaken, core, 'core', coreNeeded)
    compareUserAndReqs(threesTaken, threes, '300-level elective', threesNeeded)
    compareUserAndReqs(electivesTaken, electives, '200 or 300-level elective', electivesNeeded)

    print('You have completed', has, '/', needed, 'requirements for the Economics major.')

    taken = coresTaken + threesTaken + electivesTaken
    if has != needed:
        print('If you would like to complete the Economics major, you need to take:\n')
        suggestComplete(taken, coreNeeded, core, True, 0)
        suggestComplete(taken, threesNeeded, threes, False, 0)
        suggestComplete(taken, electivesNeeded, electives, False, 0)

def chem(userInput):
    print('Checking your requirements against the Chemistry major...')
    coreNeeded = 0
    needed = 11
    multicore = False
    has = 0
    
    core = [['CHEM 105/CHEM 105P','CHEM 205'],['BISC 116/CHEM 116', 'CHEM 205'],['CHEM 120']]
    core1 = []
    core2 = []
    core3 = []
    core4 = ['CHEM 211','CHEM 212','CHEM 330']
    flexChem = ['CHEM 223','CHEM 335','CHEM 341','CHEM 361']
    flexMath = ['MATH 215','MATH 205']
    flexPhys = ['PHYS 106','PHYS 108']
    allCourses = grabCourses('Chemistry')

    core1Taken = []
    core2Taken = []
    core3Taken = []
    core4Taken = []
    flexChemTaken = []
    flexMathTaken = []
    flexPhysTaken = []
    threesTaken = []

    if 'CHEM 105' in userInput:
        core1 = ['CHEM 105', 'CHEM 205']
        coreNeeded = 2
        if completedPath(userInput,core1):
            print('hi')
    elif 'CHEM 105P' in userInput:
        coreNeeded = 2
        core1 = ['CHEM 105P', 'CHEM 205']
        if completedPath(userInput,core1):
            print('hi')
    else:
        coreNeeded = 2
        core1 = ['CHEM 105/CHEM 105P','CHEM 205']
        if completedPath(userInput,core1):
            print('hi')
    

    if 'BISC 116' in userInput:
        coreNeeded = 2
        core2 = ['BISC 116', 'CHEM 205']
        if len(core1) != 0:
            multicore = True
        if completedPath(userInput,core2):
            print('hi')
    elif 'CHEM 116' in userInput:
        coreNeeded = 2
        core2 = ['CHEM 116', 'CHEM 205']
        if len(core1) != 0:
            multicore = True
        if completedPath(userInput,core2):
            print('hi')
    else:
        coreNeeded = 2
        core2 = ['BISC 116/CHEM 116', 'CHEM 205']
        if len(core1) != 0:
            multicore = True
        if completedPath(userInput,core2):
            print('hi')


    if 'CHEM 120' in userInput:
        coreNeeded = 1
        core3 = ['CHEM 120']
        if (len(core1) != 0) or (len(core2) != 0):
            multicore = True
        if completedPath(userInput,core3):
            print('hi')

    electives = findElectives((core + core4), allCourses)
    threes = courseLevelUntangler(electives,3)
    if 'CHEM 320' in threes:
        threes.remove('CHEM 320')
    if 'CHEM 331'in threes:
        threes.remove('CHEM 331')

    for course in userInput:
        if multicore:
            if len(core1) != 0:
                if course in core1:
                    core1Taken.append(course)
                    has += 1
            if len(core2) != 0:
                if course in core2:
                    core2Taken.append(course)
                    has += 1
            if len(core3) != 0:
                if course in core3:
                    core3Taken.append(course)
        if course in core4:
            core4Taken.append(course)
            has += 1
        if course in flexChem:
            flexChemTaken.append(course)
            has += 1
        if course in flexPhys:
            flexPhysTaken.append(course)
            has += 1
        if course in flexMath:
            flexMathTaken.append(course)
            has += 1
        if course in threes:
            threesTaken.append(course)
            has += 1

    compareUserAndReqs(core1Taken, core1, 'core (track 1 of 3))', coreNeeded)
    compareUserAndReqs(core2Taken, core2, 'core (track 2 of 3)', coreNeeded)
    compareUserAndReqs(core3Taken, core3, 'core (track 3 of 3)', coreNeeded)
    compareUserAndReqs(core4Taken, core4, 'core', 3)
    compareUserAndReqs(flexChemTaken, flexChem, '300-level elective', 3)
    compareUserAndReqs(flexPhysTaken, flexPhys, 'physics', 1)
    compareUserAndReqs(flexMathTaken, flexMath, 'math', 1)

    print('You have completed', has, '/', needed, 'requirements for the Chemistry major.')

    if has != needed:
        print('If you would like to complete the Chemistry major...')
        suggestComplete(core1Taken, coreNeeded, core1, True, 1)
        suggestComplete(core2Taken, coreNeeded, core2, True, 2)
        suggestComplete(core3Taken, 1, core3, True, 3)
        print('\tRegardless of the core path...')
        suggestComplete(core4Taken, 3, core4, True, 0)
        suggestComplete(threesTaken, 1, threes, False, 0)
        suggestComplete(flexChemTaken, 3, flexChem, False, 0)
        suggestComplete(flexMathTaken, 1, flexMath, False, 0)
        suggestComplete(flexPhysTaken, 1, flexPhys, False, 0)

def french(userInput):
    print('Checking your requirements against the French and Francophone Studies major...')
    needed = 9
    has = 0

    core = ['FREN 210','FREN 211','FREN 212']
    flexLang = ['FREN 202','FREN 203','FREN 205','FREN 206','FREN 211','FREN 226']
    flexCulture = ['FREN 207', 'FREN 220', 'FREN 222', 'FREN 225', 'FREN 227', 'FREN 229', 'FREN 230', 'FREN 232', 'FREN 233', 'FREN 237', 'FREN 300', 'FREN 314', 'FREN 322', 'FREN 323', 'FREN 324', 'FREN 332']
    flexLit = ['FREN 208', 'FREN 209', 'FREN 213', 'FREN 214', 'FREN 216', 'FREN 217', 'FREN 221', 'FREN 223', 'FREN 224', 'FREN 228', 'FREN 234', 'FREN 235', 'FREN 237', 'FREN 241', 'FREN 278', 'FREN 302', 'FREN 303', 'FREN 306', 'FREN 307', 'FREN 308', 'FREN 312', 'FREN 313', 'FREN 315', 'FREN 317', 'FREN 319', 'FREN 330', 'FREN 333']

    allCourses = grabCourses('French and Francophone Studies')
    print(allCourses)
    # twos = courseLevelUntangler(allCourses, 2)
    threes = courseLevelUntangler(allCourses, 3)

    numThrees = 0

    coresTaken = []
    flexLangTaken = []
    flexCultureTaken = []
    flexLitTaken = []
    threesTaken = []

    for course in userInput:
        if course in core:
            coresTaken.append(course)
            has += 1
        if (course in threes) and (numThrees < 2):
            threesTaken.append(course)
            has += 1
            numThrees += 1
        elif course in flexLang:
            flexLangTaken.append(course)
            has += 1
        elif course in flexCulture:
            flexCultureTaken.append(course)
            has += 1
        elif course in flexLit:
            flexLitTaken.append(course)
            has += 1
 
    
    compareUserAndReqs(coresTaken, core, 'core',1)
    compareUserAndReqs(flexLangTaken, flexLang, 'language',1)
    compareUserAndReqs(flexCultureTaken, flexCulture, 'culture',1)
    compareUserAndReqs(flexLitTaken, flexLit, 'literature',1)
    compareUserAndReqs(threesTaken, threes, '300-level elective',2)

    print('You have completed', has, '/', needed, 'requirements for the French and Francophone Studies major.')

    if has != needed: 
        print('If you would like to complete the French and Francophone Studies major, you need to take:\n')
        suggestComplete(coresTaken, int(len(core) - len(coresTaken)), core, False, 0)
        suggestComplete(flexLangTaken, int(len(flexLang) - len(flexLangTaken)), flexLang, False, 0)
        suggestComplete(flexCultureTaken, int(len(flexCulture) - len(flexCultureTaken)), flexCulture, False, 0)
        suggestComplete(flexLitTaken, int(len(flexLitTaken) - len(flexLit)), flexLit, False, 0)
        suggestComplete(threesTaken, int(2 - numThrees), threes, False, 0)

def masterCheck(userInput):
    majorsToCheck = grabMajors(userInput)
    # print(majorsToCheck)
    if 'Chemistry' in majorsToCheck:
        chem(userInput)
    if 'Computer Science' in majorsToCheck:
        cs(userInput)
    if 'Economics' in majorsToCheck:
        econ(userInput)
    if 'French and Francophone Studies' in majorsToCheck:
        french(userInput)

kat = ['ARTH 267','ES 267','CS 111','CS 220','CS 230','CS 231','CS 235','CS 240','CS 242','CS 301','CS 304','CS 342','FREN 101','FREN 102','FREN 201','FREN 202','HIST 245','HIST 220','JPN 290','MATH 205','MATH 206','MATH 223','MATH 225','NEUR 100','PHIL 215','POL1 200','WRIT 166']
julie = ['MATH 205', 'POL 123', 'WRIT 187', 'MATH 206', 'STAT 218', 'SPAN 241', 'CS 111', 'MATH 305', 'PHIL 216', 'CS 230', 'SPAN 253', 'MATH 349', 'MATH 225', 'WGST 218', 'CS 232', 'STAT 260', 'MATH 220', 'MATH 302', 'MATH 215', 'MATH 340', 'PHYS 107', 'STAT 309', 'MATH 322', 'PHYS 313', 'PORT 103', 'MATH 309']
a = ['AFR 204', 'AFR 204', 'ARTH 237', 'ARTH 226', 'ARTH 244', 'ARTH 247', 'ARTH 317', 'ARTH 222', 'ARTH 309', 'ARTH 256', 'ARTH 335', 'CHEM 335', 'CHEM 341', 'CHEM 325', 'CHEM 335', 'ENG 311', 'ENG 382', 'ES 201', 'HIST 213', 'SOC 322', 'HIST 256', 'HIST 231', 'AFR 209', 'ARTH 307', 'SPAN 303', 'SPAN 377', 'HIST 215', 'ARTH 201']
b = ['CS 230', 'CS 235', 'CS 232', 'CS 323', 'CS 232', 'CS 235', 'CHIN 382', 'JPN 232', 'ARTH 240', 'KOR 232', 'CHIN 243', 'KOR 209H', 'FREN 324', 'MATH 370', 'MATH 313', 'MATH 306', 'MATH 223', 'STAT 318', 'MATH 207Y', 'MATH 250', 'MATH 313', 'MATH 313', 'ARTS 365', 'ARTS 350', 'ARTS 207', 'ARTS 165', 'SOC 220', 'PEAC 240', 'REL 233', 'JWST 201']
c = ['AFR 204', 'AFR 235', 'ARTS 222', 'SOC 314', 'ARTH 240', 'ARTH 318', 'POL1 333', 'CAMS 234', 'CAMS 238', 'CAMS 228', 'CAMS 234', 'SPAN 268', 'CAMS 228', 'FREN 300', 'ARTS 208', 'CAMS 219', 'BISC 198', 'CS 230', 'BISC 198', 'CS 232', 'QR 260', 'GER 350', 'HIST 376', 'CAMS 201', 'MAS 222', 'CAMS 233', 'MUS 275', 'SPAN 269', 'WGST 214', 'WGST 360']
d = ['MUS 250', 'CS 230', 'AMST 152', 'GER 389', 'STAT 318', 'CS 343', 'CS 304', 'MUS 309', 'GER 225', 'GER 386', 'AMST 215', 'JPN 251', 'GER 350H', 'PHYS 350H', 'GER 286', 'SWA 203', 'ENG 342', 'FREN 300', 'GER 250H', 'AFR 212', 'ENG 234', 'GER 229', 'CHIN 204', 'THST 251', 'CS 315', 'PHYS 323H', 'CHIN 320', 'GER 239', 'HIST 204', 'GER 370']
e = ['PHYS 355', 'AMST 231', 'ASTR 303', 'LING 246', 'RUSS 386H', 'PSYC 216', 'CS 235', 'AFR 303', 'CS 111', 'AFR 211', 'ASTR 311', 'AFR 380', 'AFR 306', 'PHYS 360', 'EALC 225', 'PHYS 302', 'AFR 206', 'ENG 210', 'SWA 201', 'CS 232', 'ARTH 255', 'AFR 204', 'HIST 213', 'JPN 352', 'AFR 318', 'CS 230', 'CS 220']
f = ['SPAN 287', 'MATH 302', 'MATH 340', 'LING 238', 'CHEM 350', 'AFR 302', 'HIST 268', 'HIST 369', 'PHYS 350', 'SWA 203', 'PHYS 355', 'AFR 380', 'PHIL 207', 'MATH 307', 'SPAN 250', 'AFR 341', 'MATH 313', 'MATH 365', 'MATH 325', 'MATH 350', 'SPAN 291', 'MATH 310', 'SPAN 293', 'PSYC 216', 'PHYS 365', 'MATH 215', 'PHYS 305', 'PHYS 370']
g = ['AFR 207', 'ENG 213', 'ECON 327', 'REL 345', 'JWST 209', 'CAMS 241', 'CAMS 366', 'ENG 349', 'JWST 245', 'JWST 270', 'MUS 336', 'JWST 201', 'CAMS 235', 'MAS 250H', 'WRIT 120', 'REL 227', 'JWST 345', 'CAMS 250', 'CHEM 350H', 'ENG 211', 'FREN 330', 'JWST 233', 'SAS 302', 'ENG 222', 'JWST 350H']
h = ['ITAS 263', 'REL 318', 'ITAS 202', 'ENG 268', 'ITAS 210', 'SAS 303', 'REL 225', 'ITAS 261', 'ENG 208', 'ENG 260', 'ITAS 271', 'ITAS 270', 'FREN 303', 'HIST 260', 'PHIL 245', 'ITAS 203', 'FREN 205', 'SAS 350', 'ENG 311', 'SAS 302', 'ITAS 274', 'FREN 241', 'PEAC 215', 'POL4 340', 'ENG 210', 'SAS 242', 'PEAC 360', 'FREN 207']
i = ['PEAC 225', 'AFR 204', 'PEAC 243', 'ENG 295', 'PEAC 370', 'THST 360', 'POL1 210', 'AFR 350', 'PHYS 350H', 'PEAC 290', 'PEAC 210', 'PHYS 304', 'PEAC 240', 'AFR 206', 'PEAC 206', 'PHYS 370', 'PEAC 388', 'PEAC 205', 'AFR 216', 'ECON 334', 'WGST 250H', 'PHYS 355', 'GER 250H', 'HIST 273', 'PEAC 235', 'AFR 215', 'PEAC 224']
j = ['CS 112', 'POL3 351', 'PEAC 206', 'HIST 221', 'SOC 312', 'PEAC 261', 'MATH 313', 'HIST 280', 'POL1 210', 'PEAC 264', 'PSYC 345', 'ECON 312', 'MATH 314', 'ECON 214', 'PSYC 217', 'PEAC 201', 'CLSC 316', 'PSYC 301', 'STAT 228', 'PSYC 216', 'PEAC 207/', 'POL2 362', 'POL1 333', 'LAT 308', 'PSYC 215', 'WGST 215', 'PSYC 315R']
k = ['ECON 101','ECON 203','ECON 222','EDUC 226','ECON 233','ECON 314','ECON 318','ECON 320','CS 242','CS 301','CS 304','CS 342','FREN 101','FREN 102','FREN 201','FREN 202','HIST 245','HIST 220','JPN 290','MATH 205','MATH 206','MATH 223','MATH 225','NEUR 100','PHIL 215','POL1 200','WRIT 166']

#cs(kat)
#econ(kat)
#cs(emily)
#econ(emily)
#chem(kat)
#cs(julie)

masterCheck(kat)