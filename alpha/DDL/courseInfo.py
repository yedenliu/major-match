from ast import Index
from ctypes import *
import pandas as pd
import csv

allCourses = []         # to store every single course that counts towards a major
majorKey = {}           # a dictionary w/ a major as a key, and a list of courses that
                        # count towards it as its value

''' read in majors and the courses that count toward them from a CSV. Takes courses that are
listed in two departments (but not more than two) and reorders the courses such that the
name is in lexicographic order. Does not remove duplicate courses from the final list.'''
with open("/students/kswint/major-match/DDL/majorReqs.csv","r") as courses:
    r = csv.reader(courses)
    for row in r:
        major = row[0]          # first item in a row is the major
        majorKey[major] = []    # add that major to the majorKey dictionary
        majorCourses = []       # create a list, to be populated w courses that count towards the major
        for item in row[1:]:    # skip header row
            if item != 'Course' and len(item) != 0: # removes column headers and empty cells
                allCourses.append(item)             # add to allCourses list (add. ben allows freq counting)
                majorCourses.append(item)           # adds to list of courses we just created
                majorKey[major] = majorCourses      # resets key's value

''' Some departments have requirements like "take one 200-level CS course." Provide the (1) file containing
all courses that the department offers, (2) the department name as it is in our data, (3) the department
abbreviation, and (4) the level of the course you wish to add. Autoadds those courses to the allCourses
list and to the dictionary of majors and the courses they count for. Note that this does not account
for crosslisted courses; if a department allows you do take any 200 level math or stats class, you'll
have to call the method separately for the math courses and the stat courses.'''
def populateRegExCourses(file, dept, deptAprev, level, quantity):
    with open(file, "r") as courses:        # 'file' is the TSV of courses a dept offers
        for row in courses:                 # iterate through all of those courses
            rho = row.split('\t')           # split by deliminator so we can grab dept and num
            course = str(rho[0] + " " + rho[1])     # grab that dept and num
            i = 0
            if deptAprev.__eq__(rho[0]) and (int(rho[1][0]) == level):  # check if it's the right dept and level
                allCourses.append(course)   # add to allCourses (add. ben we can freq count)
                majorKey[dept].append(course)       # add to the list of courses that counts towards that major
                i += 1

''' Manually calling the populateRegExCourses() function manually for relevant departments and
levels. '''
allCoursesTSV = '/students/kswint/major-match/DDL/all_courses.tsv'

populateRegExCourses(allCoursesTSV,'American Studies','AMST',2)
populateRegExCourses(allCoursesTSV,'American Studies','AMST',3)

populateRegExCourses(allCoursesTSV,'Anthropology','ANTH',2)
populateRegExCourses(allCoursesTSV,'Anthropology','ANTH',3)

populateRegExCourses(allCoursesTSV,'Computer Science','CS',2)
populateRegExCourses(allCoursesTSV,'Computer Science','CS',3)

populateRegExCourses(allCoursesTSV,'Chemistry','CHEM',3)

populateRegExCourses(allCoursesTSV,'Mathematics','MATH',3)

populateRegExCourses(allCoursesTSV,'Physics - entering after Fall 2018','PHYS',3)

populateRegExCourses(allCoursesTSV,'Astrophysics','PHYS',3)

populateRegExCourses(allCoursesTSV,'Africana Studies - General Africana Studies Concentration','AFR',3)

populateRegExCourses(allCoursesTSV,'Anthropology','ANTH',1)
populateRegExCourses(allCoursesTSV,'Anthropology','ANTH',2)
populateRegExCourses(allCoursesTSV,'Anthropology','ANTH',3)

populateRegExCourses(allCoursesTSV,'Astronomy','ASTR',2)
populateRegExCourses(allCoursesTSV,'Astronomy','ASTR',3)
populateRegExCourses(allCoursesTSV,'Astronomy','GEOS',3)    # guessing that geoscience counts as a "related field"
populateRegExCourses(allCoursesTSV,'Astronomy','PHYS',3)    # guessing that physics counts as a "related field"
populateRegExCourses(allCoursesTSV,'Astronomy','CHEM',3)    # guessing that chemistry counts as a "related field"
populateRegExCourses(allCoursesTSV,'Astronomy','BISC',3)    # guessing that bisc counts as a "related field"

populateRegExCourses(allCoursesTSV,'Studio Art - students entering before Fall 2021','ARTS',2)
populateRegExCourses(allCoursesTSV,'Studio Art - students entering before Fall 2021','ARTS',3)

populateRegExCourses(allCoursesTSV,'Comparative Literary Studies','CLPT',1)
populateRegExCourses(allCoursesTSV,'Comparative Literary Studies','CLPT',2)
populateRegExCourses(allCoursesTSV,'Comparative Literary Studies','CLPT',3)

populateRegExCourses(allCoursesTSV,'Comparative Literary Studies','ENG',1)
populateRegExCourses(allCoursesTSV,'Comparative Literary Studies','ENG',2)
populateRegExCourses(allCoursesTSV,'Comparative Literary Studies','ENG',3)

populateRegExCourses(allCoursesTSV,'Italian Studies','ITAS',2)
populateRegExCourses(allCoursesTSV,'Italian Studies','ITAS',3)

populateRegExCourses(allCoursesTSV,'Jewish Studies','HEBR',2)
populateRegExCourses(allCoursesTSV,'Jewish Studies','HEBR',3)
populateRegExCourses(allCoursesTSV,'Jewish Studies','JWST',2)
populateRegExCourses(allCoursesTSV,'Jewish Studies','JWST',3)

populateRegExCourses(allCoursesTSV,'Mathematics','MATH',2)
populateRegExCourses(allCoursesTSV,'Mathematics','MATH',3)

populateRegExCourses(allCoursesTSV,'Middle Eastern Studies','MES',2)
populateRegExCourses(allCoursesTSV,'Middle Eastern Studies','MES',3)

populateRegExCourses(allCoursesTSV,'Music','CAMS',1)
populateRegExCourses(allCoursesTSV,'Music','CAMS',2)
populateRegExCourses(allCoursesTSV,'Music','CAMS',3)
populateRegExCourses(allCoursesTSV,'Music','MAS',1)
populateRegExCourses(allCoursesTSV,'Music','MAS',2)
populateRegExCourses(allCoursesTSV,'Music','MAS',3)

populateRegExCourses(allCoursesTSV,'Peace and Justice Studies','PEAC',2)
populateRegExCourses(allCoursesTSV,'Peace and Justice Studies','PEAC',3)

populateRegExCourses(allCoursesTSV,'Political Science','POL1',1)
populateRegExCourses(allCoursesTSV,'Political Science','POL1',2)
populateRegExCourses(allCoursesTSV,'Political Science','POL1',3)
populateRegExCourses(allCoursesTSV,'Political Science','POL2',1)
populateRegExCourses(allCoursesTSV,'Political Science','POL2',2)
populateRegExCourses(allCoursesTSV,'Political Science','POL2',3)
populateRegExCourses(allCoursesTSV,'Political Science','POL3',1)
populateRegExCourses(allCoursesTSV,'Political Science','POL3',2)
populateRegExCourses(allCoursesTSV,'Political Science','POL3',3)
populateRegExCourses(allCoursesTSV,'Political Science','POL4',1)
populateRegExCourses(allCoursesTSV,'Political Science','POL4',2)
populateRegExCourses(allCoursesTSV,'Political Science','POL4',3)

populateRegExCourses(allCoursesTSV,'Psychology','PSYC',2)
populateRegExCourses(allCoursesTSV,'Psychology','PSYC',3)

populateRegExCourses(allCoursesTSV,'Religion','REL',1)
populateRegExCourses(allCoursesTSV,'Religion','REL',2)
populateRegExCourses(allCoursesTSV,'Religion','REL',3)
populateRegExCourses(allCoursesTSV,'Religion','AMST',2)
populateRegExCourses(allCoursesTSV,'Religion','AMST',3)
populateRegExCourses(allCoursesTSV,'Religion','EALC',2)
populateRegExCourses(allCoursesTSV,'Religion','EALC',3)
populateRegExCourses(allCoursesTSV,'Religion','JWST',2)
populateRegExCourses(allCoursesTSV,'Religion','JWST',)
populateRegExCourses(allCoursesTSV,'Religion','MES',2)
populateRegExCourses(allCoursesTSV,'Religion','MES',3)
populateRegExCourses(allCoursesTSV,'Religion','JWST',2)
populateRegExCourses(allCoursesTSV,'Religion','JWST',3)
populateRegExCourses(allCoursesTSV,'Religion','MER',2)
populateRegExCourses(allCoursesTSV,'Religion','MER',3)
populateRegExCourses(allCoursesTSV,'Religion','SAS',2)
populateRegExCourses(allCoursesTSV,'Religion','SAS',3)

populateRegExCourses(allCoursesTSV,'Sociology','SOC',2)
populateRegExCourses(allCoursesTSV,'Sociology','SOC',3)

populateRegExCourses(allCoursesTSV,'South Asia Studies','SAS',1)
populateRegExCourses(allCoursesTSV,'South Asia Studies','SAS',2)
populateRegExCourses(allCoursesTSV,'South Asia Studies','SAS',3)

populateRegExCourses(allCoursesTSV,'Spanish','SPAN',2)
populateRegExCourses(allCoursesTSV,'Spanish','SPAN',3)

populateRegExCourses(allCoursesTSV,'Theatre Studies','THST',3)

populateRegExCourses(allCoursesTSV,"Women's and Gender Studies",'WGST',1)
populateRegExCourses(allCoursesTSV,"Women's and Gender Studies",'WGST',2)
populateRegExCourses(allCoursesTSV,"Women's and Gender Studies",'WGST',3)

allCourses.sort()    # sorts the course list lexigocraphically

''' A function that removes a course from the list of courses that count for a major. For example,
populateRegExCourses was used to add all 200 level Psychology courses to the major, but the Psychology
department does not count PSYC 299 or PSYC 299H towards the major.'''
def removeCourseFromMajor(major, course):
    if course in majorKey:
        majorKey[major].remove(course)
        removeCourseFromMajor(major,course)
    if course in allCourses:
        allCourses.remove(course)
        removeCourseFromMajor(major,course)
    else:
        pass

removeCourseFromMajor('American Studies','AMST 350')
removeCourseFromMajor('American Studies','AMST 360')
removeCourseFromMajor('American Studies','AMST 370')

removeCourseFromMajor('Art History','ARTH 350')

removeCourseFromMajor('Biological Sciences','BISC 250')
removeCourseFromMajor('Biological Sciences','BISC 250H')
removeCourseFromMajor('Biological Sciences','BISC 350')
removeCourseFromMajor('Biological Sciences','BISC 350H')
removeCourseFromMajor('Biological Sciences','BISC 355')
removeCourseFromMajor('Biological Sciences','BISC 360')
removeCourseFromMajor('Biological Sciences','BISC 365')
removeCourseFromMajor('Biological Sciences','BISC 370')

removeCourseFromMajor('Chemistry','CHEM 250')
removeCourseFromMajor('Chemistry','CHEM 250H')
removeCourseFromMajor('Chemistry','CHEM 350')
removeCourseFromMajor('Chemistry','CHEM 350H')
removeCourseFromMajor('Chemistry','CHEM 360')
removeCourseFromMajor('Chemistry','CHEM 370')

removeCourseFromMajor('Computer Science','CS 250')
removeCourseFromMajor('Computer Science','CS 250H')
removeCourseFromMajor('Computer Science','CS 350')
removeCourseFromMajor('Computer Science','CS 350H')
removeCourseFromMajor('Computer Science','CS 360')
removeCourseFromMajor('Computer Science','CS 370')

removeCourseFromMajor('Economics','ECON 350')
removeCourseFromMajor('Economics','ECON 360')
removeCourseFromMajor('Economics','ECON 370')

removeCourseFromMajor('English','ENG 350')
removeCourseFromMajor('English','ENG 360')
removeCourseFromMajor('English','ENG 370')

removeCourseFromMajor('Environmental Studies','ES 350')

removeCourseFromMajor('Neuroscience','NEUR 240')
removeCourseFromMajor('Neuroscience','NEUR 250')
removeCourseFromMajor('Neuroscience','NEUR 250H')
removeCourseFromMajor('Neuroscience','NEUR 340')
removeCourseFromMajor('Neuroscience','NEUR 350')
removeCourseFromMajor('Neuroscience','NEUR 350H')
removeCourseFromMajor('Neuroscience','NEUR 360')
removeCourseFromMajor('Neuroscience','NEUR 370')

removeCourseFromMajor('Psychology','PSYC 299')
removeCourseFromMajor('Psychology','PSYC 299H')

removeCourseFromMajor('Russian','RUSS 101')
removeCourseFromMajor('Russian','RUSS 102')
removeCourseFromMajor('Russian','RUSS 203')
removeCourseFromMajor('Russian','RUSS 303')

removeCourseFromMajor('Spanish','SPAN 201')
removeCourseFromMajor('Spanish','SPAN 202')

freq = {}
""" countFrequency(courseList, freqDict) is a function that takes a list of courses and
a dictionary in which to store their frequencies, and then determines the number of times
each course appears in the given list and assigns their frequencies as their values. """
def countFrequency(courseList, majorDict, freqDict):
    for course in courseList:
        freqDict[course] = len(majorDict[course])

''' using pandas to read the CSV into a dataframe'''
df = pd.read_csv('/students/kswint/major-match/DDL/majorReqs.csv', sep = ',', lineterminator = '\n', error_bad_lines = False)

''' create a dictionary where the keys are the courses and the values are a list of majors
the course counts towards. '''
majors = {}
for key in majorKey:
    for course in majorKey[key]:
        if course in majors:
            if key not in majors[course]:
                majors[course].append(key)
        else:
            majors[course] = []
            majors[course].append(key)

countFrequency(allCourses,majors,freq)

''' creates a dataframe with columns 1 = each course and then the
majors it counts towards'''
index = pd.Index(range(0, 1292, 1))
courseToMajorsDF = pd.DataFrame.from_dict(majors, orient = 'index')
courseToMajorsDF = courseToMajorsDF.reset_index()
courseToMajorsDF.rename(
    columns={'index':'course', '0':'major0', '1':'major1', '2':'major2',
             '3':'major3', '4':'major4', '5':'major5', '6':'major6'}
            ,inplace=True)
courseToMajorsDF = courseToMajorsDF.sort_values(by = 'course')                               # sort the courses lexicographically

'''Courses with the majors they fullfil as a TSV'''
courseToMajorsDF.to_csv('/students/kswint/major-match/DDL/coursesToMajors.tsv', sep = '\t')

majorReqsDF = pd.DataFrame.from_dict(majorKey, orient = 'index')
majorReqsDF.to_csv('/students/kswint/major-match/DDL/majorReqsDF.tsv', sep = '\t')

''' creates a dataframe with columns = each course and the number of majors it counts
towards.'''
courseFreqDF = pd.DataFrame(list(freq.items()), columns = ['course','freq'])

'''Courses with the number of majors they fullfil as a TSV'''
courseFreqDF.to_csv('/students/kswint/major-match/DDL/courseMajFreq.tsv', sep = '\t')

''' sorts courseFreqDF by the number of majors a course counts towards, with the most number
of majors at the top and least at the bottom'''
sortedDF = courseFreqDF.sort_values(by='freq', ascending=False)               # the courses that count towards the most majors at the top
print(sortedDF.head(50))

''' counts the number of courses that count towards X majors. For instance, it counts
the number of courses that only contribute to two majors.'''
countDF = sortedDF['freq'].value_counts()
print(countDF)

'''Create the master dataframe for export!'''
tuplefy = [(k, v) for k, v in majors.items()]           # converts the dictionary of majors a course counts towards
                                                        # into a list for easy MySQL parsing. Otherwise, each major
                                                        # would be its own column.
masterDF = pd.DataFrame(tuplefy, columns = ['course','majors'])      # begin the dataframe! use courses and majors
masterDF = pd.merge(courseFreqDF, masterDF, on ='course', how ="inner")        # use an inner join to add the frequency column
masterDF[['abrev','num']] = masterDF.course.str.split(expand = True) # create two new columns; one for the department
                                                                     # ("abrev") and one for the course number.
masterDF = masterDF.reindex(columns=['course', 'abrev', 'num', 'freq', 'majors'])   # rearrange the rows for aesthetic purposes
masterDF = masterDF.drop('course', 1)
print('\n', masterDF)

''' Master TSV! Columns are the course, the department (abrev), the course number (three digit, not CRN),
the number of majors that course counts towards, and a list of the majors that course counts towards.'''
masterDF.to_csv('/students/kswint/major-match/DDL/completeMajorTable.tsv', sep = '\t')