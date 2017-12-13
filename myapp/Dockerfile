FROM alpine

MAINTANER Your Name "milossimicsimo@gmail.com"

RUN apk add --update \
    python \
    python-dev \
    py-pip \
    build-base

RUN pip install --upgrade pip
RUN pip install -r requirements.txt

COPY . /code
WORKDIR /code

EXPOSE 5000
ENTRYPOINT ["python", "app.py"]