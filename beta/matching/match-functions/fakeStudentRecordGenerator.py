'''This file generates lists of courses pulled from ten departments to help us test our matching process
on longer and more varied course histories. It is for testing purposes only.'''

import pandas as pd
import csv
from random import randint
import random

from pymysql import NULL

majorReqs = '/students/kswint/major-match/DDL/majorReqsDF.tsv'
coursesToMajors = '/students/kswint/major-match/DDL/coursesToMajors.tsv'

array = [randint(1, 64) for i in range(10)]
print(array)

record = []
studentRecord = []      # temp variable

def tenDepts():
    count = 0
    with open(majorReqs, 'r') as courses:
        for row in courses:
            eligible = []
            if count in array:
                rho = row.split('\t')
                for item in rho[1:]:
                    if (len(item) >= 5):
                        if item[-2:] == '\n':
                            pass
                        else:
                            eligible.append(item)
                if len(eligible) > 0:
                    if count == array[0]:
                        studentRecord.append(random.choice(eligible[1:]))
                        studentRecord.append(random.choice(eligible[1:]))
                        studentRecord.append(random.choice(eligible[1:]))
                        studentRecord.append(random.choice(eligible[1:]))
                        studentRecord.append(random.choice(eligible[1:]))
                    if count == array[1]:
                        studentRecord.append(random.choice(eligible[1:]))
                        studentRecord.append(random.choice(eligible[1:]))
                    if count == array[2]:
                        studentRecord.append(random.choice(eligible[1:]))
                        studentRecord.append(random.choice(eligible[1:]))
                        studentRecord.append(random.choice(eligible[1:]))
                        studentRecord.append(random.choice(eligible[1:]))
                    if count == array[3]:
                        studentRecord.append(random.choice(eligible[1:]))
                    if count == array[4]:
                        studentRecord.append(random.choice(eligible[1:]))
                    if count == array[5]:
                        studentRecord.append(random.choice(eligible[1:]))
                        studentRecord.append(random.choice(eligible[1:]))
                    if count == array[6]:
                        studentRecord.append(random.choice(eligible[1:]))
                        studentRecord.append(random.choice(eligible[1:]))
                        studentRecord.append(random.choice(eligible[1:]))
                        studentRecord.append(random.choice(eligible[1:]))
                        studentRecord.append(random.choice(eligible[1:]))
                        studentRecord.append(random.choice(eligible[1:]))
                        studentRecord.append(random.choice(eligible[1:]))
                        studentRecord.append(random.choice(eligible[1:]))
                        studentRecord.append(random.choice(eligible[1:]))
                    if count == array[7]:
                        studentRecord.append(random.choice(eligible[1:]))
                    if count == array[8]:
                        studentRecord.append(random.choice(eligible[1:]))
                        studentRecord.append(random.choice(eligible[1:]))
                        studentRecord.append(random.choice(eligible[1:]))
                        studentRecord.append(random.choice(eligible[1:]))
                    if count == array[9]:
                        studentRecord.append(random.choice(eligible[1:]))
            count += 1
    record = list(set(studentRecord))
    print(record)

tenDepts()

