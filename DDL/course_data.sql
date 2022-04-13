--insert data using CSV files
use majormatch_db;

load data local infile 'tsv_files/1_courses.tsv'
into table courses 
fields terminated by '\t' 
enclosed by ''''
lines terminated by '\n'
(dept, cnum, `name`, units, max_enroll, prereq, instruct, dr, sem_offered, year_offered);

load data local infile 'tsv_files/2_courses.tsv'
into table courses 
fields terminated by '\t' 
enclosed by ''''
lines terminated by '\n'
(dept, cnum, `name`, units, max_enroll, prereq, instruct, dr, sem_offered, year_offered);

load data local infile 'tsv_files/3_courses.tsv'
into table courses 
fields terminated by '\t' 
enclosed by ''''
lines terminated by '\n'
(dept, cnum, `name`, units, max_enroll, prereq, instruct, dr, sem_offered, year_offered);

load data local infile 'tsv_files/4_courses.tsv'
into table courses 
fields terminated by '\t' 
enclosed by ''''
lines terminated by '\n'
(dept, cnum, `name`, units, max_enroll, prereq, instruct, dr, sem_offered, year_offered);

load data local infile 'tsv_files/5_courses.tsv'
into table courses 
fields terminated by '\t' 
enclosed by ''''
lines terminated by '\n'
(dept, cnum, `name`, units, max_enroll, prereq, instruct, dr, sem_offered, year_offered);

-- load data local infile 'tsv_files/6_courses.tsv'
-- into table courses 
-- fields terminated by '\t' 
-- enclosed by ''''
-- lines terminated by '\n'
-- (dept, cnum, `name`, units, max_enroll, prereq, instruct, dr, sem_offered, year_offered);

load data local infile 'tsv_files/7_courses.tsv'
into table courses 
fields terminated by '\t' 
enclosed by ''''
lines terminated by '\n'
(dept, cnum, `name`, units, max_enroll, prereq, instruct, dr, sem_offered, year_offered);


load data local infile 'tsv_files/8_courses.tsv'
into table courses 
fields terminated by '\t' 
enclosed by ''''
lines terminated by '\n'
(dept, cnum, `name`, units, max_enroll, prereq, instruct, dr, sem_offered, year_offered);

load data local infile 'tsv_files/9_courses.tsv'
into table courses 
fields terminated by '\t' 
enclosed by ''''
lines terminated by '\n'
(dept, cnum, `name`, units, max_enroll, prereq, instruct, dr, sem_offered, year_offered);

load data local infile 'tsv_files/10_courses.tsv'
into table courses 
fields terminated by '\t' 
enclosed by ''''
lines terminated by '\n'
(dept, cnum, `name`, units, max_enroll, prereq, instruct, dr, sem_offered, year_offered);

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

-- load data local infile 'tsv_files/13_courses.tsv'
-- into table courses 
-- fields terminated by '\t' 
-- enclosed by ''''
-- lines terminated by '\n'
-- (dept, cnum, `name`, units, max_enroll, prereq, instruct, dr, sem_offered, year_offered);

load data local infile 'tsv_files/14_courses.tsv'
into table courses 
fields terminated by '\t' 
enclosed by ''''
lines terminated by '\n'
(dept, cnum, `name`, units, max_enroll, prereq, instruct, dr, sem_offered, year_offered);

load data local infile 'tsv_files/15_courses.tsv'
into table courses 
fields terminated by '\t' 
enclosed by ''''
lines terminated by '\n'
(dept, cnum, `name`, units, max_enroll, prereq, instruct, dr, sem_offered, year_offered);

load data local infile 'tsv_files/16_courses.tsv'
into table courses 
fields terminated by '\t' 
enclosed by ''''
lines terminated by '\n'
(dept, cnum, `name`, units, max_enroll, prereq, instruct, dr, sem_offered, year_offered);

load data local infile 'tsv_files/17_courses.tsv'
into table courses 
fields terminated by '\t' 
enclosed by ''''
lines terminated by '\n'
(dept, cnum, `name`, units, max_enroll, prereq, instruct, dr, sem_offered, year_offered);

load data local infile 'tsv_files/18_courses.tsv'
into table courses 
fields terminated by '\t' 
enclosed by ''''
lines terminated by '\n'
(dept, cnum, `name`, units, max_enroll, prereq, instruct, dr, sem_offered, year_offered);

-- load data local infile 'tsv_files/19_courses.tsv'
-- into table courses 
-- fields terminated by '\t' 
-- enclosed by ''''
-- lines terminated by '\n'
-- (dept, cnum, `name`, units, max_enroll, prereq, instruct, dr, sem_offered, year_offered);

load data local infile 'tsv_files/20_courses.tsv'
into table courses 
fields terminated by '\t' 
enclosed by ''''
lines terminated by '\n'
(dept, cnum, `name`, units, max_enroll, prereq, instruct, dr, sem_offered, year_offered);

load data local infile 'tsv_files/21_courses.tsv'
into table courses 
fields terminated by '\t' 
enclosed by ''''
lines terminated by '\n'
(dept, cnum, `name`, units, max_enroll, prereq, instruct, dr, sem_offered, year_offered);

load data local infile 'tsv_files/22_courses.tsv'
into table courses 
fields terminated by '\t' 
enclosed by ''''
lines terminated by '\n'
(dept, cnum, `name`, units, max_enroll, prereq, instruct, dr, sem_offered, year_offered);

-- load data local infile 'tsv_files/23_courses.tsv'
-- into table courses 
-- fields terminated by '\t' 
-- enclosed by ''''
-- lines terminated by '\n'
-- (dept, cnum, `name`, units, max_enroll, prereq, instruct, dr, sem_offered, year_offered);


load data local infile 'tsv_files/24_courses.tsv'
into table courses 
fields terminated by '\t' 
enclosed by ''''
lines terminated by '\n'
(dept, cnum, `name`, units, max_enroll, prereq, instruct, dr, sem_offered, year_offered);

load data local infile 'tsv_files/25_courses.tsv'
into table courses 
fields terminated by '\t' 
enclosed by ''''
lines terminated by '\n'
(dept, cnum, `name`, units, max_enroll, prereq, instruct, dr, sem_offered, year_offered);

load data local infile 'tsv_files/26_courses.tsv'
into table courses 
fields terminated by '\t' 
enclosed by ''''
lines terminated by '\n'
(dept, cnum, `name`, units, max_enroll, prereq, instruct, dr, sem_offered, year_offered);

load data local infile 'tsv_files/27_courses.tsv'
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

load data local infile 'tsv_files/30_courses.tsv'
into table courses 
fields terminated by '\t' 
enclosed by ''''
lines terminated by '\n'
(dept, cnum, `name`, units, max_enroll, prereq, instruct, dr, sem_offered, year_offered);

load data local infile 'tsv_files/31_courses.tsv'
into table courses 
fields terminated by '\t' 
enclosed by ''''
lines terminated by '\n'
(dept, cnum, `name`, units, max_enroll, prereq, instruct, dr, sem_offered, year_offered);
load data local infile 'tsv_files/32_courses.tsv'
into table courses 
fields terminated by '\t' 
enclosed by ''''
lines terminated by '\n'
(dept, cnum, `name`, units, max_enroll, prereq, instruct, dr, sem_offered, year_offered);

-- load data local infile 'tsv_files/33_courses.tsv'
-- into table courses 
-- fields terminated by '\t' 
-- enclosed by ''''
-- lines terminated by '\n'
-- (dept, cnum, `name`, units, max_enroll, prereq, instruct, dr, sem_offered, year_offered);

load data local infile 'tsv_files/34_courses.tsv'
into table courses 
fields terminated by '\t' 
enclosed by ''''
lines terminated by '\n'
(dept, cnum, `name`, units, max_enroll, prereq, instruct, dr, sem_offered, year_offered);

load data local infile 'tsv_files/35_courses.tsv'
into table courses 
fields terminated by '\t' 
enclosed by ''''
lines terminated by '\n'
(dept, cnum, `name`, units, max_enroll, prereq, instruct, dr, sem_offered, year_offered);

-- load data local infile 'tsv_files/36_courses.tsv'
-- into table courses 
-- fields terminated by '\t' 
-- enclosed by ''''
-- lines terminated by '\n'
-- (dept, cnum, `name`, units, max_enroll, prereq, instruct, dr, sem_offered, year_offered);

load data local infile 'tsv_files/37_courses.tsv'
into table courses 
fields terminated by '\t' 
enclosed by ''''
lines terminated by '\n'
(dept, cnum, `name`, units, max_enroll, prereq, instruct, dr, sem_offered, year_offered);

load data local infile 'tsv_files/38_courses.tsv'
into table courses 
fields terminated by '\t' 
enclosed by ''''
lines terminated by '\n'
(dept, cnum, `name`, units, max_enroll, prereq, instruct, dr, sem_offered, year_offered);
load data local infile 'tsv_files/39_courses.tsv'
into table courses 
fields terminated by '\t' 
enclosed by ''''
lines terminated by '\n'
(dept, cnum, `name`, units, max_enroll, prereq, instruct, dr, sem_offered, year_offered);


load data local infile 'tsv_files/40_courses.tsv'
into table courses 
fields terminated by '\t' 
enclosed by ''''
lines terminated by '\n'
(dept, cnum, `name`, units, max_enroll, prereq, instruct, dr, sem_offered, year_offered);

load data local infile 'tsv_files/41_courses.tsv'
into table courses 
fields terminated by '\t' 
enclosed by ''''
lines terminated by '\n'
(dept, cnum, `name`, units, max_enroll, prereq, instruct, dr, sem_offered, year_offered);

load data local infile 'tsv_files/42_courses.tsv'
into table courses 
fields terminated by '\t' 
enclosed by ''''
lines terminated by '\n'
(dept, cnum, `name`, units, max_enroll, prereq, instruct, dr, sem_offered, year_offered);

-- load data local infile 'tsv_files/43_courses.tsv'
-- into table courses 
-- fields terminated by '\t' 
-- enclosed by ''''
-- lines terminated by '\n'
-- (dept, cnum, `name`, units, max_enroll, prereq, instruct, dr, sem_offered, year_offered);

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

load data local infile 'tsv_files/46_courses.tsv'
into table courses 
fields terminated by '\t' 
enclosed by ''''
lines terminated by '\n'
(dept, cnum, `name`, units, max_enroll, prereq, instruct, dr, sem_offered, year_offered);

load data local infile 'tsv_files/47_courses.tsv'
into table courses 
fields terminated by '\t' 
enclosed by ''''
lines terminated by '\n'
(dept, cnum, `name`, units, max_enroll, prereq, instruct, dr, sem_offered, year_offered);

load data local infile 'tsv_files/48_courses.tsv'
into table courses 
fields terminated by '\t' 
enclosed by ''''
lines terminated by '\n'
(dept, cnum, `name`, units, max_enroll, prereq, instruct, dr, sem_offered, year_offered);

load data local infile 'tsv_files/49_courses.tsv'
into table courses 
fields terminated by '\t' 
enclosed by ''''
lines terminated by '\n'
(dept, cnum, `name`, units, max_enroll, prereq, instruct, dr, sem_offered, year_offered);


load data local infile 'tsv_files/50_courses.tsv'
into table courses 
fields terminated by '\t' 
enclosed by ''''
lines terminated by '\n'
(dept, cnum, `name`, units, max_enroll, prereq, instruct, dr, sem_offered, year_offered);

load data local infile 'tsv_files/51_courses.tsv'
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

load data local infile 'tsv_files/53_courses.tsv'
into table courses 
fields terminated by '\t' 
enclosed by ''''
lines terminated by '\n'
(dept, cnum, `name`, units, max_enroll, prereq, instruct, dr, sem_offered, year_offered);

load data local infile 'tsv_files/54_courses.tsv'
into table courses 
fields terminated by '\t' 
enclosed by ''''
lines terminated by '\n'
(dept, cnum, `name`, units, max_enroll, prereq, instruct, dr, sem_offered, year_offered);

load data local infile 'tsv_files/55_courses.tsv'
into table courses 
fields terminated by '\t' 
enclosed by ''''
lines terminated by '\n'
(dept, cnum, `name`, units, max_enroll, prereq, instruct, dr, sem_offered, year_offered);

load data local infile 'tsv_files/56_courses.tsv'
into table courses 
fields terminated by '\t' 
enclosed by ''''
lines terminated by '\n'
(dept, cnum, `name`, units, max_enroll, prereq, instruct, dr, sem_offered, year_offered);

load data local infile 'tsv_files/57_courses.tsv'
into table courses 
fields terminated by '\t' 
enclosed by ''''
lines terminated by '\n'
(dept, cnum, `name`, units, max_enroll, prereq, instruct, dr, sem_offered, year_offered);

load data local infile 'tsv_files/58_courses.tsv'
into table courses 
fields terminated by '\t' 
enclosed by ''''
lines terminated by '\n'
(dept, cnum, `name`, units, max_enroll, prereq, instruct, dr, sem_offered, year_offered);

load data local infile 'tsv_files/59_courses.tsv'
into table courses 
fields terminated by '\t' 
enclosed by ''''
lines terminated by '\n'
(dept, cnum, `name`, units, max_enroll, prereq, instruct, dr, sem_offered, year_offered);


load data local infile 'tsv_files/60_courses.tsv'
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

load data local infile 'tsv_files/62_courses.tsv'
into table courses 
fields terminated by '\t' 
enclosed by ''''
lines terminated by '\n'
(dept, cnum, `name`, units, max_enroll, prereq, instruct, dr, sem_offered, year_offered);

-- load data local infile 'tsv_files/63_courses.tsv'
-- into table courses 
-- fields terminated by '\t' 
-- enclosed by ''''
-- lines terminated by '\n'
-- (dept, cnum, `name`, units, max_enroll, prereq, instruct, dr, sem_offered, year_offered);

load data local infile 'tsv_files/64_courses.tsv'
into table courses 
fields terminated by '\t' 
enclosed by ''''
lines terminated by '\n'
(dept, cnum, `name`, units, max_enroll, prereq, instruct, dr, sem_offered, year_offered);

load data local infile 'tsv_files/65_courses.tsv'
into table courses 
fields terminated by '\t' 
enclosed by ''''
lines terminated by '\n'
(dept, cnum, `name`, units, max_enroll, prereq, instruct, dr, sem_offered, year_offered);