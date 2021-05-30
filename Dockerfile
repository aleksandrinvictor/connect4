FROM python:3.8

RUN apt-get update && apt-get install -y \
    git

WORKDIR /workspaces/connect4

RUN curl -sSL https://raw.githubusercontent.com/python-poetry/poetry/master/get-poetry.py | python -

COPY ./pyproject.toml ./

ENV PATH=/root/.poetry/bin:$PATH

RUN poetry config virtualenvs.create false \
    && poetry install --quiet --remove-untracked
