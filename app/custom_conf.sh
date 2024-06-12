#!/bin/bash

echo "<VirtualHost *:80>" > /etc/apache2/sites-available/000-default.conf
echo "    DocumentRoot ~Core/mentees_domain.txt" >> /etc/apache2/sites-available/000-default.conf
echo "" >> /etc/apache2/sites-available/000-default.conf
echo "    <Directory ~Core/mentees_domain.txt>" >> /etc/apache2/sites-available/000-default.conf
echo "        Options Indexes FollowSymLinks" >> /etc/apache2/sites-available/000-default.conf
echo "        AllowOverride None" >> /etc/apache2/sites-available/000-default.conf
echo "        Require all granted" >> /etc/apache2/sites-available/000-default.conf
echo "    </Directory>" >> /etc/apache2/sites-available/000-default.conf
echo "" >> /etc/apache2/sites-available/000-default.conf
echo "    ErrorLog ${APACHE_LOG_DIR}/error.log" >> /etc/apache2/sites-available/000-default.conf
echo "    CustomLog ${APACHE_LOG_DIR}/access.log combined" >> /etc/apache2/sites-available/000-default.conf
echo "</VirtualHost>" >> /etc/apache2/sites-available/000-default.conf
