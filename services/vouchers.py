from schemas.create_voucher import CreateVoucherRequest
from services.eurostar_https import EurostarHTTPError, eurostar_get, eurostar_post


def get_voucher(voucher_code: str) -> dict | None:
    try:
        data = eurostar_get(f"/vouchers/{voucher_code}")
    except EurostarHTTPError:
        return None

    if not isinstance(data, dict):
        return None

    return data


def create_voucher(payload: CreateVoucherRequest) -> dict | None:
    body = payload.model_dump()
    body = {k: v for k, v in body.items() if v is not None}

    try:
        data = eurostar_post("/vouchers", payload=body)
    except EurostarHTTPError:
        return None

    if not isinstance(data, dict):
        return None

    return data