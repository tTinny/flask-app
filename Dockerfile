FROM ubuntu:18.10
RUN apt-get update
RUN apt-get install -y apt-utils
RUN apt-get install -y python3 python3-dev python3-pip nginx
RUN pip3 install uwsgi
COPY ./flask ./app
WORKDIR ./app
RUN pip3 install -r requirements.txt
CMD python3 app.py
