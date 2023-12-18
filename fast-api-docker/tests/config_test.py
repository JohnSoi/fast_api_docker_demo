import os
import pytest

from starlette.testclient import TestClient
from fast_api_docker.main import create_application
from fast_api_docker.config import get_config, Config


def get_config_override() -> Config:
    return Config(testing=1, database_url=os.environ.get("DATABASE_TEST_URL"))


@pytest.fixture(scope='module')
def test_app():
    app = create_application()
    # Переопределение зависимостей
    app.dependency_overrides[get_config] = get_config_override

    with TestClient(app) as test_client:
        yield test_client
