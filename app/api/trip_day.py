# app/api/trip_day.py
from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from typing import List
from app.schemas.trip_day import TripDayCreate, TripDayOut
from app.models.trip_day import TripDay
from app.core.database import get_db

router = APIRouter()

@router.post("/", response_model=TripDayOut)
def create_trip_day(day_in: TripDayCreate, db: Session = Depends(get_db)):
    day = TripDay(**day_in.model_dump())
    db.add(day)
    db.commit()
    db.refresh(day)
    return day

@router.get("/", response_model=List[TripDayOut])
def get_all_trip_days(db: Session = Depends(get_db)):
    return db.query(TripDay).all()

@router.get("/{trip_id}", response_model=List[TripDayOut])
def get_days_by_trip(trip_id: int, db: Session = Depends(get_db)):
    return db.query(TripDay).filter(TripDay.trip_id == trip_id).all()

@router.get("/{day_id}", response_model=TripDayOut)
def get_day_by_id(day_id: int, db: Session = Depends(get_db)):
    day = db.query(TripDay).filter(TripDay.id == day_id).first()
    if not day:
        raise HTTPException(status_code=404, detail="Trip day not found")
    return day

@router.put("/{day_id}", response_model=TripDayOut)
def update_trip_day(day_id: int, day_in: TripDayCreate, db: Session = Depends(get_db)):
    day = db.query(TripDay).filter(TripDay.id == day_id).first()
    if not day:
        raise HTTPException(status_code=404, detail="Trip day not found")
    for key, value in day_in.model_dump().items():
        setattr(day, key, value)
    db.commit()
    db.refresh(day)
    return day

@router.delete("/{day_id}")
def delete_trip_day(day_id: int, db: Session = Depends(get_db)):
    day = db.query(TripDay).filter(TripDay.id == day_id).first()
    if not day:
        raise HTTPException(status_code=404, detail="Trip day not found")
    db.delete(day)
    db.commit()
    return {"detail": "Trip day deleted successfully"}