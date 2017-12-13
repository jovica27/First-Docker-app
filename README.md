# First-Docker-app

[![Build Status](https://travis-ci.org/MilosSimic/First-Docker-app.svg?branch=master)](https://travis-ci.org/MilosSimic/First-Docker-app)

simple Docker app

Create image:
docker build -t myapp:latest .

Run container:
docker run -d -p 5000:5000 myapp

Image is pushed to dockerhub using Travis CI.

[![Dockerhub](https://www.docker.com/sites/default/files/Dockerized%20Apps_icon.png)](https://hub.docker.com/r/milossimic/simple_flask_app/)
