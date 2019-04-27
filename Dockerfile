FROM python:latest
MAINTAINER Stephan Bartkowiak - stephan@ecobonuz.com

RUN mkdir /apps
WORKDIR /apps

ADD . .

RUN pip install -r requirements.txt

EXPOSE 3000

CMD python ./api-start.py
