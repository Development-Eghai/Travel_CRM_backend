from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from sqlalchemy import select
from typing import Optional
from core.database import SessionLocal
from models.trip import Trip
from schemas.trip import TripCreate, TripOut
from utils.response import api_json_response_format  # Adjust path if needed

router = APIRouter()

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@router.post("/")
def create_trip(trip_in: TripCreate, db: Session = Depends(get_db)):
    try:
        trip = Trip(**trip_in.model_dump())
        db.add(trip)
        db.commit()
        db.refresh(trip)
        return api_json_response_format(True, "Trip created successfully.", 201, TripOut.model_validate(trip).model_dump())
    except Exception as e:
        return api_json_response_format(False, f"Error creating trip: {e}", 500, {})

@router.put("/{trip_id}")
def update_trip(trip_id: int, trip_in: TripCreate, db: Session = Depends(get_db)):
    try:
        trip = db.get(Trip, trip_id)
        if not trip:
            return api_json_response_format(False, "Trip not found", 404, {})
        for key, value in trip_in.model_dump().items():
            setattr(trip, key, value)
        db.commit()
        db.refresh(trip)
        return api_json_response_format(True, "Trip updated successfully.", 200, TripOut.model_validate(trip).model_dump())
    except Exception as e:
        return api_json_response_format(False, f"Error updating trip: {e}", 500, {})

@router.delete("/{trip_id}")
def delete_trip(trip_id: int, db: Session = Depends(get_db)):
    try:
        trip = db.get(Trip, trip_id)
        if not trip:
            return api_json_response_format(False, "Trip not found", 404, {})
        db.delete(trip)
        db.commit()
        return api_json_response_format(True, "Trip deleted successfully.", 200, {})
    except Exception as e:
        return api_json_response_format(False, f"Error deleting trip: {e}", 500, {})

@router.get("/{trip_id}")
def get_trip_by_id(trip_id: int, db: Session = Depends(get_db)):
    try:
        trip = db.get(Trip, trip_id)
        if not trip:
            return api_json_response_format(False, "Trip not found", 404, {})
        return api_json_response_format(True, "Trip retrieved successfully.", 200, TripOut.model_validate(trip).model_dump())
    except Exception as e:
        return api_json_response_format(False, f"Error retrieving trip: {e}", 500, {})

@router.get("/")
def get_trips(db: Session = Depends(get_db)):
    try:
        trips = db.scalars(select(Trip)).all()
        data = [TripOut.model_validate(t).model_dump() for t in trips]
        return api_json_response_format(True, "Trips retrieved successfully.", 200, data)
    except Exception as e:
        return api_json_response_format(False, f"Error retrieving trips: {e}", 500, {})