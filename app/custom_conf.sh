#!/bin/bash

touch /etc/apache2/sites-available/app.conf
cp ~Core/mentees_domain.txt /var/www/
chmod -R 777 /var/www/gemini/mentees_domain.txt
echo "<VirtualHost *:80>
     ServerAdmin webmaster@app
     ServerName app
     ServerAlias www.app
     DocumentRoot /var/www/gemini
     DirectoryIndex mentees_domain.txt
</VirtualHost>" >> /etc/apache2/sites-available/app.conf
echo "ServerName app" >> /etc/apache2/apache2.conf
service apache2 start
a2ensite app.conf
a2dissite 000-default.conf
service apache2 reload
