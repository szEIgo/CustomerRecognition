FROM ubuntu:latest
MAINTAINER AllUnite A/S "ala@allunite.com"
RUN apt-get update -y
RUN apt-get install -y python3-pip python3-dev build-essential
ADD consumer_task/. /app/consumer_task
ADD config.py /app
WORKDIR /app/consumer_task

run pip3 install -U pip
RUN pip3 install -r requirements.txt

ENTRYPOINT ["python3"]
CMD ["consumer.py"]






