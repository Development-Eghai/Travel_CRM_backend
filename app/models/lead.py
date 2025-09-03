from ..core.database import Base
from sqlalchemy import Column, Integer, String, Text, Date, Time, Enum, ForeignKey, DateTime
from sqlalchemy import Column, Integer, String, Text, Date, Time, Enum, DateTime, ForeignKey
from datetime import datetime

class Lead(Base):
    __tablename__ = "leads"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String(255), nullable=False)
    email = Column(String(255), nullable=False)
    mobile = Column(String(20))
    trip_type_id = Column(Integer, ForeignKey("trip_types.id"))
    destination_id = Column(Integer, ForeignKey("destinations.id"))
    pickup_location = Column(String(255))
    drop_location = Column(String(255))
    travel_date_from = Column(Date)
    travel_date_to = Column(Date)
    adults = Column(Integer)
    children = Column(Integer)
    assigned_to = Column(Integer)
    follow_up_date = Column(Date)
    follow_up_time = Column(Time)
    notes = Column(Text)
    status = Column(Enum("new", "contacted", "quoted", "booked"))
    tenant_id = Column(Integer, nullable=False)
    created_at = Column(DateTime, default=datetime.now())
    updated_at = Column(DateTime, default=datetime.now(), onupdate=datetime.now())