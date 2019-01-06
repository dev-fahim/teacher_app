FROM python:3

ENV PYTHONBUFFERED 1
RUN mkdir /code
COPY . /code/
WORKDIR /code
RUN pwd
RUN pip install -r requirements.txt
