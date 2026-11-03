from fastapi import APIRouter, HTTPException

from schemas.rebook import RebookRequest
from services.rebook import rebook

router = APIRouter(prefix="/v1/rebook", tags=["rebook"])


@router.post("", response_model=None)
def post_rebook(payload: RebookRequest):
    data = rebook(payload)

    if data is None:
        raise HTTPException(
            status_code=502,
            detail="Failed to rebook at Eurostar upstream.",
        )

    return data