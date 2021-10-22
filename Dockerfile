FROM python:3.9.7-slim-buster
WORKDIR /code
COPY requirements.txt .
RUN python -m pip install --upgrade pip
RUN pip install -r requirements.txt
COPY webapp .
