FROM python:3.10-slim

WORKDIR code/
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1
COPY pyproject.toml /code/
RUN pip3 install poetry
RUN poetry config virtualenvs.create false
RUN poetry install -n --no-ansi
COPY . .

CMD python manage.py runserver 0.0.0.0:8000
