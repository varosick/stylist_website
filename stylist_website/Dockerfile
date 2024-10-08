FROM python:3.12.0-alpine

WORKDIR /stylist_website

# set environment variables
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

# install dependencies
RUN pip install --upgrade pip
COPY ./requirements.txt /stylist_website
RUN pip install -r requirements.txt

# copy project
COPY . /stylist_website