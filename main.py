from contextlib import asynccontextmanager

from fastapi import Depends, FastAPI

from core.dependencies import verify_api_key
from core.logging_setup import logger, setup_logging
from routers.add_customer_router import router as add_customer_router
from routers.add_payment_router import router as add_payment_router
from routers.booking_router import router as booking_router
from routers.confirm_booking_router import router as confirm_booking_router
from routers.create_booking_router import router as create_booking_router
from routers.hold_booking_router import router as hold_booking_router
from routers.journey_search_router import router as journey_search_router
from routers.stations_router import router as stations_router
from routers.update_passengers_router import router as update_passengers_router
from routers.exchange_search_router import router as exchange_search_router
from routers.rebook_router import router as rebook_router
from routers.meals_router import router as meals_router
from routers.update_meals_router import router as update_meals_router
from routers.cancel_booking_items_router import router as cancel_booking_items_router
from routers.confirm_cancel_booking_router import router as confirm_cancel_booking_router
from routers.revert_changes_router import router as revert_changes_router
from routers.void_booking_router import router as void_booking_router
from routers.update_passenger_details_router import router as update_passenger_details_router
from routers.tickets_router import router as tickets_router
from routers.ready_to_travel_router import router as ready_to_travel_router
from routers.submit_travel_documents_router import router as submit_travel_documents_router
from routers.vouchers_router import router as vouchers_router
from routers.update_voucher_router import router as update_voucher_router
from routers.fare_conditions_router import router as fare_conditions_router
from routers.fare_condition_by_tariff_router import router as fare_condition_by_tariff_router

@asynccontextmanager
async def lifespan(app: FastAPI):
    setup_logging()
    logger.info("eurostar_app starting up")
    yield
    logger.info("eurostar_app shutting down")


app = FastAPI(
    title="Eurostar",
    version="v1",
    lifespan=lifespan,
    docs_url="/docs",
    redoc_url="/redoc",
)

app.include_router(stations_router, dependencies=[Depends(verify_api_key)])
app.include_router(journey_search_router, dependencies=[Depends(verify_api_key)])
app.include_router(create_booking_router, dependencies=[Depends(verify_api_key)])
app.include_router(add_customer_router, dependencies=[Depends(verify_api_key)])
app.include_router(update_passengers_router, dependencies=[Depends(verify_api_key)])
app.include_router(hold_booking_router, dependencies=[Depends(verify_api_key)])
app.include_router(add_payment_router, dependencies=[Depends(verify_api_key)])
app.include_router(confirm_booking_router, dependencies=[Depends(verify_api_key)])
app.include_router(booking_router, dependencies=[Depends(verify_api_key)])
app.include_router(exchange_search_router, dependencies=[Depends(verify_api_key)])
app.include_router(rebook_router, dependencies=[Depends(verify_api_key)])
app.include_router(meals_router, dependencies=[Depends(verify_api_key)])
app.include_router(update_meals_router, dependencies=[Depends(verify_api_key)])
app.include_router(cancel_booking_items_router, dependencies=[Depends(verify_api_key)])
app.include_router(confirm_cancel_booking_router, dependencies=[Depends(verify_api_key)])
app.include_router(revert_changes_router, dependencies=[Depends(verify_api_key)])
app.include_router(void_booking_router, dependencies=[Depends(verify_api_key)])
app.include_router(update_passenger_details_router, dependencies=[Depends(verify_api_key)])
app.include_router(tickets_router, dependencies=[Depends(verify_api_key)])
app.include_router(ready_to_travel_router, dependencies=[Depends(verify_api_key)])
app.include_router(submit_travel_documents_router, dependencies=[Depends(verify_api_key)])
app.include_router(vouchers_router, dependencies=[Depends(verify_api_key)])
app.include_router(update_voucher_router, dependencies=[Depends(verify_api_key)])
app.include_router(fare_conditions_router, dependencies=[Depends(verify_api_key)])
app.include_router(fare_condition_by_tariff_router, dependencies=[Depends(verify_api_key)])

@app.get("/", include_in_schema=False)
async def root():
    return {
        "name": app.title,
        "version": app.version,
        "docs": "/docs",
        "health": "/health",
    }


@app.get("/health", tags=["health"])
async def health():
    return {"status": "ok"}


sub_app = app