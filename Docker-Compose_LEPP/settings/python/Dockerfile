FROM python:3.9
MAINTAINER ARO7I <ARO7I@icloud.com>

ENV PYTHONDONTWRITEYTECODE 1
ENV PYTHONUNBUFFERED 1

RUN pip install -U pip
COPY requirements.txt /requirements.txt
RUN pip install -r /requirements.txt
