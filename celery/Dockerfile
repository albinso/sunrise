FROM python:3.6
ENV PYTHONUNBUFFERED 1
RUN mkdir /sunrise
WORKDIR /sunrise
COPY requirements.txt /sunrise/
RUN pip install -r requirements.txt
RUN wget -q -O - https://apt.mopidy.com/mopidy.gpg | apt-key add -
RUN wget -q -O /etc/apt/sources.list.d/mopidy.list https://apt.mopidy.com/buster.list
RUN apt-get update
RUN apt-get -y install mopidy
RUN apt-get -y install mpc
COPY . /sunrise/
#RUN python manage.py makemigrations
#RUN python manage.py migrate
