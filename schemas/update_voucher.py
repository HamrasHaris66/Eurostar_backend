from typing import Optional

from pydantic import BaseModel, Field, model_validator


class ExternalReferenceDates(BaseModel):
    originalSalesPeriodEnd: Optional[str] = None
    originalTravelPeriodEnd: Optional[str] = None


class UpdateVoucherRequest(BaseModel):
    voucherAlias: str = Field(..., min_length=1)
    reason: str = Field(..., min_length=1)

    active: Optional[bool] = None
    recipientEmail: Optional[str] = None
    salesPeriodEnd: Optional[str] = None
    externalReferencesDates: Optional[ExternalReferenceDates] = None

    @model_validator(mode="after")
    def _at_least_one_update_field(self) -> "UpdateVoucherRequest":
        if (
            self.active is None
            and self.recipientEmail is None
            and self.salesPeriodEnd is None
            and self.externalReferencesDates is None
        ):
            raise ValueError(
                "At least one of 'active', 'recipientEmail', 'salesPeriodEnd', "
                "or 'externalReferencesDates' must be provided."
            )
        return self