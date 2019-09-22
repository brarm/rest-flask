#!/bin/bash

sudo apt-get update -yq
sudo apt-get install -yq make build-essential libssl-dev zlib1g-dev libbz2-dev \
libreadline-dev libsqlite3-dev wget curl llvm libncurses5-dev libncursesw5-dev \
xz-utils tk-dev libffi-dev liblzma-dev python-openssl git

# ref - https://github.com/pyenv/pyenv-installer
curl https://pyenv.run | bash
pyenv update

echo 'export PATH="$HOME/.pyenv/bin:$PATH"' >> ~/.bashrc
echo 'eval "$(pyenv init -)"' >> ~/.bashrc
echo 'eval "$(pyenv virtualenv-init -)"' >> ~/.bashrc
source ~/.bash

# installs python 3.7.4 to ~/.pyenv
pyenv install 3.7.4

# create a virtualenv for the project
pyenv virtualenv 3.7.4 rest-flask
pyenv activate rest-flask

# install the requirements to the venv
pip install flask
pip install requests