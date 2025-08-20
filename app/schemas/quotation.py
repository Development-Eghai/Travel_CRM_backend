from pydantic import BaseModel
from datetime import datetime
from typing import Any

class QuotationBase(BaseModel):
    lead_id: int
    template_name: str
    trip_details: str
    itenary: dict[str, Any]
    hotels: dict[str, Any]
    transport: dict[str, Any]
    cost_breakdown: dict[str, Any]
    terms: str
    payment_policy: str
    cancellation_policy: str
    tenant_id: int

class QuotationCreate(QuotationBase):
    pass

class QuotationOut(QuotationBase):
    id: int
    created_at: datetime
    updated_at: datetime

    class Config:
        orm_mode = True