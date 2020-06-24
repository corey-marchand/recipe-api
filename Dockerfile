FROM python:3
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1
RUN mkdir /code
WORKDIR /code
COPY requirements.txt /code/
COPY poetry.lock pyproject.toml /code/
RUN poetry shell
RUN pip3 install poetry
RUN poetry install
COPY . /code/