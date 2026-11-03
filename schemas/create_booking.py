from enum import Enum
from typing import List, Optional

from pydantic import BaseModel, Field

from schemas.journey_search import Currency



class Direction(str, Enum):
    outbound = "outbound"
    inbound = "inbound"


class FulfillmentMethodCode(str, Enum):
    PAH = "PAH"  


class BookingItem(BaseModel):
    passengerId: str = Field(..., description="e.g. passenger_1")
    tariffCode: str = Field(..., description="e.g. B18PSXARBG")


class BookingSegment(BaseModel):
    origin: str
    destination: str
    direction: Direction
    startValidityDate: str = Field(..., description="YYYY-MM-DD")
    serviceName: str
    serviceIdentifier: str = Field(
        ...,
        description="From journey-search response — serviceIdentifier",
    )
    items: List[BookingItem] = Field(..., min_length=1)


class BookingPassenger(BaseModel):
    id: str
    type: str = Field(..., description='"AD", "CH", etc.')


class CreateBookingRequest(BaseModel):
    segments: List[BookingSegment] = Field(..., min_length=1)
    currency: Currency
    passengers: List[BookingPassenger] = Field(..., min_length=1)
    fulfillmentMethodCode: FulfillmentMethodCode = FulfillmentMethodCode.PAH
    contractCode: str = ""
    discountCards: List[str] = []



class FulfillmentMethod(BaseModel):
    code: str
    description: str
    name: str


class ProductFamilyRef(BaseModel):
    name: str
    code: str


class ResponsePassenger(BaseModel):
    id: str
    uuid: Optional[str] = None
    type: str
    disabilityType: Optional[str] = None
    loyaltyNumber: Optional[str] = None


class StationDetail(BaseModel):
    uic: str
    shortCode: Optional[str] = None
    shortName: Optional[str] = None
    name: Optional[str] = None
    timezone: Optional[str] = None


class ServiceTypeRef(BaseModel):
    name: str
    code: str


class Seat(BaseModel):
    seatNumber: str
    carriage: str
    spaceTypes: List[str] = []


class TariffDetails(BaseModel):
    tariffCode: str


class AfterSalesRule(BaseModel):
    active: bool
    validUntil: Optional[str] = None
    price: float
    type: str  # CANCEL | REBOOK | UPGRADE


class BookingProduct(BaseModel):
    name: str
    code: str
    seat: Optional[Seat] = None
    tariffDetails: TariffDetails
    inventoryClass: Optional[str] = None
    passengerId: str
    productFamily: Optional[ProductFamilyRef] = None
    itemId: Optional[str] = None
    itemRef: Optional[str] = None
    origin: Optional[StationDetail] = None
    destination: Optional[StationDetail] = None
    priceWithCurrency: float
    currency: str
    ticketNumber: Optional[str] = None
    type: Optional[str] = None
    flexibilityLevel: Optional[int] = None
    isRebookOFEActive: Optional[bool] = None
    isCancelOFEActive: Optional[bool] = None
    isActive: Optional[bool] = None
    createdRevision: Optional[str] = None
    afterSalesRules: List[AfterSalesRule] = []


class BookedSegment(BaseModel):
    ticketDocuments: List[dict] = []
    serviceType: ServiceTypeRef
    serviceName: str
    origin: StationDetail
    destination: StationDetail
    validityStartDate: str
    tariffGroupCode: Optional[str] = None
    products: List[BookingProduct]


class RevisionSource(BaseModel):
    username: Optional[str] = None


class CreateBookingResponse(BaseModel):
    reference: str
    fulfillmentMethod: List[FulfillmentMethod]
    productFamilies: List[ProductFamilyRef]
    passengers: List[ResponsePassenger]
    outbound: List[BookedSegment]
    inbound: List[BookedSegment]
    outboundTotalPrice: float
    inboundTotalPrice: float
    isDOBRequired: bool
    totalPriceWithCurrency: float
    totalPriceToBePaidWithCurrency: float
    currency: str
    createTimestamp: str
    expiryTimestamp: str
    status: str
    latestRevisionSource: RevisionSource