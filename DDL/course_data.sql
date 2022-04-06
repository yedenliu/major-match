--insert data using CSV files
-- CS DEPT
load data local infile 'tsv_files/cs_courses.tsv'
into table courses 
fields terminated by '\t' 
enclosed by ''''
lines terminated by '\n'
(dept, cnum, `name`, units, max_enroll, prereq, instruct, dr, sem_offered, year_offered);

-- CHEM DEPT
load data local infile 'tsv_files/chem_courses.tsv'
into table courses 
fields terminated by '\t' 
enclosed by ''''
lines terminated by '\n'
(dept, cnum, `name`, units, max_enroll, prereq, instruct, dr, sem_offered, year_offered);

-- ECON DEPT
load data local infile 'tsv_files/econ_courses.tsv'
into table courses 
fields terminated by '\t' 
enclosed by ''''
lines terminated by '\n'
(dept, cnum, `name`, units, max_enroll, prereq, instruct, dr, sem_offered, year_offered);

-- FRENCH DEPT
load data local infile 'tsv_files/french_courses.tsv'
into table courses 
fields terminated by '\t' 
enclosed by ''''
lines terminated by '\n'
(dept, cnum, `name`, units, max_enroll, prereq, instruct, dr, sem_offered, year_offered);
