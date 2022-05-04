--insert data using CSV files
load data local infile 'tsv_files/11_courses.tsv'
into table courses 
fields terminated by '\t' 
enclosed by ''''
lines terminated by '\n'
(dept, cnum, `name`, units, max_enroll, prereq, instruct, dr, sem_offered, year_offered);

load data local infile 'tsv_files/12_courses.tsv'
into table courses 
fields terminated by '\t' 
enclosed by ''''
lines terminated by '\n'
(dept, cnum, `name`, units, max_enroll, prereq, instruct, dr, sem_offered, year_offered);

load data local infile 'tsv_files/20_courses.tsv'
into table courses 
fields terminated by '\t' 
enclosed by ''''
lines terminated by '\n'
(dept, cnum, `name`, units, max_enroll, prereq, instruct, dr, sem_offered, year_offered);

load data local infile 'tsv_files/24_courses.tsv'
into table courses 
fields terminated by '\t' 
enclosed by ''''
lines terminated by '\n'
(dept, cnum, `name`, units, max_enroll, prereq, instruct, dr, sem_offered, year_offered);

load data local infile 'tsv_files/28_courses.tsv'
into table courses 
fields terminated by '\t' 
enclosed by ''''
lines terminated by '\n'
(dept, cnum, `name`, units, max_enroll, prereq, instruct, dr, sem_offered, year_offered);

load data local infile 'tsv_files/29_courses.tsv'
into table courses 
fields terminated by '\t' 
enclosed by ''''
lines terminated by '\n'
(dept, cnum, `name`, units, max_enroll, prereq, instruct, dr, sem_offered, year_offered);

load data local infile 'tsv_files/44_courses.tsv'
into table courses 
fields terminated by '\t' 
enclosed by ''''
lines terminated by '\n'
(dept, cnum, `name`, units, max_enroll, prereq, instruct, dr, sem_offered, year_offered);

load data local infile 'tsv_files/45_courses.tsv'
into table courses 
fields terminated by '\t' 
enclosed by ''''
lines terminated by '\n'
(dept, cnum, `name`, units, max_enroll, prereq, instruct, dr, sem_offered, year_offered);

load data local infile 'tsv_files/52_courses.tsv'
into table courses 
fields terminated by '\t' 
enclosed by ''''
lines terminated by '\n'
(dept, cnum, `name`, units, max_enroll, prereq, instruct, dr, sem_offered, year_offered);

load data local infile 'tsv_files/61_courses.tsv'
into table courses 
fields terminated by '\t' 
enclosed by ''''
lines terminated by '\n'
(dept, cnum, `name`, units, max_enroll, prereq, instruct, dr, sem_offered, year_offered);