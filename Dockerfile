# python base 3.7 slim-buster
FROM python:3.7-slim-buster as base-image

# update ubuntu
RUN apt-get -y update

RUN apt-get install -y libssl-dev curl

# copy requirements file
COPY . /usr/workspace

WORKDIR /usr/workspace
RUN pip install -r requirements.txt

RUN pip install Jinja2==3.0.3

EXPOSE 5002 5005 5055
# ENTRYPOINT ["/usr/workspace/entrypoint.sh"]
