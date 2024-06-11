FROM ubuntu

COPY app /

RUN chmod -R 777 app/start.sh
RUN app/start.sh
RUN mkdir /logs
RUN userGen &> /logs/usergen.log
