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
from app.api import trip_day
from app.api import fixed_departure
from app.api import lead_assignment
from app.api import task
from app.api import role
from app.api import site_setting
from app.api import activity_type
from app.api import blog_post
from app.api import tag
from app.api import blog_category
from app.api import quotation_item


app.include_router(quotation_item.router, prefix="/api/quotation-items", tags=["Quotation Items"])


app.include_router(blog_category.router, prefix="/api/blog-categories", tags=["Blog Categories"])


app.include_router(tag.router, prefix="/api/tags", tags=["Tags"])


app.include_router(blog_post.router, prefix="/api/blog-posts", tags=["Blog Posts"])
app.include_router(activity_type.router, prefix="/api/activity-types", tags=["Activity Types"])
app.include_router(site_setting.router, prefix="/api/site-settings", tags=["Site Settings"])
app.include_router(role.router, prefix="/api/roles", tags=["Roles"])

app.include_router(task.router, prefix="/api/task", tags=["Tasks"])
app.include_router(lead_assignment.router, prefix="/api/lead-assignments", tags=["Lead Assignments"])

app.include_router(fixed_departure.router, prefix="/api/fixed-departures", tags=["Fixed Departures"])


app.include_router(trip_day.router, prefix="/api/trip-days", tags=["Trip Days"])

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
