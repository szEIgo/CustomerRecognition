FROM ubuntu:latest
MAINTAINER AllUnite A/S "ala@allunite.com"
RUN apt-get update -y
RUN apt-get install -y python3-pip python3-dev build-essential
ADD webapp/. /app/webapp
ADD producer_task/. /app/producer_task
ADD config.py /app
#RUN ["/bin/bash", "-c", "cd app/producer_task && ls"]
WORKDIR /app/webapp
run pip3 install -U pip

RUN pip3 install -r requirements.txt
ENTRYPOINT ["python3"]
CMD ["webserver.py"]


