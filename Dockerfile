FROM ubuntu:18.04

MAINTAINER Ishan Bhatt <ishan_bhatt@hotmail.com>

RUN mkdir Trivago-Task
COPY requirements.txt Trivago-Task/requirements.txt

RUN apt-get update && apt-get install -y \
    python3-pip \
	build-essential \
	libssl-dev \
	libsasl2-dev \
	libldap2-dev \
	libffi-dev \
	python3-dev \
	libcurl4-openssl-dev \
	libssl-dev \
	cmake \
	pkg-config

RUN pip3 install -r Trivago-Task/requirements.txt
COPY . Trivago-Task

WORKDIR Trivago-Task

ENTRYPOINT ["/bin/bash", "gunicorn.sh"]