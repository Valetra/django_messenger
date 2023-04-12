FROM python:3.12.0a6-alpine3.17
ENV PYTHONUNBUFFERED 1
ENV LIBRARY_PATH=/lib:/usr/lib
WORKDIR /app
ADD . /app
RUN apk add build-base libffi-dev
RUN pip install -r requirements.txt
RUN python manage.py migrate