from fastapi import APIRouter, HTTPException

from schemas.journey_search import JourneySearchRequest, JourneySearchResponse
from services.journey_search import search_journeys

router = APIRouter(prefix="/v1/journey-search", tags=["journey-search"])


@router.post("", response_model=JourneySearchResponse)
def post_journey_search(payload: JourneySearchRequest):
    data = search_journeys(payload)

    if data is None:
        raise HTTPException(
            status_code=502,
            detail="Failed to retrieve journey search results from Eurostar upstream.",
        )

    return data