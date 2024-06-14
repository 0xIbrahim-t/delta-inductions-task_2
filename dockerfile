FROM ubuntu

SHELL ["/bin/bash", "-c"]

COPY app /scripts

RUN apt-get update
RUN apt-get install sudo -y
RUN apt-get install adduser -y
RUN apt-get install -y apache2
RUN mv /scripts/mentorDetails.txt .
RUN mv /scripts/menteeDetails.txt .
RUN chmod -R 700 /scripts/start.sh
RUN mkdir /logs
RUN /scripts/start.sh
RUN mv /scripts/userGen.sh .
RUN ./userGen.sh
RUN service apache2 start

EXPOSE 80

CMD ["tail", "-f", "/dev/null"]
