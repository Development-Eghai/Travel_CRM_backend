from datetime import datetime
from pydantic import BaseModel, ConfigDict
from typing import Optional, List

class DestinationCreate(BaseModel):
    name: str
    slug: str
    hero_image: Optional[str] = None
    description: Optional[str] = None
    parent_id: Optional[int] = None
    destination_type: str
    popular_trip_ids: Optional[List[int]] = []
    blog_category_ids: Optional[List[int]] = []
    featured_blog_ids: Optional[List[int]] = []
    about: Optional[str] = None
    how_to_reach: Optional[str] = None
    activity_ids: Optional[List[int]] = []
    travel_guide_tips: Optional[str] = None
    tenant_id: int

    model_config = ConfigDict(from_attributes=True)

class DestinationOut(DestinationCreate):
    id: int
    created_at: Optional[datetime]
    updated_at: Optional[datetime]
