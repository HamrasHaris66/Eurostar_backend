from schemas.tickets import TicketsRequest
from services.eurostar_https import EurostarHTTPError, eurostar_post


def get_tickets(payload: TicketsRequest) -> dict | None:
    body = {
        "bookingReference": payload.bookingReference,
        "lastName": payload.lastName,
    }

    params = {}
    if payload.language is not None:
        params["language"] = payload.language.value

    try:
        data = eurostar_post(
            "/tickets",
            payload=body,
            params=params or None,
        )
    except EurostarHTTPError:
        return None

    if not isinstance(data, dict):
        return None

    return data