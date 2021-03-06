FROM ubuntu:xenial-20190222

MAINTAINER "Shadow Robot's Software Team <software@shadowrobot.com>"

LABEL Description="Ubuntu Xenial image contains Ansible and Molecule" Vendor="Shadow Robot" Version="1.0"

ENV DEBIAN_FRONTEND noninteractive

ENV PYTHONPATH "/usr/local/lib/python3.7/site-packages"

ENV aurora_branch "master"

RUN set -x && \
    apt-get update && \
    \
    echo "Installing git, sudo and sshpass" && \
    apt-get install -y \
        git \
        sudo \
        sshpass && \
    \
    echo "Installing wget" && \
    apt-get install -y --no-install-recommends ca-certificates wget && \
    \
    echo "Installing unarchiver" && \
    apt-get install -y xz-utils && \
    \
    echo "Installing Python 3.7 for Ubuntu Xenial from source code" && \
    apt-get install -y \
        build-essential \
        libssl-dev \
        libffi-dev \
        libxml2-dev \
        libxslt1-dev \
        zlib1g-dev && \
    mkdir -p /tmp/python && \
    cd /tmp/python && \
    wget https://www.python.org/ftp/python/3.7.0/Python-3.7.0.tar.xz && \
    tar xf ./Python-3.7.0.tar.xz && \
    cd /tmp/python/Python-3.7.0 && \
    ./configure && \
    make && \
    make install && \
    \
    echo "Installing Pip for Python 3.7" && \
    cd /tmp && \
    wget "https://bootstrap.pypa.io/get-pip.py" && \
    python3.7 ./get-pip.py && \
    \
    echo "Cloning Aurora" && \
    cd /tmp && \
    git clone --depth 1 https://github.com/shadow-robot/aurora.git -b $aurora_branch && \
    \
    echo "Installing molecule" && \
    pip3.7 install -r /tmp/aurora/ansible/data/molecule/requirements.txt && \
    \
    echo "Clean up" && \
    apt-get clean && \
    rm -rf /var/lib/apt/lists/* /tmp/* /var/tmp/* /root/.ansible /root/.gitconfig /root/.cache
