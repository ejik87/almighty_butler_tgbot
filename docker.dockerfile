FROM python:3.11.1-slim-buster

COPY ./requirements.txt .

RUN pip install --upgrade pip && \
    pip wheel --no-cache-dir --no-deps --wheel-dir /wheels -r ./requirements.txt && \
    pip install --no-cache /wheels/*

COPY . /app
WORKDIR /
CMD python ./app/run.py