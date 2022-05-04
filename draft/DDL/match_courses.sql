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

-- drop tracker column
alter table major_pairs
drop dept;