from fast_api_docker.models.pydantic import SummaryPayloadSchema
from fast_api_docker.models.tortoise import TextSummary


async def post(payload: SummaryPayloadSchema) -> int:
    summary: TextSummary = TextSummary(
        url=payload.url,
        summary='Example summary'
    )

    await summary.save()
    return summary.id
