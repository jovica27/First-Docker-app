# First-Docker-app


[![Build Status](https://travis-ci.org/MilosSimic/First-Docker-app.svg?branch=master)](https://travis-ci.org/MilosSimic/First-Docker-app) [![Built with Spacemacs](https://cdn.rawgit.com/syl20bnr/spacemacs/442d025779da2f62fc86c2082703697714db6514/assets/spacemacs-badge.svg)](http://spacemacs.org)

simple Flask app that is in Docker demonstrating how to build run and map volumes.


## Build Docker image
docker build -t myapp:latest .


## Run from local build
Run container from local build:
docker run -d -p 5000:5000 myapp

Run container with mapped volumes from local build:
docker run -d -p 5000:5000 -v path_to_log:/usr/src/app/myapp/logs myapp


## Run from Dockerhub
Run container from dockerhub:
docker run -d -p 5000:5000 milossimic/simple_flask_app

Run container from dockerhub with mapped volumes:
docker run -d -p 5000:5000 -v path_to_log:/usr/src/app/myapp/logs milossimic/simple_flask_app


## Dockerhub link
Image is pushed to dockerhub using Travis CI.
[![Dockerhub](https://www.docker.com/sites/default/files/Dockerized%20Apps_icon.png)](https://hub.docker.com/r/milossimic/simple_flask_app/)
