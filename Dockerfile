#Image Base
FROM python:3.8.2-buster

EXPOSE 8000

#Copy Source Code
COPY . /app

#Check
#RUN ls -l

#Check II
#RUN ls ./app -l

WORKDIR /app

#Update packages
#RUN apt-get -y update

#Install Dependencies
RUN pip install -r requirements.txt

#RUN python ./app/manage.py runserver