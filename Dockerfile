FROM python:3.10.4-alpine

WORKDIR /app

ENV PYTHONDONTWRITEBYTECODE 1

ENV PYTHONUNBUFFERED 1

RUN apk update \
    && apk add postgresql-dev gcc python3-dev musl-dev
    
RUN pip install --upgrade pip 
COPY ./requirements.txt /app/requirements.txt

RUN pip3 install -r requirements.txt

COPY . /app/
