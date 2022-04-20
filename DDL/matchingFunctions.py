import pandas as pd
import csv

majorReqs = '/students/kswint/major-match/DDL/majorReqsDF.tsv'
coursesToMajors = '/students/kswint/major-match/DDL/coursesToMajors.tsv'

def cs(userInput, majorRow):
    introductorySequence = ['CS 111','CS 230']
    math = ['MATH 225']
    core = ['CS 231','CS 235','CS 240']
    with open(majorReqs, "r") as courses:
        for row in courses:
            if row[0].equals('Computer Science'):
    electives = ['CS 203','CS 204','CS 220','CS 221','CS 232','CS 234','CS 242','CS 250','CS 250H','CS 251','CS 221','CS 301','CS 304']