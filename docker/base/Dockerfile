FROM python:3.4

ENV LANG C.UTF-8

ARG project_dir=/usr/src/app/

ADD * $project_dir
WORKDIR $project_dir

RUN pip install -r requirements.txt
