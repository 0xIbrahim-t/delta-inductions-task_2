#!/bin/bash

minute=$(date +%M)
hour=$(date +%H)
day=$(date +%d)
weekday=$(date +%u)
month=$(date +%m)

if { [ "$minute" -eq 3 ] && [ "$hour" -ge 5 ] && [ "$hour" -le 8 ]; } || { [ "$minute" -eq 3 ] && [ "$hour" -eq 15 ] && [ "$day" -eq 1 ]; } || { [ "$minute" -eq 3 ] && [ "$hour" -eq 15 ] && [ "$weekday" -eq 2 ] && [ "$month" -ge 1 ] && [ "$month" -le 7 ]; }; then
    docker exec db_container /usr/bin/mysqldump -u username --no-tablespaces --password=password Task_db > db/backup.sql
fi
