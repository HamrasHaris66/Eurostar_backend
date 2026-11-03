from fastapi import APIRouter, HTTPException

from schemas.tickets import TicketsRequest
from services.tickets import get_tickets

router = APIRouter(prefix="/v1/tickets", tags=["tickets"])


@router.post("", response_model=None)
def post_tickets(payload: TicketsRequest):
    data = get_tickets(payload)

    if data is None:
        raise HTTPException(
            status_code=502,
            detail="Failed to retrieve tickets from Eurostar upstream.",
        )

    return data