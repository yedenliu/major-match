import pandas as pd
import csv

majorReqs = '/students/kswint/major-match/DDL/majorReqsDF.tsv'
coursesToMajors = '/students/kswint/major-match/DDL/coursesToMajors.tsv'

def grabCourses(dept):
    allCourses = []
    with open(majorReqs, "r") as courses:
        for row in courses:
            rho = row.split('\t')
            if (dept).__eq__(rho[0]):
                allCourses = list(set(rho[1:]))
                allCourses.sort()
    return(allCourses)

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

def courseLevelUntangler(electiveList, level):
    levelElectives = []
    for elective in electiveList:
        courseNum = int(elective.split(" ")[1][0])
        if courseNum == level:
            levelElectives.append(elective)
    return(levelElectives)

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

kat = ['ARTH 267','ES 267','CS 111','CS 220','CS 230','CS 231','CS 235','CS 240','CS 242','CS 301','CS 304','CS 342','FREN 101','FREN 102','FREN 201','FREN 202','HIST 245','HIST 220','JPN 290','MATH 205','MATH 206','MATH 223','MATH 225','NEUR 100','PHIL 215','POL1 200','WRIT 166']
emily = ['ECON 101','ECON 203','ECON 222','EDUC 226','ECON 233','ECON 314','ECON 318','ECON 320','CS 242','CS 301','CS 304','CS 342','FREN 101','FREN 102','FREN 201','FREN 202','HIST 245','HIST 220','JPN 290','MATH 205','MATH 206','MATH 223','MATH 225','NEUR 100','PHIL 215','POL1 200','WRIT 166']
julie = ['MATH 205', 'POL 123', 'WRIT 187', 'MATH 206', 'STAT 218', 'SPAN 241', 'CS 111', 'MATH 305', 'PHIL 216', 'CS 230', 'SPAN 253', 'MATH 349', 'MATH 225', 'WGST 218', 'CS 232', 'STAT 260', 'MATH 220', 'MATH 302', 'MATH 215', 'MATH 340', 'PHYS 107', 'STAT 309', 'MATH 322', 'PHYS 313', 'PORT 103', 'MATH 309']

#cs(kat)
#econ(kat)
#cs(emily)
#econ(emily)
#chem(kat)
cs(julie)
