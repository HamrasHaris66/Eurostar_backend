from schemas.create_booking import CreateBookingRequest
from services.eurostar_https import EurostarHTTPError, eurostar_post


def create_booking(payload: CreateBookingRequest) -> dict | None:
    """
    Call Eurostar POST /create-booking.
    Returns the raw parsed dict on success, or None on upstream failure.
    """
    try:
        data = eurostar_post("/create-booking", payload=payload)
    except EurostarHTTPError:
        return None

    if not isinstance(data, dict):
        return None

    return data