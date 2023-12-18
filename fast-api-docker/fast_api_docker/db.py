import os
from logging import Logger, getLogger
from typing import Dict, Union

from fastapi import FastAPI
from tortoise import Tortoise, run_async
from tortoise.contrib.fastapi import register_tortoise

log: Logger = getLogger('uvicorn')


TORTOISE_ORM: Dict[str, Dict[str, Union[str]]] = {
    'connections': {'default': os.environ.get("DATABASE_URL")},
    'apps': {
        'models': {
            'models': ['fast_api_docker.models.tortoise', 'aerich.models'],
            'default_connection': 'default'
        },
    }
}


def init_db(application: FastAPI) -> None:
    register_tortoise(
        application,
        db_url=os.getenv('DATABASE_URL'),
        modules={'models': ['fast_api_docker.models.tortoise']},
        generate_schemas=False,
        add_exception_handlers=True
    )


async def generate_schema() -> None:
    log.info('Инициализация схемы БД')

    await Tortoise.init(
        db_url=os.environ.get('DATABASE_URL'),
        modules={'models': ['models.tortoise']}
    )
    log.info('Генерация схемы')
    await Tortoise.generate_schemas()
    await Tortoise.close_connections()


if __name__ == '__main__':
    run_async(generate_schema())

