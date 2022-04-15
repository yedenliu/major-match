from ast import Index
from ctypes import *
import pandas as pd
import csv

allCourses = []
majorKey = {}

''' read in majors and the courses that count toward them from a CSV. Takes courses that are
listed in two departments (but not more than two) and reorders the courses such that the
name is in lexicographic order. Does not remove duplicate courses from the final list.'''
with open("/students/kswint/major-match/DDL/majorReqs.csv","r") as courses:
    r = csv.reader(courses)
    for row in r:
        major = row[0]
        majorKey[major] = []
        majorCourses = []
        for item in row[1:]:
            if item != 'Course' and len(item) != 0: # removes column headers and empty cells
                allCourses.append(item)
                majorCourses.append(item)
                majorKey[major] = majorCourses

''' Some departments have requirements like "take one 200-level CS course." Provide the (1) file containing
all courses that the department offers, (2) the department name as it is in our data, (3) the department
abbreviation, and (4) the level of the course you wish to add. Autoadds those courses to the allCourses
list and to the dictionary of majors and the courses they count for.'''
def populateRegExCourses(file, dept, deptAprev, level):
    with open(file, "r") as courses:
        for row in courses:
            rho = row.split('\t')
            course = str(rho[0] + " " + rho[1])
            if deptAprev.__eq__(rho[0]) and (int(rho[1][0]) == level):
                allCourses.append(course)
                majorKey[dept].append(course)

populateRegExCourses('/students/kswint/major-match/DDL/tsv_files/20_courses.tsv','Computer Science','CS',2)
populateRegExCourses('/students/kswint/major-match/DDL/tsv_files/20_courses.tsv','Computer Science','CS',2)
populateRegExCourses('/students/kswint/major-match/DDL/tsv_files/20_courses.tsv','Computer Science','CS',3)
populateRegExCourses('/students/kswint/major-match/DDL/tsv_files/20_courses.tsv','Computer Science','CS',3)
populateRegExCourses('/students/kswint/major-match/DDL/tsv_files/12_courses.tsv','Chemistry','CHEM',3)
populateRegExCourses('/students/kswint/major-match/DDL/tsv_files/44_courses.tsv','Mathematics','MATH',3)
populateRegExCourses('/students/kswint/major-match/DDL/tsv_files/44_courses.tsv','Mathematics','MATH',3)
populateRegExCourses('/students/kswint/major-match/DDL/tsv_files/52_courses.tsv','Physics - entering after Fall 2018','PHYS',3)
populateRegExCourses('/students/kswint/major-match/DDL/tsv_files/52_courses.tsv','Physics - entering after Fall 2018','PHYS',3)

allCourses.sort()                                   # sorts the course list lexigocraphically

freq = {}
""" countFrequency(courseList, freqDict) is a function that takes a list of courses and
a dictionary in which to store their frequencies, and then determines the number of times
each course appears in the given list and assigns their frequencies as their values. """
def countFrequency(courseList, majorDict, freqDict):
    for course in courseList:
        freqDict[course] = len(majorDict[course])

''' using pandas to read the CSV into a dataframe'''
df = pd.read_csv('/students/kswint/major-match/DDL/majorReqs.csv', sep = ',', lineterminator = '\n', error_bad_lines = False)
#print(df)

''' create a dictionary where the keys are the courses and the values are a list of majors
the course counts towards. '''
# majors = {}
# for course in allCourses:
#     currentDF = df[(df == course).any(axis = 1)]
#     majors[course] = list(currentDF['Major'])

majors = {}
for key in majorKey:
    for course in majorKey[key]:
        if course in majors:
            if key not in majors[course]:
                majors[course].append(key)
        else:
            majors[course] = []
            majors[course].append(key)

# for key in majors:
#     print(key, ':\t', majors[key])

countFrequency(allCourses,majors,freq)

''' creates a dataframe with columns = each course and then the
majors it counts towards'''
index = pd.Index(range(0, 1292, 1))
#df2 = pd.DataFrame.from_dict(majors, orient = 'index', index = index)
df2 = pd.DataFrame(majors, index = index)
#df3 = df2.set_index(index, drop = True, append=True, inplace=True, verify_integrity=False)
#df2 = df2.sort_values(df2.columns[0])                               # sort the courses lexicographically
print(df2)

''' creates a dataframe with columns = each course and the number of majors it counts
towards, sorted from most majors to least majors.'''
df = pd.DataFrame(list(freq.items()), columns = ['course','freq'])
sortedDF = df.sort_values(by='freq', ascending=False)               # the courses that count towards the most majors at the top
countDF = sortedDF['freq'].value_counts()
print(sortedDF)

'''Courses with the majors they fullfil as a TSV'''
#df2.to_csv('/students/kswint/major-match/DDL/coursesToMajors.tsv', sep = '\t')

'''Courses with the number of majors they fullfil as a TSV'''
#df.to_csv('/students/kswint/major-match/DDL/courseMajFreq.tsv', sep = '\t')

'''Create the master dataframe for export!'''
tuplefy = [(k, v) for k, v in majors.items()]           # converts the dictionary of majors a course counts towards
                                                        # into a list for easy MySQL parsing. Otherwise, each major
                                                        # would be its own column.
masterDF = pd.DataFrame(tuplefy, columns = ['course','majors'])      # begin the dataframe! use courses and majors
masterDF = pd.merge(df, masterDF, on ='course', how ="inner")        # use an inner join to add the frequency column
masterDF[['abrev','num']] = masterDF.course.str.split(expand = True) # create two new columns; one for the department
                                                                     # ("abrev") and one for the course number.
masterDF = masterDF.reindex(columns=['course', 'abrev', 'num', 'freq', 'majors'])   # rearrange the rows for aesthetic purposes
print(masterDF)

''' Master TSV! Columns are the course, the department (abrev), the course number (three digit, not CRN),
the number of majors that course counts towards, and a list of the majors that course counts towards.'''
# masterDF.to_csv('/students/kswint/major-match/DDL/completeMajorTable.tsv', sep = '\t')