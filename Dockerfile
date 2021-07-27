FROM tiangolo/uvicorn-gunicorn:python3.8

LABEL maintainer="Hyungyo Seo <hyunbridge@gmail.com>"

RUN pip install fastapi uvicorn hcskr

COPY ./app /app