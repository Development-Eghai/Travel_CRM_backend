# app/api/site_setting.py
from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from typing import List
from schemas.site_setting import SiteSettingCreate, SiteSettingOut
from models.site_setting import SiteSetting
from core.database import get_db

router = APIRouter()

@router.post("/", response_model=SiteSettingOut)
def create_setting(setting_in: SiteSettingCreate, db: Session = Depends(get_db)):
    setting = SiteSetting(**setting_in.model_dump())
    db.add(setting)
    db.commit()
    db.refresh(setting)
    return setting

@router.get("/", response_model=List[SiteSettingOut])
def get_settings(db: Session = Depends(get_db)):
    return db.query(SiteSetting).all()

@router.get("/{setting_id}", response_model=SiteSettingOut)
def get_setting(setting_id: int, db: Session = Depends(get_db)):
    setting = db.query(SiteSetting).filter(SiteSetting.id == setting_id).first()
    if not setting:
        raise HTTPException(status_code=404, detail="Setting not found")
    return setting

@router.put("/{setting_id}", response_model=SiteSettingOut)
def update_setting(setting_id: int, setting_in: SiteSettingCreate, db: Session = Depends(get_db)):
    setting = db.query(SiteSetting).filter(SiteSetting.id == setting_id).first()
    if not setting:
        raise HTTPException(status_code=404, detail="Setting not found")
    for key, value in setting_in.model_dump().items():
        setattr(setting, key, value)
    db.commit()
    db.refresh(setting)
    return setting

@router.delete("/{setting_id}")
def delete_setting(setting_id: int, db: Session = Depends(get_db)):
    setting = db.query(SiteSetting).filter(SiteSetting.id == setting_id).first()
    if not setting:
        raise HTTPException(status_code=404, detail="Setting not found")
    db.delete(setting)
    db.commit()
    return {"detail": "Site setting deleted"}