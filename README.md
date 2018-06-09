# ML-SSO-validation-code
For SOME SCHOOL's SSO validation code recognition.

## Docker
### Build Image
```sh
docker build -t sso-validate-flask-server:latest .
```
### Run Image
```sh
docker run -ti -d -p 127.0.0.1:5000:5000 --restart always sso-validate-flask-server:latest 
```
