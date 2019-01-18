# ML-SSO-validation-code
[![Docker Build Status](https://img.shields.io/docker/build/clooooode/ml-sso-validation-code.svg?style=popout)](https://hub.docker.com/r/clooooode/ml-sso-validation-code/builds/) [![MicroBadger Size](https://img.shields.io/microbadger/image-size/clooooode/ml-sso-validation-code.svg?style=popout)](https://hub.docker.com/r/clooooode/ml-sso-validation-code/tags/)  
For SOME SCHOOL's SSO validation code recognition.


## Usage
Before use, you have to host the service first.  
Here provide local and docker way to host it.
### With machine
```sh
$ pip3 install -r requirements-model.txt
$ python3 app.py
```
### With Docker
```sh
build image:
$ docker build -t sso-validate-flask-server:latest .
run image:
$ docker run -ti -d -p 127.0.0.1:5000:5000 --restart always sso-validate-flask-server:latest 
```
### With Docker-compose
```sh
Start container:
$ docker-compose up -d
Stop container:
$ docker-compose down
View logs:
$ docker-compose logs -f
```

### Predict
In run.py have some example usage to interact with service.
```sh
$ pip3 install -r requirements-run.txt
$ python3 run.py
```
