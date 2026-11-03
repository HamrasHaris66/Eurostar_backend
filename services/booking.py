from schemas.booking import BookingRequest
from services.eurostar_https import EurostarHTTPError, eurostar_post


def get_booking(payload: BookingRequest) -> dict | None:
    body = payload.model_dump()

    try:
        data = eurostar_post("/booking", payload=body)
    except EurostarHTTPError:
        return None

    if not isinstance(data, dict):
        return None

    return data