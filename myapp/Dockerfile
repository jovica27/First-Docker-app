FROM alpine

RUN apk add --update \
    python \
    python-dev \
    py-pip \
    build-base

RUN pip install --upgrade pip

COPY . /code
WORKDIR /code

RUN pip install -r requirements.txt

EXPOSE 5000
ENTRYPOINT ["python", "app.py"]