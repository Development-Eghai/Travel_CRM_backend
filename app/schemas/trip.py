from datetime import datetime
from pydantic import BaseModel, ConfigDict
from typing import Optional, List


class TripCreate(BaseModel):
    title: str
    overview: Optional[str] = None
    destination_id: int
    trip_model: str  # "Fixed" or "Custom"
    trip_type_id: int
    category_ids: List[int]
    hotel_category: Optional[str] = None
    price: float
    original_price: Optional[float] = None
    pickup_location: Optional[str] = None
    drop_location: Optional[str] = None
    fixed_slots: Optional[List[dict]] = None
    tenant_id: int

    model_config = ConfigDict(from_attributes=True)
    

class TripOut(BaseModel):
    id: int
    title: str
    overview: Optional[str]
    destination_id: int
    trip_model: str
    trip_type_id: int
    category_ids: List[int]
    hotel_category: Optional[str]
    price: float
    original_price: Optional[float]
    pickup_location: Optional[str]
    drop_location: Optional[str]
    fixed_slots: Optional[List[dict]]
    tenant_id: int
    created_at: Optional[datetime]  # ← This is the key fix
    updated_at: Optional[datetime]
    model_config = ConfigDict(from_attributes=True)