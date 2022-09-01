FROM python:3.9.13

RUN sed -i 's/archive.ubuntu.com/ftp.daum.net/g' /etc/apt/sources.list
RUN sed -i 's/security.ubuntu.com/ftp.daum.net/g' /etc/apt/sources.list

RUN set -xe \ 
    && apt-get update -y  \
    && apt-get upgrade -y

RUN pip3 install --upgrade pip setuptools wheel poetry

RUN apt-get install --no-install-recommends -y \
        build-essential \
        cmake \
        git \
        curl \
        wget \
        ca-certificates \
        libjpeg-dev \
        libpng-dev \
        ffmpeg \
        libsm6 \
        libxext6 \
        libgl1-mesa-glx

WORKDIR "/app"

COPY . .

RUN poetry install

CMD ["poetry","run","streamlit","run","Home.py", "--logger.level=debug"]