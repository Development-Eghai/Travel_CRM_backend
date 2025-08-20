from pydantic import BaseModel, EmailStr
from typing import Optional
from datetime import datetime, date, time

class LeadCreate(BaseModel):
    name: str
    email: EmailStr
    mobile: Optional[str]
    trip_type_id: Optional[int]
    destination_id: Optional[int]
    pickup_location: Optional[str]
    drop_location: Optional[str]
    travel_date_from: Optional[date]
    travel_date_to: Optional[date]
    adults: Optional[int]
    children: Optional[int]
    assigned_to: Optional[int]
    follow_up_date: Optional[date]
    follow_up_time: Optional[time]
    notes: Optional[str]
    status: Optional[str] = "new"
    tenant_id: int

class LeadOut(LeadCreate):
    id: int
    created_at: datetime
    updated_at: Optional[datetime]

    class Config:
        orm_mode = True