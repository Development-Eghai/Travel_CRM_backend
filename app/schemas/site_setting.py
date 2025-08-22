# app/schemas/site_setting.py
from pydantic import BaseModel, EmailStr
from typing import Optional, List, Dict
from datetime import datetime

class SiteSettingBase(BaseModel):
    site_title: Optional[str]
    company_name: Optional[str]
    site_description: Optional[str]
    logo_url: Optional[str]
    favicon_url: Optional[str]
    contact_email: Optional[EmailStr]
    phone_numbers: Optional[Dict[str, str]]  # e.g. {"support": "+91...", "sales": "+91..."}
    business_address: Optional[str]
    tenant_id: int
    is_active: Optional[bool] = True

class SiteSettingCreate(SiteSettingBase):
    pass

class SiteSettingOut(SiteSettingBase):
    id: int
    created_at: Optional[datetime]
    updated_at: Optional[datetime]

    class Config:
        orm_mode = True