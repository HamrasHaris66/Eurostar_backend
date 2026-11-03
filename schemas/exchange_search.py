from typing import List, Optional

from pydantic import BaseModel, Field

from schemas.journey_search import Currency


class ExchangePassenger(BaseModel):
    id: str = Field(..., description="e.g. passenger_1")
    type: str = Field(..., description='"AD", "CH", "SN", "YT"')


class ExchangeSearchRequest(BaseModel):
    bookingReference: str = Field(..., min_length=1)
    exchangeItems: List[int] = Field(
        ...,
        min_length=1,
        description="Item refs from the booking to exchange (itemRef values)",
    )
    origin: str
    destination: str
    currency: Optional[Currency] = None
    outboundDate: Optional[str] = Field(None, description="YYYY-MM-DD")
    inboundDate: Optional[str] = Field(None, description="YYYY-MM-DD")
    passengers: List[ExchangePassenger] = Field(..., min_length=1)