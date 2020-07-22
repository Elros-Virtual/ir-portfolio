#dockerfile

FROM ubuntu:latest

RUN apt-get update

RUN apt-get install -y python3.8

RUN apt install -y python3-pip

RUN pip install flask

RUN mkdir /app

WORKDIR /app

COPY /Websites-code /app

CMD python site.py

