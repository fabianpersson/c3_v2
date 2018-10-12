FROM python:2.7-alpine
RUN pip install --upgrade pip
RUN pip install flask
RUN pip install celery 
ADD shared/proj /home/ubuntu/proj
ADD celery-queue/data.tar.gz /home/ubuntu/
WORKDIR /home/ubuntu/
EXPOSE 5672
ENTRYPOINT celery -A proj worker  --loglevel=info

