from typing import List, Optional

from pydantic import BaseModel, Field


class Infant(BaseModel):
    firstName: str = Field(..., min_length=1)
    lastName: str = Field(..., min_length=1)


class PassengerContact(BaseModel):
    id: str = Field(..., description="e.g. passenger_1")
    email: Optional[str] = None
    phoneNumber: Optional[str] = None
    infant: Optional[Infant] = None


class UpdatePassengerDetailsRequest(BaseModel):
    bookingReference: str = Field(..., min_length=1)
    passengers: List[PassengerContact] = Field(..., min_length=1)


class ResponsePassenger(BaseModel):
    id: str
    firstName: Optional[str] = None
    lastName: Optional[str] = None
    email: Optional[str] = None
    unformattedPhoneNumber: Optional[dict] = None
    infant: Optional[Infant] = None
    detailsCaptured: Optional[str] = None


class AdditionalDetail(BaseModel):
    key: str
    value: Optional[str] = None
    itemRef: Optional[str] = None


class UpdatePassengerDetailsResponse(BaseModel):
    reference: str
    passengers: List[ResponsePassenger]
    additionalDetails: List[AdditionalDetail]