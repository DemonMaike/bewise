FROM python:3.12-slim

WORKDIR /app

RUN pip install poetry
COPY pyproject.toml poetry.lock ./
COPY . .
RUN poetry config virtualenvs.create false && poetry install --no-dev --no-interaction --no-ansi

EXPOSE 8000

CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8000"]