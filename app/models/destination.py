from sqlalchemy import Column, Integer, String, Text, Enum, JSON, DateTime
from datetime import datetime
from ..core.database import Base

class Destination(Base):
    __tablename__ = "destinations"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String(255), nullable=False)
    slug = Column(String(255), nullable=False)
    hero_image = Column(Text)
    description = Column(Text)
    parent_id = Column(Integer)
    destination_type = Column(Enum("Domestic", "International"), nullable=False)
    popular_trip_ids = Column(JSON)
    blog_category_ids = Column(JSON)
    featured_blog_ids = Column(JSON)
    about = Column(Text)
    how_to_reach = Column(Text)
    activity_ids = Column(JSON)
    travel_guide_tips = Column(Text)
    tenant_id = Column(Integer, nullable=False)
    created_at = Column(DateTime, default=datetime.now())
    updated_at = Column(DateTime, default=datetime.now(), onupdate=datetime.now())