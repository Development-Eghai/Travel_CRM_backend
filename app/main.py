from fastapi import FastAPI
from app.api import trip
from app.core.config import settings
from app.api import user
from app.api import destination
from app.api import activity
from app.api import trip_type
from app.api import lead
app = FastAPI(title="Travel CRM")
from app.api import lead_comments
from app.api import quotation
from app.api import bookings
from app.api import category

app.include_router(category.router, prefix="/api/categories", tags=["Categories"])

app.include_router(bookings.router, prefix="/api/bookings", tags=["Bookings"])
app.include_router(lead_comments.router, prefix="/api/lead-comments", tags=["Lead Comments"])
app.include_router(quotation.router, prefix="/api/quotation", tags=["Quotation"])
app.include_router(trip_type.router, prefix="/api/trip-types", tags=["Trip Types"])

app.include_router(lead.router, prefix="/api/leads", tags=["Leads"])

app.include_router(activity.router, prefix="/api/activities", tags=["Activities"])
app.include_router(user.router, prefix="/api/users", tags=["Users"])

app.include_router(trip.router, prefix="/api/trips", tags=["Trips"])
app.include_router(destination.router, prefix="/api/destinations", tags=["Destinations"])
