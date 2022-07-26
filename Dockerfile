FROM python:3.8-slim-buster

RUN apt update && apt upgrade -y
RUN apt install git -y
COPY requirements.txt /requirements.txt

RUN cd /
RUN pip3 install -U pip && pip3 install -U -r requirements.txt
RUN mkdir /My-k-drama-bot-source-code
WORKDIR /My-k-drama-bot-source-code
COPY start.sh /start.sh
CMD ["/bin/bash", "/start.sh"]
