FROM python:3.9

WORKDIR /app-products/

ENV PYTHONUNBUFFERED 1

RUN apt-get update \
    && apt-get install -y gcc python3-dev \
    && apt-get -y install libffi-dev \
    && apt-get -y install python3-dev libpq-dev

RUN pip install --upgrade pip

COPY . /app-products

COPY requirements.txt requirements.txt 

RUN  pip install -r requirements.txt

COPY ./docker/app_start /app_start


RUN chmod +x /app_start

