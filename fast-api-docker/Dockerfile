# Базовый образ
FROM python:3.11.5-slim

# Рабочая директория
WORKDIR /usr/src/fast-api-docker

# Переменные окружения
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

# Установка системных зависимостей
RUN apt-get update \
    && apt-get install gcc -y \
    && apt-get clean
RUN apt install netcat-traditional

# Установка зависимостей
RUN pip install --upgrade pip
RUN pip install poetry
COPY ./pyproject.toml .
RUN poetry config virtualenvs.create false  \
    && poetry install $(test "$YOUR_ENV" == production && echo "--no-dev") --no-interaction --no-ansi

# Копирование папки проекта
COPY . .

# Добавление entrypoint.sh
COPY ./entrypoint.sh .
RUN chmod +x /usr/src/fast-api-docker/entrypoint.sh

# Запуск проверки на корректность экзепляра БД
ENTRYPOINT ["/usr/src/fast-api-docker/entrypoint.sh"]
