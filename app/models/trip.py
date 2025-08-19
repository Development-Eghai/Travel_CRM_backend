from enum import Enum
from click import DateTime
from sqlalchemy import Column, Integer, String, Text, Enum, DECIMAL, DateTime, JSON,func
from app.core.database import Base
from datetime import datetime


class Trip(Base):
    __tablename__ = "trips"

    id = Column(Integer, primary_key=True, index=True)
    title = Column(String(255), nullable=False)
    overview = Column(Text)
    destination_id = Column(Integer, nullable=False)
    trip_model = Column(Enum("Fixed", "Custom"), nullable=False)
    trip_type_id = Column(Integer, nullable=False)
    category_ids = Column(JSON)
    hotel_category = Column(String(100))
    price = Column(DECIMAL(10, 2), nullable=False)
    original_price = Column(DECIMAL(10, 2))
    pickup_location = Column(String(255))
    drop_location = Column(String(255))
    fixed_slots = Column(JSON)
    tenant_id = Column(Integer, nullable=False)
    created_at = Column(DateTime, default=datetime.now())
    updated_at = Column(DateTime, default=datetime.now(), onupdate=datetime.now())

    