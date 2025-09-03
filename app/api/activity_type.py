# app/api/activity_type.py
from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from typing import List
from schemas.activity_type import ActivityTypeCreate, ActivityTypeOut
from models.activity_type import ActivityType
from core.database import get_db

router = APIRouter()

@router.post("/", response_model=ActivityTypeOut)
def create_activity_type(activity_in: ActivityTypeCreate, db: Session = Depends(get_db)):
    activity = ActivityType(**activity_in.model_dump())
    db.add(activity)
    db.commit()
    db.refresh(activity)
    return activity

@router.get("/", response_model=List[ActivityTypeOut])
def get_activity_types(db: Session = Depends(get_db)):
    return db.query(ActivityType).all()

@router.get("/{activity_id}", response_model=ActivityTypeOut)
def get_activity_type(activity_id: int, db: Session = Depends(get_db)):
    activity = db.query(ActivityType).filter(ActivityType.id == activity_id).first()
    if not activity:
        raise HTTPException(status_code=404, detail="Activity type not found")
    return activity

@router.put("/{activity_id}", response_model=ActivityTypeOut)
def update_activity_type(activity_id: int, activity_in: ActivityTypeCreate, db: Session = Depends(get_db)):
    activity = db.query(ActivityType).filter(ActivityType.id == activity_id).first()
    if not activity:
        raise HTTPException(status_code=404, detail="Activity type not found")
    for key, value in activity_in.model_dump().items():
        setattr(activity, key, value)
    db.commit()
    db.refresh(activity)
    return activity

@router.delete("/{activity_id}")
def delete_activity_type(activity_id: int, db: Session = Depends(get_db)):
    activity = db.query(ActivityType).filter(ActivityType.id == activity_id).first()
    if not activity:
        raise HTTPException(status_code=404, detail="Activity type not found")
    db.delete(activity)
    db.commit()
    return {"detail": "Activity type deleted"}