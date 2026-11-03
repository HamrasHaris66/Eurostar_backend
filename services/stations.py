from services.eurostar_https import EurostarHTTPError, eurostar_get


def fetch_stations() -> list[dict]:
    """
    Fetch all Eurostar stations.
    Returns [] on any upstream failure — the router maps that to a clean 502.
    """
    try:
        data = eurostar_get("/stations")
    except EurostarHTTPError:
        return []

    if not isinstance(data, list):
        return []

    return [item for item in data if isinstance(item, dict)]