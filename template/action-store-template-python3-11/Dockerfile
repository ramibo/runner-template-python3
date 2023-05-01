ARG BUILDPLATFORM=linux/amd64
ARG BUILDTAG=3-alpine
FROM --platform=${TARGETPLATFORM:-linux/amd64} ghcr.io/openfaas/of-watchdog:0.9.10 as watchdog

FROM --platform=$BUILDPLATFORM python:3.11-slim-buster as prod

COPY --from=watchdog /fwatchdog /usr/bin/fwatchdog

RUN chmod +x /usr/bin/fwatchdog

RUN addgroup --system user && adduser --system user --ingroup user

USER user

ENV PATH=$PATH:/home/user/.local/bin

WORKDIR /home/user/app

RUN pip install --no-cache poetry
RUN poetry config --no-cache

COPY function/pyproject.toml .
COPY function/poetry.lock .
COPY function/handler handler


RUN poetry install --no-root --without dev

RUN poetry build --format=wheel
RUN poetry export --only main -f requirements.txt --without-hashes --output requirements.txt

RUN pip install --no-cache -r requirements.txt dist/*.whl -r handler/action_store/requirements.txt --user

ARG FUNCNAME=''
ENV FUNCNAME=$FUNCNAME

ENV fprocess="python -m handler.server.api"
ENV cgi_headers="true"
ENV mode="http"
ENV upstream_url="http://127.0.0.1:8000"
ENV write_debug="false"

HEALTHCHECK --interval=5s CMD [ -e /tmp/.lock ] || exit 1

CMD ["fwatchdog"]
