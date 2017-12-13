FROM alpine

RUN apk add --update \
    python \
    python-dev \
    py-pip \
    build-base

RUN pip install --upgrade pip

COPY . /app
WORKDIR /app

RUN ["/bin/pwd"]

RUN pip install -r /app/requirements.txt

EXPOSE 5000
ENTRYPOINT ["python", "app.py"]
