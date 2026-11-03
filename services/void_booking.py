from schemas.void_booking import VoidBookingRequest
from services.eurostar_https import EurostarHTTPError, eurostar_post


def void_booking(payload: VoidBookingRequest) -> dict | None:
    body = payload.model_dump()

    try:
        data = eurostar_post("/void-booking", payload=body)
    except EurostarHTTPError:
        return None

    if not isinstance(data, dict):
        return None

    return data