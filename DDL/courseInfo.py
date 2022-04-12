from ctypes import *
import pandas as pd
import csv

duplicateCourses = []
allCourses = []

''' read in majors and the courses that count toward them from a CSV. Takes courses that are
listed in two departments (but not more than two) and reorders the courses such that the
name is in lexicographic order. Does not remove duplicate courses from the final list.'''
with open("/students/kswint/cs304/project/personal/majorReqs.csv","r") as courses:
    r = csv.reader(courses)
    for row in r:
        for item in row[1:]:
            if '/' in item:                         # removes duplicate cross-listed courses
                first = item.split('/')[0]          # gets first department
                second = item.split('/')[1]         # gets second department
                if first < second:                  # reorders them in lexicographic order
                    item = first + '/' + second
                else:
                    duplicateCourses.append(item)   # so we know where there are duplicates and can adjust
                    item = second + '/' + first
            if item != 'Course' and len(item) != 0: # removes column headers and empty cells
                allCourses.append(item)

allCourses.sort()                                   # sorts the course list lexigocraphically
duplicateCourses.sort()
#print(allCourses)

freq = {}
""" countFrequency(courseList, freqDict) is a function that takes a list of courses and
a dictionary in which to store their frequencies, and then determines the number of times
each course appears in the given list and assigns their frequencies as their values. """
def countFrequency(courseList, freqDict):
    for course in courseList:
        if (course in freqDict):
            freqDict[course] += 1
        else:
            freqDict[course] = 1

countFrequency(allCourses,freq)
# print(freq)

''' using pandas to read the CSV into a dataframe'''
df = pd.read_csv('/students/kswint/cs304/project/personal/majorReqs.csv')
# print(df)

uncrossedCourses = {}
def uncross(courseDict):
    for key in courseDict:
        if '/' in key:
            first = key.split('/')[0]          # gets first department
            second = key.split('/')[1]
            uncrossedCourses[first] = courseDict[key]
            uncrossedCourses[second] = courseDict[key]
            if len(key.split('/')) > 2:
                third = key.split('/')[2]
                uncrossedCourses[third] = courseDict[key]
        else:
            uncrossedCourses[key] = courseDict[key]

''' create a dictionary where the keys are the courses and the values are a list of majors
the course counts towards. '''
majors = {}
for course in allCourses:
    currentDF = df[(df == course).any(axis = 1)]
    majors[course] = list(currentDF['Major'])
# print(majors)

uncross(majors)
#print(uncrossedCourses)

def padMajorList(majorList):
    if len(majorList) <= 65:
        majorList.append('')
        padMajorList(majorList)
    return majorList

#for key in majors:
#    padMajorList(majors[key])

#print(majors)

''' creates a dataframe with columns = each course and then the
majors it counts towards'''

df2 = pd.DataFrame.from_dict(majors, orient = 'index')
#print(df2)

''' creates a dataframe with columns = each course and the number of majors it counts
towards, sorted from most majors to least majors.'''
df = pd.DataFrame(list(freq.items()), columns = ['course','freq'])
sortedDF = df.sort_values(by='freq', ascending=False)
countDF = sortedDF['freq'].value_counts()
#print(sortedDF.head(50))

'''Courses with the majors they fullfil as a TSV'''
#df2.to_csv('/students/kswint/major-match/DDL/coursesToMajors.tsv', sep = '\t')

'''Courses with the number of majors they fullfil as a TSV'''
#df.to_csv('/students/kswint/major-match/DDL/courseMajFreq.tsv', sep = '\t')

tuplefy = [(k, v) for k, v in majors.items()]
#print(tuplefy)
# masterDF = pd.DataFrame(tuplefy, columns = ['course','majors'])
# masterDF = pd.merge(df, masterDF, on ='course', how ="inner")
# masterDF[['abrev','num']] = masterDF.course.str.split(" ", expand = True)
# masterDF = masterDF.reindex(columns=['course', 'majors', 'freq'])
# print(masterDF)