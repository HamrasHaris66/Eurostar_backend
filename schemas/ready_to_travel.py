from typing import List

from pydantic import BaseModel, Field


class ReadyToTravelRequest(BaseModel):
    bookingReference: str = Field(..., min_length=1)


class PassengerReadyStatus(BaseModel):
    passengerUUID: str
    readyToTravel: bool


class ReadyToTravelResponse(BaseModel):
    passengers: List[PassengerReadyStatus]