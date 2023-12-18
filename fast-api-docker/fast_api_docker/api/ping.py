from typing import Dict, Union

from fastapi import Depends, APIRouter

from fast_api_docker.config import Config, get_config

router = APIRouter()


@router.get('/ping')
async def pong(config: Config = Depends(get_config)) -> Dict[str, Union[str, bool]]:
    return {
        'ping': 'pong',
        'environment': config.environment,
        'testing': config.testing
    }
