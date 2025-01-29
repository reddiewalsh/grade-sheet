FROM mcr.microsoft.com/devcontainers/python:1.2-3.11-bookworm

RUN apt update && apt -y upgrade

RUN apt -y install neovim

RUN pip install pipenv

# COPY ../Pipfile* .

# RUN pipenv install --system --dev

COPY .. .

CMD [ "bash" ]