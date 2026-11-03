from typing import List

from pydantic import BaseModel, Field

from schemas.journey_search import Currency


class RebookItem(BaseModel):
    passengerId: str = Field(..., description="e.g. passenger_1")
    tariffCode: str = Field(..., description="New tariff from exchange-search")


class RebookSegment(BaseModel):
    origin: str
    destination: str
    direction: str = Field(..., description='"outbound" | "inbound"')
    departureDate: str = Field(..., description="YYYY-MM-DD")
    serviceName: str
    serviceIdentifier: str
    items: List[RebookItem] = Field(..., min_length=1)


class RebookRequest(BaseModel):
    bookingReference: str = Field(..., min_length=1)
    currency: Currency
    segments: List[RebookSegment] = Field(..., min_length=1)