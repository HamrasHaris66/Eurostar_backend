from schemas.confirm_cancel_booking import ConfirmCancelBookingRequest
from services.eurostar_https import EurostarHTTPError, eurostar_post


def confirm_cancel_booking(payload: ConfirmCancelBookingRequest) -> dict | None:
    body = payload.model_dump()

    try:
        data = eurostar_post("/confirm-cancel-booking", payload=body)
    except EurostarHTTPError:
        return None

    if not isinstance(data, dict):
        return None

    return data