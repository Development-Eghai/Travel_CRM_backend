# app/api/bookings.py
from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from typing import List
from app.schemas.bookings import BookingCreate, BookingOut
from app.models.bookings import Booking
from app.core.database import get_db

router = APIRouter()

@router.post("/", response_model=BookingOut)
def create_booking(booking_in: BookingCreate, db: Session = Depends(get_db)):
    booking = Booking(**booking_in.model_dump())
    db.add(booking)
    db.commit()
    db.refresh(booking)
    return booking

@router.get("/{booking_id}", response_model=BookingOut)
def get_booking_by_id(booking_id: int, db: Session = Depends(get_db)):
    booking = db.query(Booking).filter(Booking.id == booking_id).first()
    if not booking:
        raise HTTPException(status_code=404, detail="Booking not found")
    return booking

@router.get("/", response_model=List[BookingOut])
def get_all_bookings(db: Session = Depends(get_db)):
    return db.query(Booking).all()

@router.put("/{booking_id}", response_model=BookingOut)
def update_booking(booking_id: int, booking_in: BookingCreate, db: Session = Depends(get_db)):
    booking = db.query(Booking).filter(Booking.id == booking_id).first()
    if not booking:
        raise HTTPException(status_code=404, detail="Booking not found")
    for key, value in booking_in.model_dump().items():
        setattr(booking, key, value)
    db.commit()
    db.refresh(booking)
    return booking

@router.delete("/{booking_id}")
def delete_booking(booking_id: int, db: Session = Depends(get_db)):
    booking = db.query(Booking).filter(Booking.id == booking_id).first()
    if not booking:
        raise HTTPException(status_code=404, detail="Booking not found")
    db.delete(booking)
    db.commit()
    return {"detail": "Booking deleted successfully"}
