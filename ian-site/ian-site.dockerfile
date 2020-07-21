#dockerfile

FROM ubuntu:latest

RUN apt-get update

RUN apt-get install -y python3.8

RUN apt install -y python3-pip

RUN pip3 install flask

RUN mkdir /app

WORKDIR /app

COPY /Websites-code/Ian-site/site.py /app

CMD py site.py

