from contextlib import asynccontextmanager
from logging import Logger, getLogger

from fastapi import FastAPI

from fast_api_docker.api import ping, summaries
from fast_api_docker.db import init_db


log: Logger = getLogger('uvicorn')


@asynccontextmanager
async def lifespan(application: FastAPI):
    """Менеджер жизненного цикла приложения"""
    log.info('Запуск жизненного цикла приложения')
    init_db(application)
    yield
    log.info('Конец жизненного цикла приложения')


def create_application() -> FastAPI:
    application = FastAPI(lifespan=lifespan)
    application.include_router(ping.router)
    application.include_router(summaries.router, prefix='/summaries', tags=['summaries'])
    return application


app: FastAPI = create_application()



