FROM python:3.11.2
ENV PYTHONUNBUFFERED 1
RUN mkdir /app
WORKDIR /app

COPY pyproject.toml poetry.lock ./
RUN apt-get clean && \
    apt-get update && \
    apt-get install -y locales build-essential python3-dev default-libmysqlclient-dev &&\
    echo ru_RU.UTF-8 UTF-8 >> /etc/locale.gen && \
    locale-gen && \
    python -m pip install poetry==1.3.1 && \
    poetry config virtualenvs.create false

RUN python -m pip install --upgrade pip && poetry install --no-root

COPY ./ /app/

EXPOSE 80
ENTRYPOINT ["/app/run.sh"]
CMD gunicorn --bind '0.0.0.0:80' b2broker.wsgi
