FROM python:3.10-alpine

WORKDIR /
RUN apk update && apk upgrade
COPY requirements.txt requirements.txt
RUN pip3 install -r requirements.txt

COPY app.py /
ENV FLASK_APP=app.py
ENV FLASK_RUN_HOST=0.0.0.0
EXPOSE 5000

