FROM python:2.7-alpine
RUN pip install --upgrade pip
RUN pip install flask
RUN pip install celery 
ADD shared/proj /home/ubuntu/proj
ADD data/data-full.tar.gz /home/ubuntu
WORKDIR /home/ubuntu/
EXPOSE 5672
#RUN celery -A proj worker -l info 
ENTRYPOINT celery -A proj worker  --loglevel=info --without-gossip --without-heartbeat

