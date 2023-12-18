# Обучение poetry и FastAPI

## Poetry
<a href="https://python-poetry.org/docs/basic-usage/">Документация</a>
* Создание нового проекта: 
```bash 
poetry new poetry-demo
```
* Добавить зависимости
```bash
poetry add fastapi
```
* Использовать ```venv``` внутри проекта (изменить в файле конфигурации)
```toml
[virtualenvs]
in-project = true
```
* Установка зависимостей
```bash
poetry install 
```
* Запуск скриптов
```bash
 poetry run python your_script.py
 poetry run pytest
 poetry run uvicorn fast_api_docker.main:app --reload --workers 1
```
---
## Работа с контейнером

* Подключение к БД в контейнере и просмотр таблиц
```bash
# Подключение к СУБД 
docker-compose exec web-db psql -U postgres
# Подключение к БД
\c web_dev
# Список таблиц
\dt
```
* Если после клонирования и запуска контейнера, падает ```entrypoint.sh``` нужно изменить окончание строк на ```\n```
---

## Работа с Tortoise и Aerich
* Создать папку с моделью и файл с моделями
```python
from tortoise.fields import TextField, DatetimeField
from tortoise.models import Model


class TextSummary(Model):
    url: TextField = TextField()
    summary: TextField = TextField()
    created_at: DatetimeField = DatetimeField(auto_now_add=True)

    def __str__(self) -> str:
        return self.url
```
* Создать файл конфигурации БД
```python
import os
from typing import Dict, Union

print(os.environ.get("DATABASE_URL"))

TORTOISE_ORM: Dict[str, Dict[str, Union[str]]] = {
    'connections': {'default': os.environ.get("DATABASE_URL")},
    'apps': {
        'models': {
            'models': ['fast_api_docker.models.tortoise', 'aerich.models'],
            'default_connection': 'default'
        },
    }
}
```
> Для выполнения команд без контейнера 
> следует удалить ```docker-compose exec web ```
* Выполнить команду для инициализации настроек
```bash
docker-compose exec web aerich init -t app.db.TORTOISE_ORM
```
* Выполнить команду для создания миграции
```bash
docker-compose exec web aerich init-db
```
> Если в процессе последней команды выходит ошибка
> инициализации БД - следует удалить папку с миграциями

* Обновление до последней версии
```bash
docker-compose exec web aerich upgrade
```
* Откат последней версии
```bash
docker-compose exec web aerich downgrade
```
* История миграций
```bash
docker-compose exec web aerich history
```
---
## Работа с PyTest
* В папке создать файл с окончанием ```_test.py```
* Создать файл с тестами. Функция или класс должны оканчиваться на ```test```
```python
import os
import pytest

from starlette.testclient import TestClient
from fast_api_docker.main import app
from fast_api_docker.config import get_config, Config


def get_config_override() -> Config:
    return Config(testing=1, database_url=os.environ.get("DATABASE_TEST_URL"))


@pytest.fixture(scope='module')
def test_app():
    # Переопределение зависимостей
    app.dependency_overrides[get_config] = get_config_override

    with TestClient(app) as test_client:
        yield test_client
```
* Запуск тестов
```bash
docker-compose exec web poetry run pytest
```