########################################################################################################
#   IMPORT MODULES
########################################################################################################
from bs4 import BeautifulSoup as BS 
import requests, csv, os
import xml
import traceback # for exceptions

########################################################################################################
#   CREATING SOUP OBJECT
########################################################################################################
def html_object(url):
    page = requests.get(url) 
    if page.status_code == 200: # 200 means success
        html = page.content
    soup = BS(html, 'html.parser')
    return soup

def find_sections(soup):
    return soup.find_all('section')

########################################################################################################
#   GETTERS & HELPER FUNCTIONS
########################################################################################################
'''
Find <div> with the corresponding class to the course name
Param - The <section> (html type) that the course resides in
Return - String of the full course name, marked by the <div> tag and 'coursename_big' class
'''
def remove_tags(text):
    return ''.join(xml.etree.ElementTree.fromstring(text).itertext())

def find_name_tag(section):
    tag = section.find('div',{'class': 'coursename_big'})
    s = tag.string
    return s

'''
Getter for the name features of a course
Param - The <section> (html type) that the course resides in
Return - List of strings of the course name items
'''
def get_name_list(s):
    name_list = [] 
    try:
        content = s.split(' - ')
        long_name = content[1]
        short_name = content[0].split(' ')
        dept = short_name[0].replace('\n', '') 
        cnum = short_name[1].replace('/', '')
        name_list = [dept, cnum, long_name]
    except:
        traceback.print_exc()
    return name_list

def is_crosslisted(section):
    return "Crosslisted" in str(section)

def get_cross_list(s):
    name_list2 = [] 
    try:
        content = s.split(' - ')
        long_name = content[1].strip()
        short_name = content[0].split(' ')
        dept2 = short_name[2]
        cnum2 = short_name[3]
        name_list2 = [dept2, cnum2, long_name]
    except:
        traceback.print_exc()
    return name_list2

'''
Param - The <section> (html type) that the course resides in
Return - list of strings that have the <div> tag and 'coursedetail col-xs-12' class
'''
def find_info_tags(section):
    tag = section.find('div', {'class': 'coursedetail col-xs-12'})
    s = str(tag).replace('</p>', '')
    s = s.replace('<span>', '')
    s = s.replace('</span>', '')
    s = s.replace('</div>', '')
    s_list = s.split('<p>')
    return s_list

def get_info_list(s_list):
    units = ''
    max_enroll = ''
    prereq = ''
    instruct = ''
    dr = ''
    sem_offer = ''
    year_offer = '' 
    for item in s_list:
        item = item.replace('<', '')
        item = item.replace('>', '')
        if 'Units' in item:
            units = item.split(': ')
            units = units[1]
        if 'Max Enroll' in item:
            max_enroll = item.split(': ')
            max_enroll = max_enroll[1]
        if 'Prerequisites' in item:
            item = item.strip('<span>')
            prereq = item.split(': ')
            prereq = prereq[1]
        if 'Instructor' in item:
            instruct = item.split(': ')
            instruct = instruct[1]
        if 'Distribution' in item:
            dr = item.split(': ')
            dr = dr[1]
        if 'Typical' in item:
            sem_offer = item.split(': ')
            sem_offer = sem_offer[1]
        if 'Semesters' in item:
            year_offer = item.split(': ')
            year_offer = year_offer[1]
        else:
            pass
    return [units, max_enroll, prereq, instruct, dr, sem_offer, year_offer]

def get_course_dict(section, iteration):
    # run helper functions
    s = find_name_tag(section)
    s_list = find_info_tags(section)
    info_list = get_info_list(s_list)
    
    # defining variables
    dept = None
    cnum = None
    name = None
    if iteration == 2:
        try:
            name_list = get_cross_list(s)
            dept = name_list[0]
            cnum = name_list[1]
            name = name_list[2]
        except:
            traceback.print_exc()
    else:
        try:
            name_list = get_name_list(s)
            dept = name_list[0]
            cnum = name_list[1]
            name = name_list[2]
        except:
            traceback.print_exc()
    
    units = info_list[0]
    max_enroll = info_list[1]
    prereq = info_list[2]
    instruct = info_list[3]
    dr = info_list[4]
    sem_offer = info_list[5]
    year_offer = info_list[6]

    # defining dictionary
    course_dict =  {'Department': dept,
                    'Course Number': cnum,
                    'Course Name': name,
                    'Units': units, 
                    'Max Enrollment': max_enroll, 
                    'Prerequisites': prereq, 
                    'Instructor': instruct,
                    'Distribution Requirements': dr, 
                    'Typical Periods Offered': sem_offer, 
                    'Semesters Offered this Academic Year': year_offer} 
    return course_dict

def all_courses(sections):
    course_list = []
    for section in sections:
        course = get_course_dict(section, 1)
        course_list.append(course)
        if is_crosslisted(section):
            course2 = get_course_dict(section, 2)
            course_list.append(course2)
    return course_list