FROM ubuntu

SHELL ["/bin/bash", "-c"]

COPY app /scripts
COPY setup.sh .

RUN apt-get update
RUN apt-get install sudo -y
RUN apt-get install adduser -y
RUN mv /scripts/mentorDetails.txt .
RUN mv /scripts/menteeDetails.txt .
RUN chmod -R 700 /scripts/start.sh
RUN chmod -R 700 setup.sh
RUN mkdir /logs

CMD ./setup.sh
