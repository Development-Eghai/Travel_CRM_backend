from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from typing import List
from schemas.site_setting import SiteSettingCreate, SiteSettingOut
from models.site_setting import SiteSetting
from core.database import get_db
from utils.response import api_json_response_format  # Adjust path if needed

router = APIRouter()

@router.post("/")
def create_setting(setting_in: SiteSettingCreate, db: Session = Depends(get_db)):
    try:
        setting = SiteSetting(**setting_in.model_dump())
        db.add(setting)
        db.commit()
        db.refresh(setting)
        return api_json_response_format(True, "Site setting created successfully.", 201, SiteSettingOut.model_validate(setting).model_dump())
    except Exception as e:
        return api_json_response_format(False, f"Error creating site setting: {e}", 500, {})

@router.get("/")
def get_settings(db: Session = Depends(get_db)):
    try:
        settings = db.query(SiteSetting).all()
        data = [SiteSettingOut.model_validate(s).model_dump() for s in settings]
        return api_json_response_format(True, "Site settings retrieved successfully.", 200, data)
    except Exception as e:
        return api_json_response_format(False, f"Error retrieving site settings: {e}", 500, {})

@router.get("/{setting_id}")
def get_setting(setting_id: int, db: Session = Depends(get_db)):
    try:
        setting = db.query(SiteSetting).filter(SiteSetting.id == setting_id).first()
        if not setting:
            return api_json_response_format(False, "Site setting not found", 404, {})
        return api_json_response_format(True, "Site setting retrieved successfully.", 200, SiteSettingOut.model_validate(setting).model_dump())
    except Exception as e:
        return api_json_response_format(False, f"Error retrieving site setting: {e}", 500, {})

@router.put("/{setting_id}")
def update_setting(setting_id: int, setting_in: SiteSettingCreate, db: Session = Depends(get_db)):
    try:
        setting = db.query(SiteSetting).filter(SiteSetting.id == setting_id).first()
        if not setting:
            return api_json_response_format(False, "Site setting not found", 404, {})
        for key, value in setting_in.model_dump().items():
            setattr(setting, key, value)
        db.commit()
        db.refresh(setting)
        return api_json_response_format(True, "Site setting updated successfully.", 200, SiteSettingOut.model_validate(setting).model_dump())
    except Exception as e:
        return api_json_response_format(False, f"Error updating site setting: {e}", 500, {})

@router.delete("/{setting_id}")
def delete_setting(setting_id: int, db: Session = Depends(get_db)):
    try:
        setting = db.query(SiteSetting).filter(SiteSetting.id == setting_id).first()
        if not setting:
            return api_json_response_format(False, "Site setting not found", 404, {})
        db.delete(setting)
        db.commit()
        return api_json_response_format(True, "Site setting deleted successfully.", 200, {})
    except Exception as e:
        return api_json_response_format(False, f"Error deleting site setting: {e}", 500, {})