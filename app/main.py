from fastapi import FastAPI
from app.api import trip
from app.core.config import settings
from app.api import user
app = FastAPI(title="Travel CRM")

app.include_router(user.router, prefix="/api/users", tags=["Users"])

app.include_router(trip.router, prefix="/api/trips", tags=["Trips"])