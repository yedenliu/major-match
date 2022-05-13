from os import major
from pkgutil import iter_importers
from unittest.util import unorderable_list_difference
import pandas as pd
import csv

majorReqs = '/students/kswint/major-match/beta/DDL/majorReqsDF.tsv'
coursesToMajors = '/students/kswint/major-match/beta/DDL/coursesToMajors.tsv'

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

''' Takes a major name as a string, and then gets all the courses that count towards that major.'''
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
the courses that count as elective courses for that major.

For example, the CS major requires that students take "two 300 level CS courses, 
and at least two additional computer science course at the 200 or 300 level." To avoid
having CS 230, CS 231, CS 235, or CS 240 count for the elective instead of the core,
this function will "remove" those courses from the list of 200-level CS courses so
the remaining courses are the ones that could fulfill that elective requirement.'''
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
                pass
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
        if count <= needed:
            print(course, 'fulfills', count, 'of', needed, reqName, 'requirements')
            count += 1
    if needed <= has:
        print("You've fulfilled all", reqName, "requirements for the major!\n")
    else:
        print('You need', (needed - has), 'more course(s) to fulfill all', reqName, "requirements for the major!\n")

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

def matchBandaid(userInput, majorCourses):
    has = 0
    for course in userInput:
        if course in majorCourses:
            has += 1
    return(has)

def africanaStudiesAfrica(userInput):
    dept = 'Africana Studies - Africa Concentration'
    majorCourses = grabCourses(dept)
    
    needed = 9
    has = matchBandaid(userInput, majorCourses)
    
    print(dept + ': ' + str(has) + '/' + str(needed))

def africanaStudiesGeneral(userInput):
    dept = 'Africana Studies - General Africana Studies Concentration'
    majorCourses = grabCourses(dept)
    
    needed = 9
    has = matchBandaid(userInput, majorCourses)
    
    print(dept + ': ' + str(has) + '/' + str(needed))

def africanaStudiesCaribbeanLatinAmerica(userInput):
    dept = 'Africana Studies - The Caribbean and Latin America Concentration'
    majorCourses = grabCourses(dept)
    
    needed = 9
    has = matchBandaid(userInput, majorCourses)
    
    print(dept + ': ' + str(has) + '/' + str(needed))

def africanaStudiesUnitedStates(userInput):
    dept = 'Africana Studies - United States Concentration'
    majorCourses = grabCourses(dept)
    
    needed = 9
    has = matchBandaid(userInput, majorCourses)
    
    print(dept + ': ' + str(has) + '/' + str(needed))

def americanStudies(userInput):
    dept = 'American Studies'
    majorCourses = grabCourses(dept)
    
    needed = 9
    has = matchBandaid(userInput, majorCourses)
    
    print(dept + ': ' + str(has) + '/' + str(needed))

def anthropology(userInput):
    dept = 'Anthropology'
    majorCourses = grabCourses(dept)
    
    needed = 9
    has = matchBandaid(userInput, majorCourses)
    
    print(dept + ': ' + str(has) + '/' + str(needed))

def architecture(userInput):
    dept = 'Architecture'
    majorCourses = grabCourses(dept)
    
    needed = 11
    has = matchBandaid(userInput, majorCourses)
    
    print(dept + ': ' + str(has) + '/' + str(needed))

def artHistory(userInput):
    dept = 'Art History'
    majorCourses = grabCourses(dept)
    
    needed = 10
    has = matchBandaid(userInput, majorCourses)
    
    print(dept + ': ' + str(has) + '/' + str(needed))

def astronomy(userInput):
    dept = 'Astronomy'
    majorCourses = grabCourses(dept)
    
    needed = 12
    has = matchBandaid(userInput, majorCourses)
    
    print(dept + ': ' + str(has) + '/' + str(needed))

def astrophysics(userInput):
    dept = 'Astrophysics'
    majorCourses = grabCourses(dept)
    
    needed = 15
    has = matchBandaid(userInput, majorCourses)
    
    print(dept + ': ' + str(has) + '/' + str(needed))

def biochem(userInput):
    dept = 'Biochemistry'
    majorCourses = grabCourses(dept)
    
    needed = 13
    has = matchBandaid(userInput, majorCourses)
    
    print(dept + ': ' + str(has) + '/' + str(needed))

def biology(userInput):
    dept = 'Biological Sciences'
    majorCourses = grabCourses(dept)
    
    needed = 11
    has = matchBandaid(userInput, majorCourses)
    
    print(dept + ': ' + str(has) + '/' + str(needed))

def chemicalPhysics(userInput):
    dept = 'Chemical Physics'
    majorCourses = grabCourses(dept)
    
    needed = 13
    has = matchBandaid(userInput, majorCourses)
    
    print(dept + ': ' + str(has) + '/' + str(needed))

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

    # if has != needed:
    #     print('If you would like to complete the Chemistry major...')
    #     suggestComplete(core1Taken, coreNeeded, core1, True, 1)
    #     suggestComplete(core2Taken, coreNeeded, core2, True, 2)
    #     suggestComplete(core3Taken, 1, core3, True, 3)
    #     print('\tRegardless of the core path...')
    #     suggestComplete(core4Taken, 3, core4, True, 0)
    #     suggestComplete(threesTaken, 1, threes, False, 0)
    #     suggestComplete(flexChemTaken, 3, flexChem, False, 0)
    #     suggestComplete(flexMathTaken, 1, flexMath, False, 0)
    #     suggestComplete(flexPhysTaken, 1, flexPhys, False, 0)

def camsPre2020(userInput):
    dept = 'Cinema and Media Studies - entering in Fall 2020 and before'
    majorCourses = grabCourses(dept)
    
    needed = 10
    has = matchBandaid(userInput, majorCourses)
    
    print(dept + ': ' + str(has) + '/' + str(needed))

def camsCurrent(userInput):
    dept = 'Cinema and Media Studies - entering in Spring 2021 and after'
    majorCourses = grabCourses(dept)
    
    needed = 10
    has = matchBandaid(userInput, majorCourses)
    
    print(dept + ': ' + str(has) + '/' + str(needed))

def classicalCivilization(userInput):
    dept = 'Classical Civilization'
    majorCourses = grabCourses(dept)
    
    needed = 9
    has = matchBandaid(userInput, majorCourses)
    
    print(dept + ': ' + str(has) + '/' + str(needed))

def cogSciCS(userInput):
    dept = 'Cognitive and Linguistic Sciences - Computer Science Concentration'
    majorCourses = grabCourses(dept)
    
    needed = 9
    has = matchBandaid(userInput, majorCourses)
    
    print(dept + ': ' + str(has) + '/' + str(needed))

def cogSciLing(userInput):
    dept = 'Cognitive and Linguistic Sciences - Linguistics Concentration'
    majorCourses = grabCourses(dept)
    
    needed = 9
    has = matchBandaid(userInput, majorCourses)
    
    print(dept + ': ' + str(has) + '/' + str(needed))

def cogSciPhil(userInput):
    dept = 'Cognitive and Linguistic Sciences - Philosophy Concentration'
    majorCourses = grabCourses(dept)
    
    needed = 9
    has = matchBandaid(userInput, majorCourses)
    
    print(dept + ': ' + str(has) + '/' + str(needed))

def cogSciPsych(userInput):
    dept = 'Cognitive and Linguistic Sciences - Psychology Concentration'
    majorCourses = grabCourses(dept)
    
    needed = 9
    has = matchBandaid(userInput, majorCourses)
    
    print(dept + ': ' + str(has) + '/' + str(needed))

def compLit(userInput):
    dept = 'Comparative Literary Studies'
    majorCourses = grabCourses(dept)
    
    needed = 9
    has = matchBandaid(userInput, majorCourses)
    
    print(dept + ': ' + str(has) + '/' + str(needed))

# TODO electives don't seem to be working, 342 and 304 aren't counting
# TODO suggestComplete is buggy here too
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

    # taken = coresTaken + threesTaken + electivesTaken
    # if has != needed: 
    #     print('If you would like to complete the Computer Science major, you need to take:\n')
    #     suggestComplete(introsTaken, int(len(introductory) - len(introsTaken)), introductory, True, 0)
    #     suggestComplete(mathTaken, int(len(math) - len(mathTaken)), math, True, 0)
    #     suggestComplete(coresTaken, int(len(core) - len(coresTaken)), core, True, 0)
    #     suggestComplete(threesTaken, int(2 - numThrees), threes, False, 0)
    #     suggestComplete(electivesTaken, int(2 - numElectives), electives, False, 0)

def dataScience(userInput):
    dept = 'Data Science'
    majorCourses = grabCourses(dept)
    
    needed = 12
    has = matchBandaid(userInput, majorCourses)
    
    print(dept + ': ' + str(has) + '/' + str(needed))

def eastAsianLangCult(userInput):
    dept = 'East Asian Languages and Cultures'
    majorCourses = grabCourses(dept)
    
    needed = 8
    has = matchBandaid(userInput, majorCourses)
    
    print(dept + ': ' + str(has) + '/' + str(needed))

def eastAsianStudies(userInput):
    dept = 'East Asian Studies'
    majorCourses = grabCourses(dept)
    
    needed = 10
    has = matchBandaid(userInput, majorCourses)
    
    print(dept + ': ' + str(has) + '/' + str(needed))

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

    # taken = coresTaken + threesTaken + electivesTaken
    # if has != needed:
    #     print('If you would like to complete the Economics major, you need to take:\n')
    #     suggestComplete(taken, coreNeeded, core, True, 0)
    #     suggestComplete(taken, threesNeeded, threes, False, 0)
    #     suggestComplete(taken, electivesNeeded, electives, False, 0)

def educationStudies(userInput):
    dept = 'Education Studies'
    majorCourses = grabCourses(dept)
    
    needed = 9
    has = matchBandaid(userInput, majorCourses)
    
    print(dept + ': ' + str(has) + '/' + str(needed))

def english(userInput):
    dept = 'English'
    majorCourses = grabCourses(dept)
    
    needed = 10
    has = matchBandaid(userInput, majorCourses)
    
    print(dept + ': ' + str(has) + '/' + str(needed))

def englishCreativeWriting(userInput):
    dept = 'English and Creative Writing'
    majorCourses = grabCourses(dept)
    
    needed = 12
    has = matchBandaid(userInput, majorCourses)
    
    print(dept + ': ' + str(has) + '/' + str(needed))

def environmentalStudies(userInput):
    dept = 'Environmental Studies'
    majorCourses = grabCourses(dept)
    
    needed = 10
    has = matchBandaid(userInput, majorCourses)
    
    print(dept + ': ' + str(has) + '/' + str(needed))

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

    # if has != needed: 
    #     print('If you would like to complete the French and Francophone Studies major, you need to take:\n')
    #     suggestComplete(coresTaken, int(len(core) - len(coresTaken)), core, False, 0)
    #     suggestComplete(flexLangTaken, int(len(flexLang) - len(flexLangTaken)), flexLang, False, 0)
    #     suggestComplete(flexCultureTaken, int(len(flexCulture) - len(flexCultureTaken)), flexCulture, False, 0)
    #     suggestComplete(flexLitTaken, int(len(flexLitTaken) - len(flexLit)), flexLit, False, 0)
    #     suggestComplete(threesTaken, int(2 - numThrees), threes, False, 0)

def frenchCulturalStudies(userInput):
    dept = 'French Cultural Studies'
    majorCourses = grabCourses(dept)
    
    needed = 8
    has = matchBandaid(userInput, majorCourses)
    
    print(dept + ': ' + str(has) + '/' + str(needed))

def geosciences(userInput):
    dept = 'Geosciences'
    majorCourses = grabCourses(dept)
    
    needed = 12
    has = matchBandaid(userInput, majorCourses)
    
    print(dept + ': ' + str(has) + '/' + str(needed))

def german(userInput):
    dept = 'German Studies'
    majorCourses = grabCourses(dept)
    
    needed = 9                                          # they dont actually specify how many are needed
    has = matchBandaid(userInput, majorCourses)
    
    print(dept + ': ' + str(has) + '/' + str(needed))

def history(userInput):
    print('Checking your requirements against the History major...')
    needed = 9
    has = 0

    flexAfrChiJapLatAmMidEaSouAs = ['HIST 207','LAST 207','HIST 211','LAST 211','HIST 212','HIST 215','HIST 218','HIST 263','PEAC 224','HIST 264','HIST 265','HIST 266','SAS 266','HIST 268','HIST 270','HIST 272','HIST 273','HIST 275','HIST 276','HIST 277','HIST 278','HIST 280','HIST 284','HIST 285','REL 266','HIST 293','MES 293','HIST 359','HIST 364','MES 364','HIST 365','HIST 366','MES 366','HIST 367','SAS 367','HIST 369','MES 369','HIST 371','HIST 376','HIST 377','HIST 383']
    flexEurUniStRus = ['HIST 201','HIST 203','HIST 204','HIST 205','HIST 212','HIST 213','HIST 214','HIST 220','HIST 221','ENG 221','HIST 222','HIST 228','HIST 229','HIST 230','HIST 231','HIST 232','HIST 233','HIST 234','HIST 240','HIST 242','HIST 243','HIST 244','HIST 245','HIST 246','HIST 247','HIST 248','HIST 249','HIST 251','HIST 252','HIST 253','HIST 254','HIST 256','HIST 260','HIST 261','PEAC 261','HIST 262','HIST 267','HIST 277','HIST 279','ES 299','HIST 299','HIST 302','HIST 311','HIST 312','HIST 314','HIST 319','HIST 320','HIST 321','HIST 330','HIST 334','HIST 340','HIST 341','HIST 352','HIST 354','HIST 358','HIST 359','HIST 375']
    flexPreMod = ['HIST 208','HIST 211','LAST 211','HIST 213','HIST 214','HIST 221','ENG 221','HIST 222','HIST 228','HIST 229','HIST 230','HIST 231','HIST 232','HIST 234','HIST 246','HIST 279','HIST 325','HIST 329','HIST 330','HIST 375','HIST 379']

    allCourses = grabCourses('History')

    twos = courseLevelUntangler(allCourses,2) 
    threes = courseLevelUntangler(allCourses,3)
    electives = twos + threes

    numThrees = 0

    flexAfrChiJapLatAmMidEaSouAsTaken = []
    flexEurUniStRusTaken = []
    flexPreModTaken = []
    threesTaken = []
    electivesTaken = []

    for course in userInput:
        if (course in threes) and (numThrees < 2):
            threesTaken.append(course)
            has += 1
            numThrees += 1
        elif (course in flexAfrChiJapLatAmMidEaSouAs) and (len(flexAfrChiJapLatAmMidEaSouAsTaken) < 1):
            flexAfrChiJapLatAmMidEaSouAsTaken.append(course)
            has += 1
        elif (course in flexEurUniStRus) and (len(flexEurUniStRusTaken) < 1):
            flexEurUniStRusTaken.append(course)
            has += 1
        elif (course in flexPreMod) and (len(flexPreModTaken) < 1):
            flexPreModTaken.append(course)
            has += 1
        elif course in electives:
            electivesTaken.append(course)
            has += 1

    compareUserAndReqs(flexAfrChiJapLatAmMidEaSouAsTaken, flexAfrChiJapLatAmMidEaSouAs, 'history of Africa, China, Japan, Latin America, the Middle East, or South Asia',1)
    compareUserAndReqs(flexEurUniStRusTaken, flexEurUniStRus, 'history of Europe, the United States, or Russia',1)
    compareUserAndReqs(flexPreModTaken, flexPreMod, 'premodern history', 1)
    compareUserAndReqs(threesTaken, threes, '300-level elective', 2)
    compareUserAndReqs(electivesTaken, electives, '200 or 300-level elective', 4)

    print('You have completed', has, '/', needed, 'requirements for the History major.')

    remainingElectivesNeeded = 6 - len(threesTaken) - len(electivesTaken)

    # if has != needed: 
    #     print('If you would like to complete the History major, you need to take:\n')
    #     suggestComplete(flexAfrChiJapLatAmMidEaSouAsTaken, int(1 - len(flexAfrChiJapLatAmMidEaSouAsTaken)), flexAfrChiJapLatAmMidEaSouAs, False, 0)
    #     suggestComplete(flexEurUniStRusTaken, int(1 - len(flexEurUniStRusTaken)), flexEurUniStRus, False, 0)
    #     suggestComplete(flexPreModTaken, int(1 - len(flexPreModTaken)), flexPreMod, False, 0)
    #     suggestComplete(threesTaken, int(2 - numThrees), threes, False, 0)
    #     suggestComplete(electivesTaken, remainingElectivesNeeded, electives, False, 0)

def internationalRelationsEcon(userInput):
    dept = 'International Relations - Economics'
    majorCourses = grabCourses(dept)
    
    needed = 14
    has = matchBandaid(userInput, majorCourses)
    
    print(dept + ': ' + str(has) + '/' + str(needed))

def internationalRelationsHistory(userInput):
    dept = 'International Relations - History'
    majorCourses = grabCourses(dept)
    
    needed = 14
    has = matchBandaid(userInput, majorCourses)
    
    print(dept + ': ' + str(has) + '/' + str(needed))

def internationalRelationsPoliSci(userInput):
    dept = 'International Relations - Political Science'
    majorCourses = grabCourses(dept)
    
    needed = 14
    has = matchBandaid(userInput, majorCourses)
    
    print(dept + ': ' + str(has) + '/' + str(needed))

def italian(userInput):
    dept = 'Italian Studies'
    majorCourses = grabCourses(dept)
    
    needed = 9
    has = matchBandaid(userInput, majorCourses)
    
    print(dept + ': ' + str(has) + '/' + str(needed))

def jewishStudies(userInput):
    dept = 'Jewish Studies'
    majorCourses = grabCourses(dept)
    
    needed = 9
    has = matchBandaid(userInput, majorCourses)
    
    print(dept + ': ' + str(has) + '/' + str(needed))

def latinAmericanStudies(userInput):
    dept = 'Latin American Studies'
    majorCourses = grabCourses(dept)
    
    needed = 9
    has = matchBandaid(userInput, majorCourses)
    
    print(dept + ': ' + str(has) + '/' + str(needed))

def math(userInput):
    print('Checking your requirements against the Mathematics major...')
    needed = 10
    has = 0

    introductoryOne = ['MATH 115','MATH 115Z']
    introductoryTwo = ['MATH 116','MATH 120']
    core = ['MATH 205','MATH 206','MATH 302','MATH 305']

    inflexible = introductoryOne + introductoryTwo + core

    allCourses = grabCourses('Mathematics')
    electives = findElectives(inflexible, allCourses)

    threes = courseLevelUntangler(electives,3)

    numThrees = 0

    introsOneTaken = []
    introsTwoTaken = []
    coresTaken = []
    threesTaken = []
    electivesTaken = []

    for course in userInput:
        if course in introductoryOne:
            introsOneTaken.append(course)
            has += 1
        elif course in introductoryTwo:
            introsTwoTaken.append(course)
            has += 1
        elif course in core:
            coresTaken.append(course)
            has += 1
        elif (course in threes) and (numThrees < 2):
            threesTaken.append(course)
            has += 1
            numThrees += 1
        elif course in electives:
            electivesTaken.append(course)
            has += 1

    compareUserAndReqs(introsOneTaken, introductoryOne, 'introductory',1)
    compareUserAndReqs(introsTwoTaken, introductoryTwo, 'introductory',1)
    compareUserAndReqs(coresTaken, core, 'core',4)
    compareUserAndReqs(threesTaken, threes, '300-level elective', 2)
    compareUserAndReqs(electivesTaken, electives, '200 or 300-level elective', 2)

    print('You have completed', has, '/', needed, 'requirements for the Mathematics major.')

    if has != needed: 
        print('If you would like to complete the Mathematics major, you need to take:\n')
        suggestComplete(introsOneTaken, int(1 - len(introsOneTaken)), introductoryOne, False, 0)
        suggestComplete(introsTwoTaken, int(1 - len(introsTwoTaken)), introductoryTwo, False, 0)
        suggestComplete(coresTaken, int(len(core) - len(coresTaken)), core, True, 0)
        suggestComplete(threesTaken, int(2 - numThrees), threes, False, 0)
        suggestComplete(electivesTaken, int(2 - len(electivesTaken)), electives, False, 0)

def mediaArtsSciences(userInput):
    dept = 'Media Arts and Sciences'
    majorCourses = grabCourses(dept)
    
    needed = 12
    has = matchBandaid(userInput, majorCourses)
    
    print(dept + ': ' + str(has) + '/' + str(needed))

def medievalRenaissanceStudies(userInput):
    dept = 'Medieval Renaissance Studies'
    majorCourses = grabCourses(dept)
    
    needed = 9
    has = matchBandaid(userInput, majorCourses)
    
    print(dept + ': ' + str(has) + '/' + str(needed))

def middleEasternStudies(userInput):
    dept = 'Middle Eastern Studies'
    majorCourses = grabCourses(dept)
    
    needed = 9
    has = matchBandaid(userInput, majorCourses)
    
    print(dept + ': ' + str(has) + '/' + str(needed))

def music(userInput):
    dept = 'Music'
    majorCourses = grabCourses(dept)
    
    needed = 10
    has = matchBandaid(userInput, majorCourses)
    
    print(dept + ': ' + str(has) + '/' + str(needed))

def neuroscience(userInput):
    dept = 'Neuroscience'
    majorCourses = grabCourses(dept)
    
    needed = 11
    has = matchBandaid(userInput, majorCourses)
    
    print(dept + ': ' + str(has) + '/' + str(needed))

def peaceJusticeStudies(userInput):
    dept = 'Peace and Justice Studies'
    majorCourses = grabCourses(dept)
    
    needed = 10
    has = matchBandaid(userInput, majorCourses)
    
    print(dept + ': ' + str(has) + '/' + str(needed))

''' Let's get one thing straight: this helper function is an absolute dumpster fire. I am embarassed for
anyone to see this. It's genuinely atrocious. I'm not even sure if it will ever get to the recursive function,
but I'm leaving it in because I can't think and removing it would haunt me.

This helper function is *supposed* to look at the number of courses a philosophy student has taken in 
subfield B and the number of courses they have taken in subfield C, and then allocate further courses in a clever
way. Philosophy majors must take two courses within subfield B and two courses within subfield C.Let me paint 
a picture:
        Kat is an up-and-coming philosophy student who is passionate about metaphysics, and has taken all of her
        philosophy classes within subfield C. This may not be an issue, since lots of classes in subfield C also
        are in subfield B. First, philosophy(userInput) will look at all the classes she's taken and will find the
        ones that are *only* in subfield B or are *only* in subfield C and will allocate them appropriately. It will
        then say "gee, the rest of the classes she's taken could cover either the subfield B or the subfield C requirement!
        how do i sort that out?" and will call subfieldSort(). subfieldSort() will gracefully take the burden from 
        philosophy(). It sees that Kat has taken enough classes for her subfield C requirement and only needs to
        fill her subfield B requirement. No problem. It goes through the list of courses she's taken, and grabs however many
        she needs (in this case, 2) to fulfill her subfield B requirement. Once it's done, it lets philosophy() know
        that it doesn't need to worry about how it allocates the rest of the classes to each subfield since Kat has
        already fulfilled the requirement.'''
# TODO Idk. i think that i'm still not allocating Bs correctly. IDK
def subfieldSort(remainingBandC, numBs, numCs, bTaken, cTaken):
    # these are designated by the philosophy dept
    subfieldB = ['PHIL 102','PHIL 105','PHIL 106','PHIL 108','PHIL 111','PHIL 115','PHIL 203','PHIL 205','PHIL 213','PHIL 220','PHIL 222','PHIL 226','PHIL 228','PHIL 229','PHIL 231','PHIL 233','PHIL 234','PHIL 236','PHIL 249','PHIL 300','PHIL 301','PHIL 303','PHIL 304','PHIL 306','PHIL 307','PHIL 310','PHIL 316','PHIL 317','PHIL 323','PHIL 330','PHIL 331','PHIL 333','PHIL 338','PHIL 340','PHIL 341','PHIL 342','PHIL 345','PHIL 366']
    subfieldC = ['PHIL 103','PHIL 112','PHIL 200','PHIL 207','PHIL 215','PHIL 216','PHIL 218','PHIL 220','PHIL 229','PHIL 245','PHIL 300','PHIL 306','PHIL 310','PHIL 311','PHIL 317','PHIL 319','PHIL 323','PHIL 325','PHIL 331','PHIL 333','PHIL 341','PHIL 345']
    
    inCourses = remainingBandC              # I get errors when I just try and use remainingBandC
    b = numBs                               # I get errors when I just try and use numBs
    c = numCs                               # I get errors when I just try and use numCs

    addBs = []                              # the first of many unnecessary new lists
    addCs = []                              # the second of many unnecessary new lists

    '''Potential flaws in my logic begin here. This will always "fill up" subfield B before it fills subfield C. I feel
    like this is an issue, but it might not be. A few scenarios:
        (a) Kat has taken 2 unique subfield B courses and 1 unique subfield C course. This is fine, since the
            missing subfield C course will be filled in with a course that is in both subfield B and subfield C.
        (b) Kat has taken 1 unique subfield B course and 2 unique subfield C courses. This is fine, since the
            missing subfield B course will be filled in with a course that is in both subfield B and subfield C.
        (c) Kat has taken <1 unique subfield B course and <1 unique subfield C course. This is fine, since Kat
            needs to fill in both subfield B and subfield C. So even if she only has one additional course that
            could fulfill either subfield, it doesn't really change her actual major completion.
            
    I might be wrong.'''
    for course in inCourses:
        if (course in subfieldB) and (b < 2):
            b += 1
            addBs.append(course)
            inCourses.remove(course)

    for course in inCourses:
        if (course in subfieldC) and (c < 2): 
            c += 1
            addCs.append(course)
            inCourses.remove(course)

    addBs = addBs + bTaken          # the unique subfield B courses given by philosophy() + our new allocated subfield B courses
    addCs = addCs + cTaken          # the unique subfield C courses given by philosophy() + our new allocated subfield C courses

    #recursedB = []                  # idk. I felt like I needed new lists here.
    #recursedC = []

    '''I don't think this recursive call will ever be reached, since the for loops will continue populating until
    both categories have two courses. Logically, I should remove this, but emotionally I cannot.'''
    #if (b < 2) or (c < 2):
    #    newBandC = subfieldSort(inCourses, b, c, addBs, addCs)
    #    recursedB = newBandC[0]
    #    recursedC = newBandC[1]

    outBs = addBs #+ recursedB
    outCs = addCs #+ recursedC

    output = [outBs, outCs]

    return(output)   

# TODO figure out how to move courses... like phil 200 should be showing up as an elective
def philosophy(userInput):
    print('Checking your requirements against the Philosophy major...')
    needed = 9
    has = 0
    hasList = []

    # these are designated by the philosophy dept
    core = ['PHIL 201','PHIL 221']
    subfieldA = ['PHIL 102','PHIL 200','PHIL 231','PHIL 300','PHIL 301','PHIL 305','PHIL 306','PHIL 307','PHIL 310']
    subfieldB = ['PHIL 102','PHIL 105','PHIL 106','PHIL 108','PHIL 111','PHIL 115','PHIL 203','PHIL 205','PHIL 213','PHIL 220','PHIL 222','PHIL 226','PHIL 228','PHIL 229','PHIL 231','PHIL 233','PHIL 234','PHIL 236','PHIL 249','PHIL 300','PHIL 301','PHIL 303','PHIL 304','PHIL 306','PHIL 307','PHIL 310','PHIL 316','PHIL 317','PHIL 323','PHIL 330','PHIL 331','PHIL 333','PHIL 338','PHIL 340','PHIL 341','PHIL 342','PHIL 345','PHIL 366']
    subfieldC = ['PHIL 103','PHIL 112','PHIL 200','PHIL 207','PHIL 215','PHIL 216','PHIL 218','PHIL 220','PHIL 229','PHIL 245','PHIL 300','PHIL 306','PHIL 310','PHIL 311','PHIL 317','PHIL 319','PHIL 323','PHIL 325','PHIL 331','PHIL 333','PHIL 341','PHIL 345']

    # these are the courses in each subfield that are unique to that subfield
    subfieldAUnique = ['PHIL 201','PHIL 221','PHIL 305']
    subfieldBUnique = ['PHIL 105', 'PHIL 106', 'PHIL 108', 'PHIL 111', 'PHIL 115', 'PHIL 203', 'PHIL 205', 'PHIL 213', 'PHIL 222', 'PHIL 226', 'PHIL 228', 'PHIL 233', 'PHIL 234', 'PHIL 236', 'PHIL 249', 'PHIL 303', 'PHIL 304', 'PHIL 316', 'PHIL 330', 'PHIL 338', 'PHIL 340', 'PHIL 342', 'PHIL 366']
    subfieldCUnique = ['PHIL 103', 'PHIL 112', 'PHIL 207', 'PHIL 215', 'PHIL 216', 'PHIL 218', 'PHIL 245', 'PHIL 311', 'PHIL 319', 'PHIL 325']
    
    # these are the courses that belong to multiple subfields
    multiSubfield = ['EDUC 102', 'PHIL 102', 'PHIL 200', 'PHIL 22', 'PHIL 220', 'PHIL 229', 'PHIL 231', 'PHIL 300', 'PHIL 301', 'PHIL 306', 'PHIL 307', 'PHIL 310', 'PHIL 317', 'PHIL 323', 'PHIL 331', 'PHIL 333', 'PHIL 341', 'PHIL 345', 'WRIT 114']

    allCourses = grabCourses('Philosophy')
    extras = findElectives(core, allCourses)
    threes = courseLevelUntangler(allCourses,3)

    numThrees = 0

    coreTaken = []
    subfieldATaken = []
    subfieldBTaken = []
    subfieldCTaken = []
    threesTaken = []
    extraTaken = []
    
    '''Philosophy majors must take 300-level philosophy courses within multiple subfields. This little
    Boolean dance is how I'm checking it. If it's super efficient and impressive, praise my for my 
    ingenuity. Otherwise, I will be honest and say that I am coding like an infant right now and that
    this was the simplest way I could figure it out. Never tell Ben Wood, he would be so disappointed that
    I didn't retain more from 240'''
    multiSubs = False
    threeA = False
    threeB = False
    threeC = False
    for course in userInput:
        if course in threes:
            if (course in subfieldA) and (threeA == False):
                threeA = True
            if (course in subfieldB) and (threeB == False):
                threeB = True
            if (course in subfieldC) and (threeC == False):
                threeC = True

    '''We've done the Boolean jig, now we perform the finale'''
    if threeA:
        if threeB or threeC:
            multiSubs = True
    if threeB:
        if threeC:
            multiSubs = True


    tempTaken = userInput                   # I get errors if I just use userInput

    for course in userInput:
        if (course in subfieldAUnique):         # ignore that the Phil dept doesn't require a subfield A course. I just wanted it
            tempTaken.remove(course)            # remove it from our wee tempTaken list that we will later pass to subfieldSort()
            subfieldATaken.append(course)       # if the course is only in subfield A, then we can safely allocate it to subfield A 
            hasList.append(course)              # I have to use hasList to get rid of duplicates. Yes it's embarassing
        if (course in subfieldBUnique):         # similar logic as for A and C
            tempTaken.remove(course)
            subfieldBTaken.append(course)
            hasList.append(course)
        if (course in subfieldCUnique):
            tempTaken.remove(course)
            subfieldCTaken.append(course)
            hasList.append(course)
        if course in core:                      # if i'm understanding reqs correctly, core/electives/300s can overlap w subfield reqs
            coreTaken.append(course)
            hasList.append(course)
        elif course in threes:
            threesTaken.append(course)
            hasList.append(course)
        elif course in extras:
            extraTaken.append(course)
            hasList.append(course)

    
    newB, newC = subfieldSort(tempTaken, 0, 2, subfieldBTaken, subfieldCTaken)

    bLen = len(newB)        # otherwise I get an infinite loop
    if len(newB) > 0:       # if we've added any new B courses
        i = 0
        while i < len(newC):
            subfieldBTaken.append(course)   # add those new courses to the original subfieldBTaken list
            hasList.append(course)
            i += 1
    
    
    cLen = len(newC)        # otherwise I get an infinite loop
    if cLen > 0:            # if we've added any new C courses
        i = 0
        while i < cLen:
            subfieldCTaken.append(newC[i])  # add those new courses to the original subfieldBTaken list
            hasList.append(newC[i])
            i += 1

    # for some reason I get duplicates out of this process. I don't have the brain power to fix it at the source.
    # I'm sure it will cause lots of bugs. Woo!
    bDeDuplicate = []
    cDeDuplicate = []
    [bDeDuplicate.append(x) for x in subfieldBTaken if x not in bDeDuplicate]
    [cDeDuplicate.append(x) for x in subfieldCTaken if x not in cDeDuplicate]
    subfieldBTaken = bDeDuplicate
    subfieldCTaken = cDeDuplicate

    # now we de-dupe the list of the courses someone has taken so we get the real count
    hasListTwo = []
    [hasListTwo.append(x) for x in hasList if x not in hasListTwo]
    hasListTwo.sort()
    has = len(hasListTwo)

    compareUserAndReqs(coreTaken, core, 'core',2)
    compareUserAndReqs(subfieldBTaken, subfieldB, 'Subfield B: Value Theory', 2)
    compareUserAndReqs(subfieldCTaken, subfieldC, 'Subfield C: Metaphysics and Theory of Knowledge',2)
    compareUserAndReqs(threesTaken, threes, '300-level elective', 2)
    if multiSubs:
        print('You have completed 300-level electives in more than one subfield.\n')
    else:
        otherSubs = 'subfield A, subfield B, or subfield C'
        if threeA:
            otherSubs = 'subfield B or subfield C'
        elif threeB:
            otherSubs = 'subfield A or subfield C'
        elif threeC:
            otherSubs = 'subfield A or subfield B'
        print('You have not completed 300-level electives in multiple subfields. To complete the distribution requirement, select additional 300-level courses from', otherSubs, '\n')
    compareUserAndReqs(extraTaken, extras, '200 or 300-level elective', 4)

    remainingElectivesNeeded = needed - numThrees
    if len(subfieldBTaken) == 1:
        remainingElectivesNeeded = remainingElectivesNeeded - 1
    if len(subfieldBTaken) >= 2:
        remainingElectivesNeeded = remainingElectivesNeeded - 2
    if len(subfieldCTaken) != 0:
        remainingElectivesNeeded = remainingElectivesNeeded - 1

    print('You have completed', has, '/', needed, 'requirements for the Philosophy major.')

    # if has != needed: 
    #     print('If you would like to complete the Philosophy major, you need to take:\n')
    #     suggestComplete(coreTaken, int(2 - len(coreTaken)), core, True, 0)
    #     suggestComplete(subfieldBTaken, int(2 - len(subfieldBTaken)), subfieldB, False, 0)
    #     suggestComplete(subfieldCTaken, int(2 - len(subfieldCTaken)), subfieldC, False, 0)
    #     suggestComplete(threesTaken, int(2 - numThrees), threes, False, 0)
    #     suggestComplete(extraTaken, remainingElectivesNeeded, extras, False, 0)

def physics(userInput):
    dept = 'Physics - entering after Fall 2018'
    majorCourses = grabCourses(dept)
    
    needed = 11
    has = matchBandaid(userInput, majorCourses)
    
    print(dept + ': ' + str(has) + '/' + str(needed))

def poliSci(userInput):
    dept = 'Political Science'
    majorCourses = grabCourses(dept)
    
    needed = 9
    has = matchBandaid(userInput, majorCourses)
    
    print(dept + ': ' + str(has) + '/' + str(needed))

def psychology(userInput):
    dept = 'Psychology'
    majorCourses = grabCourses(dept)
    
    needed = 9
    has = matchBandaid(userInput, majorCourses)
    
    print(dept + ': ' + str(has) + '/' + str(needed))

def religion(userInput):
    dept = 'Religion'
    majorCourses = grabCourses(dept)
    
    needed = 9
    has = matchBandaid(userInput, majorCourses)
    
    print(dept + ': ' + str(has) + '/' + str(needed))

def russian(userInput):
    dept = 'Russian'
    majorCourses = grabCourses(dept)
    
    needed = 8
    has = matchBandaid(userInput, majorCourses)
    
    print(dept + ': ' + str(has) + '/' + str(needed))

def russianAreaStudies(userInput):
    dept = 'Russian Area Studies'
    majorCourses = grabCourses(dept)
    
    needed = 8
    has = matchBandaid(userInput, majorCourses)
    
    print(dept + ': ' + str(has) + '/' + str(needed))

def sociology(userInput):
    dept = 'Sociology'
    majorCourses = grabCourses(dept)
    
    needed = 9
    has = matchBandaid(userInput, majorCourses)
    
    print(dept + ': ' + str(has) + '/' + str(needed))

def southAsiaStudies(userInput):
    dept = 'South Asia Studies'
    majorCourses = grabCourses(dept)
    
    needed = 9
    has = matchBandaid(userInput, majorCourses)
    
    print(dept + ': ' + str(has) + '/' + str(needed))

def spanish(userInput):
    dept = 'Spanish'
    majorCourses = grabCourses(dept)
    
    needed = 8
    has = matchBandaid(userInput, majorCourses)
    
    print(dept + ': ' + str(has) + '/' + str(needed))

def studioArt(userInput):
    dept = 'Studio Art - students entering before Fall 2021'
    majorCourses = grabCourses(dept)
    
    needed = 10
    has = matchBandaid(userInput, majorCourses)
    
    print(dept + ': ' + str(has) + '/' + str(needed))

def theatreStudies(userInput):
    dept = 'Theatre Studies'
    majorCourses = grabCourses(dept)
    
    needed = 10
    has = matchBandaid(userInput, majorCourses)
    
    print(dept + ': ' + str(has) + '/' + str(needed))

def womensGenderStudies(userInput):
    dept = "Women's and Gender Studies"
    majorCourses = grabCourses(dept)
    
    needed = 9
    has = matchBandaid(userInput, majorCourses)
    
    print(dept + ': ' + str(has) + '/' + str(needed))

def masterCheck(userInput):
    majorsToCheck = grabMajors(userInput)

    if 'Africana Studies - Africa Concentration' in majorsToCheck:
        africanaStudiesAfrica(userInput)
    if 'Africana Studies - General Africana Studies Concentration' in majorsToCheck:
        africanaStudiesGeneral(userInput)
    if 'Africana Studies - The Caribbean and Latin America Concentration' in majorsToCheck:
        africanaStudiesCaribbeanLatinAmerica(userInput)
    if 'Africana Studies - United States Concentration' in majorsToCheck:
        africanaStudiesUnitedStates(userInput)
    
    if 'American Studies' in majorsToCheck:
        americanStudies(userInput)
    
    if 'Anthropology' in majorsToCheck:
        anthropology(userInput)
    
    if 'Architecture' in majorsToCheck:
        architecture(userInput)
    
    if 'Art History' in majorsToCheck:
        artHistory(userInput)
    
    if 'Astronomy' in majorsToCheck:
        astronomy(userInput)
    if 'Astrophysics' in majorsToCheck:
        astrophysics(userInput)
    
    if 'Biochemistry' in majorsToCheck:
        biochem(userInput)
    if 'Biological Sciences' in majorsToCheck:
        biology(userInput)
    
    if 'Chemical Physics' in majorsToCheck:
        chemicalPhysics(userInput)
    if 'Chemistry' in majorsToCheck:
        chem(userInput)
    
    if 'Cinema and Media Studies - entering in Fall 2020 and before' in majorsToCheck:
        camsPre2020(userInput)
    if 'Cinema and Media Studies - entering in Spring 2021 and after' in majorsToCheck:
        camsCurrent(userInput)
    
    if 'Classical Civilization' in majorsToCheck:
        classicalCivilization(userInput)
    
    if 'Cognitive and Linguistic Sciences - Computer Science Concentration' in majorsToCheck:
        cogSciCS(userInput)
    if 'Cognitive and Linguistic Sciences - Linguistics Concentration' in majorsToCheck:
        cogSciLing(userInput)
    if 'Cognitive and Linguistic Sciences - Philosophy Concentration' in majorsToCheck:
        cogSciPhil(userInput)
    if 'Cognitive and Linguistic Sciences - Psychology Concentration' in majorsToCheck:
        cogSciPsych(userInput)
    
    if 'Comparative Literary Studies' in majorsToCheck:
        compLit(userInput)
    
    if 'Computer Science' in majorsToCheck:
        cs(userInput)
    
    if 'Data Science' in majorsToCheck:
        dataScience(userInput)
    
    if 'East Asian Languages and Cultures' in majorsToCheck:
        eastAsianLangCult(userInput)
    if 'East Asian Studies' in majorsToCheck:
        eastAsianStudies(userInput)
    
    if 'Economics' in majorsToCheck:
        econ(userInput)
    
    if 'English' in majorsToCheck:
        english(userInput)
    if 'English and Creative Writing' in majorsToCheck:
        englishCreativeWriting(userInput)
    
    if 'Environmental Studies' in majorsToCheck:
        environmentalStudies(userInput)
    
    if 'French and Francophone Studies' in majorsToCheck:
        french(userInput)
    if 'French Cultural Studies' in majorsToCheck:
        frenchCulturalStudies(userInput)
    
    if 'Geosciences' in majorsToCheck:
        geosciences(userInput)
    
    if 'German Studies' in majorsToCheck:
        german(userInput)
    
    if 'History' in majorsToCheck:
        history(userInput)
    
    if 'International Relations - Economics' in majorsToCheck:
        internationalRelationsEcon(userInput)
    if 'International Relations - History' in majorsToCheck:
        internationalRelationsHistory(userInput)
    if 'International Relations - Political Science' in majorsToCheck:
        internationalRelationsPoliSci(userInput)
    
    if 'Italian Studies' in majorsToCheck:
        italian(userInput)
    
    if 'Jewish Studies' in majorsToCheck:
        jewishStudies(userInput)
    
    if 'Latin American Studies' in majorsToCheck:
        latinAmericanStudies(userInput)
    
    if 'Mathematics' in majorsToCheck:
        math(userInput)
    
    if 'Media Arts and Sciences' in majorsToCheck:
        mediaArtsSciences(userInput)

    if 'Medieval Renaissance Studies' in majorsToCheck:
        medievalRenaissanceStudies(userInput)

    if 'Middle Eastern Studies' in majorsToCheck:
        middleEasternStudies(userInput)

    if 'Music' in majorsToCheck:
        music(userInput)

    if 'Neuroscience' in majorsToCheck:
        neuroscience(userInput)

    if 'Peace and Justice Studies' in majorsToCheck:
        peaceJusticeStudies(userInput)

    if 'Philosophy' in majorsToCheck:
        philosophy(userInput)

    if 'Physics - entering after Fall 2018' in majorsToCheck:
        physics(userInput)

    if 'Political Science' in majorsToCheck:
        poliSci(userInput)

    if 'Psychology' in majorsToCheck:
        psychology(userInput)

    if 'Religion' in majorsToCheck:
        religion(userInput)

    if 'Russian' in majorsToCheck:
        russian(userInput)
    if 'Russian Area Studies' in majorsToCheck:
        russianAreaStudies(userInput)

    if 'Sociology' in majorsToCheck:
        sociology(userInput)

    if 'South Asia Studies' in majorsToCheck:
        southAsiaStudies(userInput)

    if 'Spanish' in majorsToCheck:
        spanish(userInput)

    if 'Theatre Studies' in majorsToCheck:
        theatreStudies(userInput)

    if "Women's and Gender Studies" in majorsToCheck:
        womensGenderStudies(userInput)

kat = ['ARTH 267','ES 267','CS 111','CS 220','CS 230','CS 231','CS 235','CS 240','CS 242','CS 301','CS 304','CS 342','FREN 101','FREN 102','FREN 201','FREN 202','HIST 245','HIST 220','JPN 290','MATH 205','MATH 206','MATH 223','MATH 225','NEUR 100','PHIL 215','POL1 200','WRIT 166','MATH 220','PHIL 200','HIST 254','HIST 312','PHIL 325']
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

phil = ['PHIL 201','PHIL 221','PHIL 207','PHIL 215','PHIL 311','PHIL 319','PHIL 229','PHIL 306']
bAndC = ['PHIL 200','PHIL 229','PHIL 207','PHIL 215','PHIL 216','PHIL 220','PHIL 229','PHIL 300','PHIL 306','PHIL 103', 'PHIL 112', 'PHIL 218', 'PHIL 245', 'PHIL 311', 'PHIL 319', 'PHIL 325']

#subfieldAUnique = ['PHIL 305']
#subfieldBUnique = ['PHIL 105', 'PHIL 106', 'PHIL 108', 'PHIL 111', 'PHIL 115', 'PHIL 203', 'PHIL 205', 'PHIL 213', 'PHIL 222', 'PHIL 226', 'PHIL 228', 'PHIL 233', 'PHIL 234', 'PHIL 236', 'PHIL 249', 'PHIL 303', 'PHIL 304', 'PHIL 316', 'PHIL 330', 'PHIL 338', 'PHIL 340', 'PHIL 342', 'PHIL 366']
#subfieldCUnique = ['PHIL 103', 'PHIL 112', 'PHIL 207', 'PHIL 215', 'PHIL 216', 'PHIL 218', 'PHIL 245', 'PHIL 311', 'PHIL 319', 'PHIL 325']
    

#cs(kat)
#econ(kat)
#cs(emily)
#econ(emily)
#chem(kat)
#cs(julie)
 
masterCheck(julie)