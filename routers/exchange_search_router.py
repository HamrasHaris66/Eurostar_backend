from fastapi import APIRouter, HTTPException

from schemas.exchange_search import ExchangeSearchRequest
from services.exchange_search import exchange_search

router = APIRouter(prefix="/v1/exchange-search", tags=["exchange-search"])


@router.post("", response_model=None)
def post_exchange_search(payload: ExchangeSearchRequest):
    data = exchange_search(payload)

    if data is None:
        raise HTTPException(
            status_code=502,
            detail="Failed to search exchange options at Eurostar upstream.",
        )

    return data