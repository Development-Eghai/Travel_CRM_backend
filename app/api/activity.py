from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from schemas.activity import ActivityCreate, ActivityOut
from models.activity import Activity
from core.database import get_db

router = APIRouter()

@router.post("/", response_model=ActivityOut)
def create_activity(activity_in: ActivityCreate, db: Session = Depends(get_db)):
    activity = Activity(**activity_in.model_dump())
    db.add(activity)
    db.commit()
    db.refresh(activity)
    return activity

@router.get("/", response_model=list[ActivityOut])
def get_all_activities(db: Session = Depends(get_db)):
    return db.query(Activity).all()

@router.get("/{activity_id}", response_model=ActivityOut)
def get_activity_by_id(activity_id: int, db: Session = Depends(get_db)):
    activity = db.query(Activity).filter(Activity.id == activity_id).first()
    if not activity:
        raise HTTPException(status_code=404, detail="Activity not found")
    return activity

@router.put("/{activity_id}", response_model=ActivityOut)
def update_activity(activity_id: int, activity_in: ActivityCreate, db: Session = Depends(get_db)):
    activity = db.query(Activity).filter(Activity.id == activity_id).first()
    if not activity:
        raise HTTPException(status_code=404, detail="Activity not found")
    for key, value in activity_in.model_dump().items():
        setattr(activity, key, value)
    db.commit()
    db.refresh(activity)
    return activity

@router.delete("/{activity_id}")
def delete_activity(activity_id: int, db: Session = Depends(get_db)):
    activity = db.query(Activity).filter(Activity.id == activity_id).first()
    if not activity:
        raise HTTPException(status_code=404, detail="Activity not found")
    db.delete(activity)
    db.commit()
    return {"detail": "Activity deleted successfully"}