from fastapi import FastAPI
from fastapi.types import DecoratedCallable

from .config_test import test_app


def test_ping(test_app: FastAPI):
    response: DecoratedCallable = test_app.get('/ping')
    assert response.status_code == 200
    assert response.json() == {"environment": "dev", "ping": "pong", "testing": True}
