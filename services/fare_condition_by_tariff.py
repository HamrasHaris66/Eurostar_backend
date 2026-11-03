from services.eurostar_https import EurostarHTTPError, eurostar_get


def get_fare_condition_by_tariff(tariff_code: str) -> tuple[dict | None, str | None]:
    """
    Call Eurostar GET /fare-conditions/{tariffCode}.

    Returns (data, error_kind). error_kind is one of:
      - None        -> success
      - "not_found" -> Eurostar returned 404
      - "upstream"  -> other upstream failure
    """
    try:
        data = eurostar_get(f"/fare-conditions/{tariff_code}")
    except EurostarHTTPError as exc:
        if exc.status_code == 404:
            return None, "not_found"
        return None, "upstream"

    if not isinstance(data, dict):
        return None, "upstream"

    return data, None