FROM centos:centos7
MAINTAINER Holmes Team <holmes@holmesdoc.com>

RUN yum install -y epel-release
RUN yum install -y python-pip

ADD     /requirements.txt /code/requirements.txt
WORKDIR /code
RUN     pip install -r requirements.txt
ADD     code /code

RUN mkdir /data

ENTRYPOINT ["python", "app.py"]