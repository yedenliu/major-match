--insert data using CSV files
use majormatch_db;

load data local infile 'all_courses.tsv'
into table courses 
fields terminated by '\t' 
enclosed by ''''
lines terminated by '\n'
(dept, cnum, `name`, units, max_enroll, prereq, instruct, dr, sem_offered, year_offered);
