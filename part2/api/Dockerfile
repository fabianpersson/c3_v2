FROM python:2.7-alpine
RUN pip install --upgrade pip
RUN pip install flask
RUN pip install celery 
ADD shared/proj /home/ubuntu/proj
ADD api/app.py /home/ubuntu/
ADD data/data-full.tar.gz /home/ubuntu
RUN ls /home/ubuntu/
WORKDIR /home/ubuntu/
EXPOSE 5000
#RUN celery -A proj worker -l info 
ENTRYPOINT python app.py

