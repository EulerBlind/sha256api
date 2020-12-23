FROM tiangolo/uvicorn-gunicorn:python3.8-alpine3.10
RUN sed -i 's/dl-cdn.alpinelinux.org/mirrors.aliyun.com/g' /etc/apk/repositories

RUN apk update && apk add --no-cache add gcc musl-dev python3-dev libffi-dev openssl-dev
RUN pip install --upgrade pip -i https://pypi.doubanio.com/simple
RUN pip install poetry -i https://pypi.doubanio.com/simple
COPY pyproject.toml pyproject.toml
COPY poetry.lock poetry.lock

RUN mkdir -p /root/.poetry/env && source $HOME/.poetry/env && poetry config virtualenvs.create false && poetry install --no-dev --no-ansi --no-root

RUN apk del gcc libffi-dev

COPY ./sha256_api.py /app/

