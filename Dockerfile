FROM python:latest
MAINTAINER Stephan Bartkowiak - stephan@ecobonuz.com

RUN mkdir /apps
WORKDIR /apps

ADD . .

RUN pip install -r requirements.txt

CMD python ./apistart.py
