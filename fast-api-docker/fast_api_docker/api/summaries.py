from typing import Any, Dict

from fastapi import APIRouter, HTTPException

from fast_api_docker.api import crud
from fast_api_docker.models.pydantic import SummaryPayloadSchema, SummaryResponseSchema


router = APIRouter()


@router.post('/', response_model=SummaryResponseSchema, status_code=201)
async def create_summary(payload: SummaryPayloadSchema) -> Dict[str, Any]:
    summary_id: int = await crud.post(payload)

    return {
        'id': summary_id,
        'url': payload.url
    }
