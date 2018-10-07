# ML-SSO-validation-code
[![FOSSA Status](https://app.fossa.io/api/projects/git%2Bgithub.com%2Fjackey8616%2FML-SSO-validation-code.svg?type=shield)](https://app.fossa.io/projects/git%2Bgithub.com%2Fjackey8616%2FML-SSO-validation-code?ref=badge_shield)

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

### Predict
In run.py have some example usage to interact with service.
```sh
$ pip3 install -r requirements-run.txt
$ python3 run.py
```


## License
[![FOSSA Status](https://app.fossa.io/api/projects/git%2Bgithub.com%2Fjackey8616%2FML-SSO-validation-code.svg?type=large)](https://app.fossa.io/projects/git%2Bgithub.com%2Fjackey8616%2FML-SSO-validation-code?ref=badge_large)