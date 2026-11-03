from enum import Enum
from typing import Optional

from pydantic import BaseModel, Field, field_validator


class Gender(str, Enum):
    M = "M"
    F = "F"
    U = "U"
    X = "X"


class DocumentType(str, Enum):
    passport = "passport"
    identity_card_a = "identity card - a"
    identity_card_c = "identity card - c"
    identity_card_i = "identity card - i"
    group_passport = "group passport"
    military_identification = "military identification"
    diplomatic_identification = "diplomatic identification"
    crew_member_certificate = "crew member certificate"
    passport_card = "passport card"
    other = "other"


class TravelDocumentPassenger(BaseModel):
    passengerUUID: str = Field(..., min_length=1)
    dateOfBirth: Optional[str] = Field(None, description="YYYY-MM-DD")
    documentNumber: str = Field(..., min_length=1, max_length=35)
    familyName: str = Field(..., min_length=1, max_length=35)
    givenName: str = Field(..., min_length=1, max_length=35)
    gender: Optional[Gender] = None
    nationality: str = Field(..., min_length=3, max_length=3)
    documentType: DocumentType
    countryOfIssue: str = Field(..., min_length=3, max_length=3)
    expiryDate: str = Field(..., description="YYYY-MM-DD, future date")

    @field_validator("familyName", "givenName", mode="before")
    @classmethod
    def _uppercase(cls, v):
        if isinstance(v, str):
            return v.upper()
        return v

    @field_validator("documentNumber", mode="before")
    @classmethod
    def _uppercase_docnum(cls, v):
        if isinstance(v, str):
            return v.upper()
        return v


class SubmitTravelDocumentsRequest(BaseModel):
    bookingReference: str = Field(..., min_length=1)
    passenger: TravelDocumentPassenger


class SubmitTravelDocumentsResponse(BaseModel):
    success: bool
    message: str = "Travel documents submitted successfully."