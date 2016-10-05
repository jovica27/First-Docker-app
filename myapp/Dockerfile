FROM alpine

RUN apk add --update \
    python \
    python-dev \
    py-pip \
    build-base

RUN pip install --upgrade pip

RUN pip install Flask

COPY . /code

WORKDIR /code

CMD python app.py