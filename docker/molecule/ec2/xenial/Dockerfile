FROM shadowrobot/aurora-molecule:xenial

MAINTAINER "Shadow Robot's Software Team <software@shadowrobot.com>"

LABEL Description="Ubuntu Xenial image contains Ansible, Molecule and EC2 driver" Vendor="Shadow Robot" Version="1.0"

ENV aurora_branch "master"

RUN set -x && \
    \
    echo "Install Docker using playbook to avoid installing Python 3.5" && \
    git clone --depth 1 https://github.com/shadow-robot/aurora.git -b $aurora_branch /tmp/aurora && \
    cd /tmp/aurora/ && \
    export ANSIBLE_ROLES_PATH="/tmp/aurora/ansible/roles" && \
    ansible-playbook -vvv --ask-become-pass -i ansible/inventory/local/install-software \
        ansible/playbooks/install-software.yml --extra-vars 'software=[aws-cli]' && \
    cd /root && \
    \
    echo "Clean up" && \
    apt-get clean && \
    rm -rf /var/lib/apt/lists/* /tmp/* /var/tmp/* /root/.ansible /root/.gitconfig /root/.cache
