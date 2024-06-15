#!/bin/bash


while read line; do
    mentee=$(echo "$line" | awk '{print $1}')
 	  mentee_db=$mentee
  	export mentee_db
 	  python3 /scripts/start_db_1.py
  	python3 /scripts/start_db_2.py
done < ~Core/menteeDetails.txt

tail -f /dev/null
