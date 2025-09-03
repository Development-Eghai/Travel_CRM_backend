from sqlalchemy import Column, Integer, String, Text, JSON, DateTime, func
from ..core.database import Base
from datetime import datetime

class Quotation(Base):
    __tablename__ = "quotations"

    id = Column(Integer, primary_key=True, index=True)
    lead_id = Column(Integer, nullable=False)
    template_name = Column(String(255), nullable=False)
    trip_details = Column(Text)
    itenary = Column(JSON)
    hotels = Column(JSON)
    transport = Column(JSON)
    cost_breakdown = Column(JSON)
    terms = Column(Text)
    payment_policy = Column(Text)
    cancellation_policy = Column(Text)
    tenant_id = Column(Integer, nullable=False)
    created_at = Column(DateTime, default=datetime.now())
    updated_at = Column(DateTime, default=datetime.now(), onupdate=datetime.now())