#!/bin/bash

touch /etc/apache2/sites-available/app.conf
echo "<VirtualHost *:80>
     ServerAdmin webmaster@app
     ServerName app
     ServerAlias www.app
     DocumentRoot /core
     DirectoryIndex mentees_domain.txt
</VirtualHost>" >> /etc/apache2/sites-available/app.conf
echo "ServerName app" >> /etc/apache2/apache2.conf
service apache2 start
a2ensite app.conf
a2dissite 000-default.conf
service apache2 reload
