from schemas.add_customer import AddCustomerRequest
from services.eurostar_https import EurostarHTTPError, eurostar_post


def add_customer(payload: AddCustomerRequest) -> dict | None:
    """
    Call Eurostar POST /add-customer.
    Attaches customer (contact) details to a provisional booking.
    Returns the parsed dict on success, None on upstream failure.
    """
    try:
        data = eurostar_post("/add-customer", payload=payload)
    except EurostarHTTPError:
        return None

    if not isinstance(data, dict):
        return None

    return data