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

def suggestComplete(taken, neededNum, options, core):
    if len(taken) < neededNum:
        for course in taken:
            if course in options:
                options.remove(course)
        if core:
            print('\n\tYou must take these course(s):')
            for course in options:
                print('\t\t', course)
        elif not core:
            print('\n\tYou should select', neededNum, 'course(s) from the following list:')
            for course in options:
                print('\t\t', course)

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
        suggestComplete(introsTaken, int(len(introductory) - len(introsTaken)), introductory, True)
        suggestComplete(mathTaken, int(len(math) - len(mathTaken)), math, True)
        suggestComplete(coresTaken, int(len(core) - len(coresTaken)), core, True)
        suggestComplete(threesTaken, int(2 - numThrees), threes, False)
        suggestComplete(electivesTaken, int(2 - numElectives), electives, False)

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
        suggestComplete(taken, coreNeeded, core, True)
        suggestComplete(taken, threesNeeded, threes, False)
        suggestComplete(taken, electivesNeeded, electives, False)

kat = ['ARTH 267','ES 267','CS 111','CS 220','CS 230','CS 231','CS 235','CS 240','CS 242','CS 301','CS 304','CS 342','FREN 101','FREN 102','FREN 201','FREN 202','HIST 245','HIST 220','JPN 290','MATH 205','MATH 206','MATH 223','MATH 225','NEUR 100','PHIL 215','POL1 200','WRIT 166']
emily = ['ECON 101','ECON 203','ECON 222','EDUC 226','ECON 233','ECON 314','ECON 318','ECON 320','CS 242','CS 301','CS 304','CS 342','FREN 101','FREN 102','FREN 201','FREN 202','HIST 245','HIST 220','JPN 290','MATH 205','MATH 206','MATH 223','MATH 225','NEUR 100','PHIL 215','POL1 200','WRIT 166']

#cs(kat)
#econ(kat)
cs(emily)
#econ(emily)