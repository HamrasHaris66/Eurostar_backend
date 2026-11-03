from schemas.cancel_booking_items import CancelBookingItemsRequest
from services.eurostar_https import EurostarHTTPError, eurostar_post


def cancel_booking_items(payload: CancelBookingItemsRequest) -> dict | None:
    body = payload.model_dump()

    if body.get("itemRefs") is None:
        body.pop("itemRefs", None)

    try:
        data = eurostar_post("/cancel-booking-items", payload=body)
    except EurostarHTTPError:
        return None

    if not isinstance(data, dict):
        return None

    return data