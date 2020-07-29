ARG BUILD_FROM=debian:buster-slim

FROM $BUILD_FROM


RUN apt-get update
RUN apt-get install -y python3-dev \
                       python3-gst-1.0 \
                       python3-lxml \
                       python3-pip \
                       python3-setuptools \
                       python3-wheel \
 && rm -rf /var/lib/apt/lists/*

RUN apt-get update \
 && apt-get install -y git \
 && rm -rf /var/lib/apt/lists/*

COPY requirements.txt requirements.txt

RUN pip3 install -r requirements.txt \
 && rm -rf ~/.cache/pip





