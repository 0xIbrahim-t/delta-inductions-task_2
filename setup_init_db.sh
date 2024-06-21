#!/bin/bash

while read line; do
	mentee=$(echo "$line" | awk '{print $1}')
  echo "create table ${mentee}_task_submitted (Task_number INT, Sysad VARCHAR(3), Web VARCHAR(3), App VARCHAR(3));" >> db/init.sql
  echo "INSERT INTO ${mentee}_task_submitted (Task_number, Sysad, Web, App) Values (1, "n", "n", "n");" >> db/init.sql
  echo "INSERT INTO ${mentee}_task_submitted (Task_number, Sysad, Web, App) Values (2, "n", "n", "n");" >> db/init.sql
  echo "INSERT INTO ${mentee}_task_submitted (Task_number, Sysad, Web, App) Values (3, "n", "n", "n");" >> db/init.sql
done < app/menteeDetails.txt
