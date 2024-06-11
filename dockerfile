FROM ubuntu

COPY app /scripts

RUN chmod -R 777 scripts/start.sh
RUN mkdir /logs
RUN scripts/start.sh &> /logs/start.log
RUN cd -
RUN userGen &> /logs/usergen.log
