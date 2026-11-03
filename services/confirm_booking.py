from schemas.confirm_booking import ConfirmBookingRequest
from services.eurostar_https import EurostarHTTPError, eurostar_post


def confirm_booking(payload: ConfirmBookingRequest) -> dict | None:
    body = payload.model_dump()

    try:
        data = eurostar_post("/confirm-booking", payload=body)
    except EurostarHTTPError:
        return None

    if not isinstance(data, dict):
        return None

    return data