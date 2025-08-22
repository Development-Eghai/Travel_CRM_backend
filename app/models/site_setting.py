# app/models/site_setting.py
from sqlalchemy import Column, Integer, String, Text, JSON, Boolean, DateTime
from datetime import datetime
from app.core.database import Base

class SiteSetting(Base):
    __tablename__ = "site_settings"

    id = Column(Integer, primary_key=True, index=True)
    site_title = Column(String(255), nullable=True)
    company_name = Column(String(255), nullable=True)
    site_description = Column(Text, nullable=True)
    logo_url = Column(Text, nullable=True)
    favicon_url = Column(Text, nullable=True)
    contact_email = Column(String(255), nullable=True)
    phone_numbers = Column(JSON, nullable=True)
    business_address = Column(Text, nullable=True)
    tenant_id = Column(Integer, nullable=False)
    is_active = Column(Boolean, default=True)
    created_at = Column(DateTime, default=datetime.now())
    updated_at = Column(DateTime, default=datetime.now(), onupdate=datetime.now())