#!/bin/bash


echo "127.0.0.1 gemini.club" >> /etc/hosts

echo "* * * * * cronjob_db.sh" | crontab -

