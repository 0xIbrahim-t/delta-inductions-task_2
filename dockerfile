FROM ubuntu

COPY app /scripts

RUN apt-get update
RUN apt-get install sudo
RUN apt-get install adduser
RUN chmod -R 777 /scripts/start.sh
RUN mkdir /logs
RUN /scripts/start.sh &> /logs/start.log
RUN userGen &> /logs/usergen.log
