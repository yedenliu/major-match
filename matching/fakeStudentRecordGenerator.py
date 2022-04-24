import pandas as pd
import csv
from random import randint
import random

from pymysql import NULL

majorReqs = '/students/kswint/major-match/DDL/majorReqsDF.tsv'
coursesToMajors = '/students/kswint/major-match/DDL/coursesToMajors.tsv'

array = [randint(1, 64) for i in range(10)]
print(array)

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
                course1 = random.choice(eligible[1:])
                course2 = random.choice(eligible[1:])
                print(rho[0], course1, course2)
        count += 1

