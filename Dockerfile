FROM python:3.9.10

ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

ENV WORKDIR=/home/app/web
RUN groupadd -r app && useradd -rm -d /home/app -s /bin/bash -g app app

WORKDIR ${WORKDIR}

RUN pip install --upgrade pip && \
pip install poetry

COPY pyproject.toml poetry.lock ${WORKDIR}/

# Docker containers are already isolated and don't need virtual environments.
# so we turn off the creation of virtualenv.
RUN poetry config virtualenvs.create false --local && \
poetry install 

COPY . ${WORKDIR}/

RUN chown -R app:app ${WORKDIR}

USER app

EXPOSE 8000