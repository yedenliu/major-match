from ctypes import *
import pandas as pd
import csv

allCourses = []

''' read in majors and the courses that count toward them from a CSV. Takes courses that are
listed in two departments (but not more than two) and reorders the courses such that the
name is in lexicographic order. Does not remove duplicate courses from the final list.'''
with open("/students/kswint/major-match/DDL/majorReqs.csv","r") as courses:
    r = csv.reader(courses)
    for row in r:
        for item in row[1:]:
            if item != 'Course' and len(item) != 0: # removes column headers and empty cells
                allCourses.append(item)

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
majors = {}
for course in allCourses:
    currentDF = df[(df == course).any(axis = 1)]
    majors[course] = list(currentDF['Major'])

countFrequency(allCourses,majors,freq)

''' creates a dataframe with columns = each course and then the
majors it counts towards'''
df2 = pd.DataFrame.from_dict(majors, orient = 'index')
#df2 = df2.sort_values(df2.columns[0])                               # sort the courses lexicographically
#print(df2.head(50))

''' creates a dataframe with columns = each course and the number of majors it counts
towards, sorted from most majors to least majors.'''
df = pd.DataFrame(list(freq.items()), columns = ['course','freq'])
sortedDF = df.sort_values(by='freq', ascending=False)               # the courses that count towards the most majors at the top
countDF = sortedDF['freq'].value_counts()
#print(sortedDF)

'''Courses with the majors they fullfil as a TSV'''
df2.to_csv('/students/kswint/major-match/DDL/coursesToMajors.tsv', sep = '\t')

'''Courses with the number of majors they fullfil as a TSV'''
df.to_csv('/students/kswint/major-match/DDL/courseMajFreq.tsv', sep = '\t')

tuplefy = [(k, v) for k, v in majors.items()]
#print(tuplefy)
masterDF = pd.DataFrame(tuplefy, columns = ['course','majors'])
masterDF = pd.merge(df, masterDF, on ='course', how ="inner")
# masterDF[['abrev','num']] = masterDF.course.str.split(" ", expand = True)
# masterDF = masterDF.reindex(columns=['course', 'majors', 'freq'])
#print(masterDF)