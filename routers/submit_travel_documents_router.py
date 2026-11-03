from fastapi import APIRouter, HTTPException

from schemas.submit_travel_documents import (
    SubmitTravelDocumentsRequest,
    SubmitTravelDocumentsResponse,
)
from services.submit_travel_documents import submit_travel_documents

router = APIRouter(prefix="/v1/submit-travel-docs", tags=["submit-travel-docs"])


@router.post("", response_model=SubmitTravelDocumentsResponse)
def post_submit_travel_documents(payload: SubmitTravelDocumentsRequest):
    ok = submit_travel_documents(payload)

    if not ok:
        raise HTTPException(
            status_code=502,
            detail="Failed to submit travel documents at Eurostar upstream.",
        )

    return SubmitTravelDocumentsResponse(success=True)