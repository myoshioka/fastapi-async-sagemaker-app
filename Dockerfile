FROM python:3.8-slim

WORKDIR /code
COPY poetry.lock pyproject.toml /code/

# System deps:
RUN pip install poetry

# Project initialization:
RUN poetry config virtualenvs.create false \
&& poetry install

COPY . /code
