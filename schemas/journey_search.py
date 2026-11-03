from enum import Enum
from typing import List, Optional

from pydantic import BaseModel, Field, field_validator



class Currency(str, Enum):
    GBP = "GBP"
    EUR = "EUR"
    USD = "USD"


class JourneySearchRequest(BaseModel):
    origin: str = Field(..., description="UIC code of origin station")
    destination: str = Field(..., description="UIC code of destination station")
    currency: Currency = Field(..., description="ISO 4217 currency code")
    outboundDate: str = Field(..., description="YYYY-MM-DD")
    inboundDate: Optional[str] = Field(None, description="YYYY-MM-DD (return only)")

    adults: int = Field(..., ge=1, le=9)
    seniors: int = Field(0, ge=0, le=9)
    youths: int = Field(0, ge=0, le=9)
    children: int = Field(0, ge=0, le=9)
    infants: int = Field(0, ge=0, le=9)

    contractCode: Optional[str] = Field(None, description='e.g. "PUBLIC"')
    productFamilies: Optional[List[str]] = Field(None, description='e.g. ["PUB"]')

    @field_validator("outboundDate", "inboundDate")
    @classmethod
    def _check_date_format(cls, v: Optional[str]) -> Optional[str]:
        if v is None:
            return v
        #Eurostar expects YYYY-MM-DD
        if len(v) != 10 or v[4] != "-" or v[7] != "-":
            raise ValueError("Date must be in YYYY-MM-DD format")
        return v



class StationRef(BaseModel):
    uic: str
    shortCode: Optional[str] = None
    shortName: Optional[str] = None
    timezone: Optional[str] = None


class Timing(BaseModel):
    departs: str
    arrives: str
    duration: int
    departureDate: str
    arrivalDate: str


class ServiceType(BaseModel):
    name: str
    code: str


class Product(BaseModel):
    name: str
    passengerId: str
    tariffCode: str
    bucketCode: str
    price: float


class Leg(BaseModel):
    origin: StationRef
    destination: StationRef
    timing: Timing
    serviceType: ServiceType
    serviceName: str
    serviceIdentifier: str
    products: List[Product]
    flexibilityLevel: Optional[int] = None


class TravelClass(BaseModel):
    code: str
    name: str


class ProductFamily(BaseModel):
    code: Optional[str] = None
    name: Optional[str] = None
    


class Fare(BaseModel):
    flexibilityLevel: Optional[int] = None
    seats: int
    legs: List[Leg]
    travelClass: TravelClass = Field(..., alias="class")
    productCode: Optional[str] = None
    productFamily: Optional[ProductFamily] = None

    model_config = {"populate_by_name": True}


class Journey(BaseModel):
    fares: List[Fare]


class JourneyDirection(BaseModel):
    origin: Optional[StationRef] = None
    destination: Optional[StationRef] = None
    journeys: List[Journey] = []


class PassengerType(BaseModel):
    type: str
    id: str
    disabilityType: str


class JourneySearchResponse(BaseModel):
    outbound: JourneyDirection
    inbound: Optional[JourneyDirection] = None
    passengers: List[PassengerType]