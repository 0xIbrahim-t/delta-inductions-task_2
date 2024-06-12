#!/bin/bash


sudo apt-get install apache
echo "127.0.0.1 gemini.club" >> /etc/hosts
sudo a2enmod proxy
sudo a2enmod proxy_http

echo "<VirtualHost *:80>" > /etc/apache2/sites-available/000-default.conf
echo "    ServerName gemini.club" >> /etc/apache2/sites-available/000-default.conf
echo "" >> /etc/apache2/sites-available/000-default.conf
echo "    ProxyPreserveHost On" >> /etc/apache2/sites-available/000-default.conf
echo "    ProxyPass / http://localhost:80/" >> /etc/apache2/sites-available/000-default.conf
echo "    ProxyPassReverse / http://localhost:80/" >> /etc/apache2/sites-available/000-default.conf
echo "" >> /etc/apache2/sites-available/000-default.conf
echo "    ErrorLog ${APACHE_LOG_DIR}/error.log" >> /etc/apache2/sites-available/000-default.conf
echo "    CustomLog ${APACHE_LOG_DIR}/access.log combined" >> /etc/apache2/sites-available/000-default.conf
echo "</VirtualHost>" >> /etc/apache2/sites-available/000-default.conf

sudo systemctl restart apache2
