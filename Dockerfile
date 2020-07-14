FROM ubuntu


RUN apt-get update -y
RUN apt-get install -y python3-pip python3-dev

ARG API_KEY

WORKDIR /app

COPY app/requirements.txt requirements.txt
RUN pip3 install -r requirements.txt

CMD python3 app.py
