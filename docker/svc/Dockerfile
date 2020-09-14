FROM tiangolo/uvicorn-gunicorn:python3.8-alpine3.10

RUN apt-get update && \
    apt-get install -y --no-install-recommends \
    ca-certificates \
    git \
    && apt-get clean && \
    rm -rf /var/lib/apt/lists/*

ENV WORKDIR /app

COPY Pipfile Pipfile.lock ${WORKDIR}

RUN set -ex \
    && apt-get update -y --fix-missing \
    && apt-get install -y -q --no-install-recommends \
    curl \
    file \
    && apt-get purge -y --auto-remove
    
RUN pip install pipenv --no-cache-dir && \
    pipenv install --system --deploy && \
    pip uninstall -y pipenv virtualenv-clone virtualenv

COPY backend $WORKDIR