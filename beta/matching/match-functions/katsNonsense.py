import pandas as pd
import csv

finalList = []
courseIn = 'STAT 218, STAT 220, STAT 221, STAT 228, STAT 260, STAT 318'
courseList = courseIn.split(',')
for item in courseList:
    if item[0] == ' ':
        item = item[1:]
    if item[-1:] == ',':
        item = item[0:-1]
    finalList.append(item)
#print(finalList)

majorReqs = '/students/kswint/major-match/beta/DDL/majorReqsDF.tsv'
coursesToMajors = '/students/kswint/major-match/beta/DDL/coursesToMajors.tsv'
allCourses = '/students/kswint/major-match/beta/DDL/all_courses.tsv'

allCoursesListTemp = []

with open(allCourses, "r") as allCourses:
    for row in allCourses:
        rho = row.split(' ')
        rho = rho[0].split('\t')
        dept = rho[0]
        num = rho[1]
        course = dept + ' ' + num
        allCoursesListTemp.append(course)

allCoursesList = []
[allCoursesList.append(x) for x in allCoursesListTemp if x not in allCoursesList]
#print(allCoursesList)

coursesWithMajors = []

with open(coursesToMajors, "r") as ctm:
    for row in ctm:
        rho = row.split('\t')
        coursesWithMajors.append(rho[1])

#print(coursesWithMajors)

coursesWithoutMajors = []

independentStudies = ['250','250H','250GH','250GH','350','350H','360','370','099','099G']
deptsExclude100s = ['KOR','SPAN','PORT','JPN','PHIL','RUSS','CHIN','FREN']
introNums = ['101','102','103','201']
independentsToCheck = []

def intro(course):
    dept, num = course.split(' ')
    if (dept not in deptsExclude100s) and (num not in introNums):
        return(True)
    else:
        return(False)

for course in allCoursesList:
    if course not in coursesWithMajors:
        number = course.split(' ')[1] 
        if (number not in independentStudies) and intro(course):
            coursesWithoutMajors.append(course)
        if number in independentStudies:
            independentsToCheck.append(course)


coursesWithoutMajors.sort()
print(coursesWithoutMajors)
print(independentsToCheck)
