FROM ubuntu:xenial-20190222

MAINTAINER "Shadow Robot's Software Team <software@shadowrobot.com>"

LABEL Description="This image is used for testing empty Ubuntu Xenial deployment" Vendor="Shadow Robot" Version="1.0"

ENV DEBIAN_FRONTEND noninteractive

ENV USER testuser

RUN set -x && \
    apt-get update && \
    \
    echo "Installing sudo" && \
    apt-get install -y sudo && \
    \
    echo "Create testuser with empty password" && \
    useradd -m $USER && \
    passwd -d $USER && \
    adduser $USER sudo && \
    \
    echo "Clean up" && \
    apt-get clean && \
    rm -rf /var/lib/apt/lists/* /tmp/* /var/tmp/* /root/.ansible /root/.gitconfig /root/.cache

USER $USER
