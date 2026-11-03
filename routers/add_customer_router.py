from fastapi import APIRouter, HTTPException

from schemas.add_customer import AddCustomerRequest, AddCustomerResponse
from services.add_customer import add_customer

router = APIRouter(prefix="/v1/add-customer", tags=["add-customer"])


@router.post("", response_model=AddCustomerResponse)
def post_add_customer(payload: AddCustomerRequest):
    data = add_customer(payload)

    if data is None:
        raise HTTPException(
            status_code=502,
            detail="Failed to add customer to booking on Eurostar upstream.",
        )

    return data