from typing import Optional

from pydantic import BaseModel, Field

from schemas.journey_search import Currency


class PaymentInput(BaseModel):
    amount: float = Field(..., gt=0, description="Positive amount to charge")
    currency: Currency
    externalReference: str = Field(
        ...,
        min_length=1,
        description="Unique per transaction within the booking",
    )


class AddPaymentRequest(BaseModel):
    bookingReference: str = Field(..., min_length=1)
    payment: PaymentInput


class PaymentRecord(BaseModel):
    id: str
    uuid: Optional[str] = None
    refId: Optional[str] = None
    method: Optional[str] = None
    reference: Optional[str] = None
    externalReference: Optional[str] = None
    currency: str
    amountWithCurrency: float
    availableRefundAmount: Optional[float] = None
    transactionTimestamp: Optional[str] = None
    refundProcessTimestamp: Optional[str] = None
    isSuccessful: bool
    paymentStatus: str


class AddPaymentResponse(BaseModel):
    reference: str
    payments: list[PaymentRecord]