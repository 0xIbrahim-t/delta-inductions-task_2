# delta-inductions-task_2

### Please run this before starting the servers, to set up the database, and run it only once
> ./setup_init_db.sh

### to start the server
> docker-compose up -d

### setup the conf to make the file accessible locally using gemini.club instead of default localhost and to start the cronjob for database backups
> ./setup_conf.sh
##### warning: pls do not run this more than once, please set all the changes done by the bash file to the default, before running this for the second time. Also do not run this from another directory.



## You can see the server PHPMyAdmin running on post 8080 and web app running in port 5000, and the menteesDomain.txt in gemini.club
