FROM ubuntu:18.04
FROM python:3.6.9
ENV PYTHONUNBUFFERED=1

RUN apt-get -y update && apt-get install -y apt-utils && \
    apt-get install -y binutils libproj-dev gdal-bin vim gettext git

RUN mkdir /djnago_cicd
WORKDIR /djnago_cicd
ADD . /djnago_cicd

RUN pip install pipenv
RUN pip install -r requirements.txt

LABEL maintainer = "Poornima Byregowda <poornimagowda@sensehawk.com>" \
      version="1.0"

RUN export SIMPLE_SETTINGS=settings.development

RUN python manage.py migrate
CMD ["gunicorn", "--access-logfile",  "--workers",  "5",   "--worker-class" , "gevent",  "--timeout",  "1000",  "--bind",  "0.0.0.0:8080",  "sensehawk_data_vault.wsgi:application"]