FROM python:3.12-slim

ENV TZ=Europe/Lisbon
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

RUN mkdir -p /var/www/healthcare.com/

WORKDIR /usr/src

COPY --from=ghcr.io/astral-sh/uv:latest /uv /uvx /bin/
COPY src /usr/src
COPY pyproject.toml /usr/src/pyproject.toml
COPY uv.lock /usr/src/uv.lock

RUN uv sync --frozen --no-cache
RUN chmod 777 /usr/src/app/healthcare/entrypoint.sh

WORKDIR /usr/src/app/healthcare
