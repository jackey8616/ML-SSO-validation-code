FROM python:3

MAINTAINER Clooooode "jackey8616@gmail.com"

COPY . app

WORKDIR /app

RUN pip3 install -r requirements.txt

ENTRYPOINT ["python3"]

CMD ["app.py"]
