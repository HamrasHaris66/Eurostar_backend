from schemas.hold_booking import HoldBookingRequest
from services.eurostar_https import EurostarHTTPError, eurostar_post


def hold_booking(payload: HoldBookingRequest) -> dict | None:
    body = payload.model_dump()

    try:
        data = eurostar_post("/hold-booking", payload=body)
    except EurostarHTTPError:
        return None

    if not isinstance(data, dict):
        return None

    return data