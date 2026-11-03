from schemas.add_payment import AddPaymentRequest
from services.eurostar_https import EurostarHTTPError, eurostar_post


def add_payment(payload: AddPaymentRequest) -> dict | None:
    body = payload.model_dump()

    try:
        data = eurostar_post("/add-payment", payload=body)
    except EurostarHTTPError:
        return None

    if not isinstance(data, dict):
        return None

    return data