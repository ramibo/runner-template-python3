ARG BUILDPLATFORM=linux/amd64
ARG BUILDTAG=3-alpine
FROM --platform=${TARGETPLATFORM:-linux/amd64} ghcr.io/openfaas/of-watchdog:0.9.10 as watchdog

FROM --platform=$BUILDPLATFORM python:3.11-slim-buster as prod

COPY --from=watchdog /fwatchdog /usr/bin/fwatchdog

RUN chmod +x /usr/bin/fwatchdog

ARG ADDITIONAL_PACKAGE
RUN /bin/sh -c set -eux; apt-get update; apt-get install -y --no-install-recommends gcc git gnupg make build-essential ${ADDITIONAL_PACKAGE}; rm -rf /var/lib/apt/lists/*

RUN addgroup --system user && adduser --system user --ingroup user

USER user

ENV PATH=$PATH:/home/user/.local/bin

# WORKDIR /home/user/app

WORKDIR /home/app/

RUN pip install --no-cache poetry
RUN poetry config --no-cache

COPY pyproject.toml .
COPY poetry.lock .

COPY function function

RUN poetry install --no-root #--without dev

RUN poetry export --only main -f requirements.txt --without-hashes --output requirements.txt

RUN pip install --no-cache -r requirements.txt -r function/requirements.txt --user

COPY server server
COPY index.py .

ARG FUNCNAME=''
ENV FUNCNAME=$FUNCNAME

ENV fprocess="python index.py"
ENV cgi_headers="true"
ENV mode="http"
ENV upstream_url="http://127.0.0.1:8000"
ENV write_debug="false"

HEALTHCHECK --interval=5s CMD [ -e /tmp/.lock ] || exit 1

CMD ["fwatchdog"]
