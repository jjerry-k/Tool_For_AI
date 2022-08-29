FROM ubuntu:20.04

RUN sed -i 's/archive.ubuntu.com/ftp.daum.net/g' /etc/apt/sources.list
RUN sed -i 's/security.ubuntu.com/ftp.daum.net/g' /etc/apt/sources.list

RUN set -xe \ 
    && apt-get update -y  \
    && apt-get upgrade -y

RUN add-apt-repository ppa:deadsnakes/ppa

RUN apt install -y python3.9

RUN curl https://bootstrap.pypa.io/get-pip.py -o get-pip.py \
    && python3.9 get-pip.py

RUN pip3 install --upgrade pip setuptools wheel poetry

RUN DEBIAN_FRONTEND=noninteractive TZ=Asia/Seoul apt-get -y install tzdata

RUN apt-get install --no-install-recommends -y \
        build-essential \
        cmake \
        git \
        curl \
        wget \
        ca-certificates \
        libjpeg-dev \
        libpng-dev

WORKDIR "/app"

COPY . .

RUN poetry update

RUN poetry install

CMD ["poetry","run","streamlit","run","Main.py"]