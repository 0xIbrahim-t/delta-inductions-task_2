#!/bin/bash

echo "INSERT INTO web_users (rollnumber, username, password, usertype, doamin_1, domain_2, domain_3) Values ("none", "core", "1234567890", "core", "none", "none", "none");" >> db/init.sql

while read line; do
	mentee=$(echo "$line" | awk '{print $1}')
 	rollnumber=$(echo "$line" | awk '{print $2}')
	rollnumber="${rollnumber//[$'\n\r\t ']/}"
	echo "create table ${mentee}_task_submitted (Task_number INT, Sysad VARCHAR(3), Web VARCHAR(3), App VARCHAR(3));" >> db/init.sql
	echo "INSERT INTO ${mentee}_task_submitted (Task_number, Sysad, Web, App) Values (1, "n", "n", "n");" >> db/init.sql
	echo "INSERT INTO ${mentee}_task_submitted (Task_number, Sysad, Web, App) Values (2, "n", "n", "n");" >> db/init.sql
	echo "INSERT INTO ${mentee}_task_submitted (Task_number, Sysad, Web, App) Values (3, "n", "n", "n");" >> db/init.sql
 	echo "INSERT INTO web_users (rollnumber, username, password, usertype, doamin_1, domain_2, domain_3) Values ($rollnumber, $mentee, "1234567890", "mentee", "none", "none", "none");" >> db/init.sql
done < app/menteeDetails.txt

while read line; do
	mentor=$(echo "$line" | awk '{print $1}')
	dom=$(echo "$line" | awk '{print $2}')
 	cap=$(echo "$line" | awk '{print $3}')
  	cap="${cap//[$'\n\r\t ']/}"
	echo "INSERT INTO web_users (rollnumber, username, password, usertype, doamin_1, domain_2, domain_3) Values ($cap, $mentor, "1234567890", "mentor", $dom, "none", "none");" >> db/init.sql
done < app/mentorDetails.txt

echo "Database successfully initialized for the mysql container."
