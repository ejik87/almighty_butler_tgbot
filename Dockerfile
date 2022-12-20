FROM python:3.11.1-slim-buster

MAINTAINER Ejik87

COPY ./requirements.txt .

RUN pip install --upgrade pip && \
    pip wheel --no-cache-dir --no-deps --wheel-dir /wheels -r ./requirements.txt && \
    pip install --no-cache /wheels/*

COPY . /bot
WORKDIR /bot
CMD python run.py