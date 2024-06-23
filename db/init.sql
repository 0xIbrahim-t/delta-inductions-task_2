CREATE USER 'user' IDENTIFIED BY 'pass';
GRANT SELECT ON Task_db.* TO 'user';
FLUSH PRIVILEGES;

USE Task_db;

create table web_users (rollnumber VARCHAR(20), username VARCHAR(20), password VARCHAR(20), usertype VARCHAR(20), doamin_1 VARCHAR(20), domain_2 VARCHAR(20), domain_3 VARCHAR(20), allocated_mentor VARCHAR(20));




