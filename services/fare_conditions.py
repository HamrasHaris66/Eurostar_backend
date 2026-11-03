from services.eurostar_https import EurostarHTTPError, eurostar_get


def get_fare_conditions() -> dict | None:
    """
    Call Eurostar GET /fare-conditions.

    Returns the full mapping of tariff codes to their post-booking rules.
    Response is a dict keyed by tariff code — passed through as-is.
    """
    try:
        data = eurostar_get("/fare-conditions")
    except EurostarHTTPError:
        return None

    if not isinstance(data, dict):
        return None

    return data