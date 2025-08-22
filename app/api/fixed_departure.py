# app/api/fixed_departure.py
from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from typing import List
from app.schemas.fixed_departure import FixedDepartureCreate, FixedDepartureOut
from app.models.fixed_departure import FixedDeparture
from app.core.database import get_db

router = APIRouter()

@router.post("/", response_model=FixedDepartureOut)
def create_fixed_departure(fd_in: FixedDepartureCreate, db: Session = Depends(get_db)):
    fd = FixedDeparture(**fd_in.model_dump())
    db.add(fd)
    db.commit()
    db.refresh(fd)
    return fd

@router.get("/", response_model=List[FixedDepartureOut])
def get_all_fixed_departures(db: Session = Depends(get_db)):
    return db.query(FixedDeparture).all()

@router.get("/trip/{trip_id}", response_model=List[FixedDepartureOut])
def get_departures_by_trip(trip_id: int, db: Session = Depends(get_db)):
    return db.query(FixedDeparture).filter(FixedDeparture.trip_id == trip_id).all()

@router.get("/{fd_id}", response_model=FixedDepartureOut)
def get_departure_by_id(fd_id: int, db: Session = Depends(get_db)):
    fd = db.query(FixedDeparture).filter(FixedDeparture.id == fd_id).first()
    if not fd:
        raise HTTPException(status_code=404, detail="Fixed departure not found")
    return fd

@router.put("/{fd_id}", response_model=FixedDepartureOut)
def update_fixed_departure(fd_id: int, fd_in: FixedDepartureCreate, db: Session = Depends(get_db)):
    fd = db.query(FixedDeparture).filter(FixedDeparture.id == fd_id).first()
    if not fd:
        raise HTTPException(status_code=404, detail="Fixed departure not found")
    for key, value in fd_in.model_dump().items():
        setattr(fd, key, value)
    db.commit()
    db.refresh(fd)
    return fd

@router.delete("/{fd_id}")
def delete_fixed_departure(fd_id: int, db: Session = Depends(get_db)):
    fd = db.query(FixedDeparture).filter(FixedDeparture.id == fd_id).first()
    if not fd:
        raise HTTPException(status_code=404, detail="Fixed departure not found")
    db.delete(fd)
    db.commit()
    return {"detail": "Fixed departure deleted successfully"}