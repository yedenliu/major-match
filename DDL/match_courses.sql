-- add tracker column
alter table major_pairs
add dept varchar(10);

-- CS DEPT
insert into major_pairs(cid, dept)
select cid, dept from courses
where dept = 'CS';

UPDATE major_pairs
SET dept_id = 20
WHERE dept = 'CS';

-- CHEM DEPT
insert into major_pairs(cid, dept)
select cid, dept from courses
where dept = 'CHEM';

UPDATE major_pairs
SET dept_id = 12
WHERE dept = 'CHEM';

-- CHPH DEPT
insert into major_pairs(cid, dept)
select cid, dept from courses
where dept = 'CHPH';

UPDATE major_pairs
SET dept_id = 11
WHERE dept = 'CHPH';

-- ECON DEPT
insert into major_pairs(cid, dept)
select cid, dept from courses
where dept = 'ECON';

UPDATE major_pairs
SET dept_id = 24
WHERE dept = 'ECON';

-- FRENCH DEPT
insert into major_pairs(cid, dept)
select cid, dept from courses
where dept = 'FRST';

UPDATE major_pairs
SET dept_id = 29
WHERE dept = 'FRST';

-- FRENCH 2 DEPT
insert into major_pairs(cid, dept)
select cid, dept from courses
where dept = 'FREN';

UPDATE major_pairs
SET dept_id = 28
WHERE dept = 'FREN';

-- STAT DEPT
insert into major_pairs(cid, dept)
select cid, dept from courses
where dept = 'STAT';

UPDATE major_pairs
SET dept_id = 44
WHERE dept = 'STAT';

-- MAS DEPT
insert into major_pairs(cid, dept)
select cid, dept from courses
where dept = 'MAS';

UPDATE major_pairs
SET dept_id = 45
WHERE dept = 'MAS';

-- PHYS DEPT
insert into major_pairs(cid, dept)
select cid, dept from courses
where dept = 'PHYS';

UPDATE major_pairs
SET dept_id = 52
WHERE dept = 'PHYS';

-- MATH DEPT
insert into major_pairs(cid, dept)
select cid, dept from courses
where dept = 'MATH';

UPDATE major_pairs
SET dept_id = 61
WHERE dept = 'MATH';

-- drop tracker column
alter table major_pairs
drop dept;