from os import getenv
from logging import getLogger, Logger
from functools import lru_cache

from pydantic import AnyUrl
from pydantic_settings import BaseSettings


log: Logger = getLogger('uvicorn')


class Config(BaseSettings):
    environment: str = getenv('ENVIRONMENT', 'PRODUCTION')
    testing: bool = getenv('TESTING', False)
    database_url: AnyUrl = getenv('DATABASE_URL')
    database_test_url: AnyUrl = getenv('DATABASE_TEST_URL')


@lru_cache()
def get_config() -> Config:
    log.info('Загрузка переменных окружения')
    return Config()

