from schemas.update_voucher import UpdateVoucherRequest
from services.eurostar_https import EurostarHTTPError, eurostar_patch


def update_voucher(payload: UpdateVoucherRequest) -> dict | None:
    """
    Call Eurostar PATCH /vouchers.

    Updates an existing voucher (activation, recipient email, sales
    period, or external reference dates). Returns the latest full
    voucher state on success.
    """
    body = payload.model_dump(exclude_none=True)

    try:
        data = eurostar_patch("/vouchers", payload=body)
    except EurostarHTTPError:
        return None

    if not isinstance(data, dict):
        return None

    return data