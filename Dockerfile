FROM python:3.10.2-slim-bullseye

ENV PIP_DISABLE_PIP_VERSION_CHECK 1
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

RUN  adduser user
USER user
WORKDIR /app
COPY requirements.txt .
RUN pip install -r requirements.txt

COPY . .