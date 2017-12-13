FROM alpine

RUN apk add --update \
    python \
    python-dev \
    py-pip \
    build-base

RUN pip install --upgrade pip

COPY . /app
WORKDIR /app

RUN pip install -r Flask

EXPOSE 5000
ENTRYPOINT ["python", "app.py"]
