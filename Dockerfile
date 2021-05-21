# python base 3.7 slim-buster
FROM python:3.7-slim-buster as base-image

# update ubuntu
RUN apt-get -y update

RUN apt-get install -y libssl-dev curl

# copy requirements file
COPY . /usr/workspace

COPY ./models/GRU_128_rnn_size.tar.gz /usr/workspace/models/GRU_128_rnn_size.tar.gz

WORKDIR /usr/workspace
RUN pip install -r requirements.txt

# RUN rasa train -vv --dump-stories --force --debug

WORKDIR /usr/workspace