# delta-inductions-task_2

## to start the server
> docker build -t task-2_image .
> docker run -d -p 80:80 --name task-2_container task-2_image

## setup the conf to make the file accessible locally using gemini.club instead of default localhost
> setup_conf.sh
