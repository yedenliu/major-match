# -*- coding: utf-8 -*-
'''
CS304 Course Catalog Scraping

INSTALL:
pip install bs4 --> NEED TO UPDATE OR ELSE FIND FUNCTIONS DON'T WORK
pip install soupsieve
'''
########################################################################################################
#   IMPORT MODULES
########################################################################################################
from bs4 import BeautifulSoup as BS 
import requests, csv, os
from scrape_helpers import *

########################################################################################################
#   FUNCTIONS TO COMPILE DATA
########################################################################################################

fields=['Department', 
        'Course Number', 
        'Course Name',
        'Units', 
        'Max Enrollment', 
        'Prerequisites', 
        'Instructor', 
        'Distribution Requirements', 
        'Typical Periods Offered', 
        'Semesters Offered this Academic Year']

def create_tsv(dept_id, url):
    file_name = str(dept_id) + '_courses.tsv'
    soup = html_object(url)
    sections = find_sections(soup)
    data = all_courses(sections)
    cwd = '/students/yl9/cs304/major-match' #'/students/majormatch/project/'
    with open(os.path.join(cwd, 'DDL', 'tsv_files', file_name), 'a', encoding='UTF8', newline='') as f:
        writer = csv.DictWriter(f, fieldnames=fields, delimiter='\t')
        # write the data
        writer.writerows(data)

########################################################################################################
#   DATA IMPORT + EXPORT
########################################################################################################
def parse_majors():
    # iterate through the catalog_urls.tsv file for (1) dept num (2) catalog page URL
    import pandas as pd
    cwd = os.getcwd()
    file_path = os.path.join(cwd, 'catalog_urls.tsv')
    col_list = ['dept_id', 'cat_url']
    df = pd.read_csv(file_path, delimiter='\t', usecols=col_list,)
    for i in range(len(df.index)):
        dept_id = df.iat[i, 0]
        cat_url = df.iat[i, 1]
        create_tsv(dept_id, cat_url)

parse_majors()