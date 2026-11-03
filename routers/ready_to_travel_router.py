from fastapi import APIRouter, HTTPException

from schemas.ready_to_travel import ReadyToTravelRequest
from services.ready_to_travel import ready_to_travel

router = APIRouter(prefix="/v1/ready-to-travel", tags=["ready-to-travel"])


@router.post("", response_model=None)
def post_ready_to_travel(payload: ReadyToTravelRequest):
    data = ready_to_travel(payload)

    if data is None:
        raise HTTPException(
            status_code=502,
            detail="Failed to check ready-to-travel status at Eurostar upstream.",
        )

    return data