from ast import List
from fastapi import HTTPException
from sqlalchemy import select
from typing import Optional
from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from app.core.database import SessionLocal
from app.models.trip import Trip
from app.schemas.trip import TripCreate, TripOut
from app.crud.trip import create_trip, get_trips

router = APIRouter()

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@router.post("/", response_model=TripOut)
def create_trip(trip_in: TripCreate, db: Session = Depends(get_db)):
    trip = Trip(**trip_in.model_dump())
    db.add(trip)
    db.commit()
    db.refresh(trip)
    return trip

@router.put("/{trip_id}", response_model=TripOut)
def update_trip(trip_id: int, trip_in: TripCreate, db: Session = Depends(get_db)):
    trip = db.get(Trip, trip_id)
    if not trip:
        raise HTTPException(status_code=404, detail="Trip not found")
    for key, value in trip_in.model_dump().items():
        setattr(trip, key, value)
    db.commit()
    db.refresh(trip)
    return trip


@router.delete("/{trip_id}")
def delete_trip(trip_id: int, db: Session = Depends(get_db)):
    trip = db.get(Trip, trip_id)
    if not trip:
        raise HTTPException(status_code=404, detail="Trip not found")
    db.delete(trip)
    db.commit()
    return {"detail": "Trip deleted successfully"}


@router.get("/{trip_id}", response_model=TripOut)
def get_trip_by_id(trip_id: int, db: Session = Depends(get_db)):
    trip = db.get(Trip, trip_id)
    if not trip:
        raise HTTPException(status_code=404, detail="Trip not found")
    return trip

# @router.get("/", response_model=TripOut)
# def get_trips(
#     destination_id: Optional[int] = None,
#     trip_type_id: Optional[int] = None,
#     tenant_id: Optional[int] = None,
#     db: Session = Depends(get_db)
# ):
#     query = select(Trip)
#     if destination_id:
#         query = query.where(Trip.destination_id == destination_id)
#     if trip_type_id:
#         query = query.where(Trip.trip_type_id == trip_type_id)
#     if tenant_id:
#         query = query.where(Trip.tenant_id == tenant_id)
#     return db.scalars(query).all()

@router.get("/", response_model=list[TripOut])
def get_trips(db: Session = Depends(get_db)):
    trips = db.scalars(select(Trip)).all()
    return [TripOut.model_validate(t).model_dump() for t in trips]

# @router.get("/", response_model=list[TripOut])
# def read_all(db: Session = Depends(get_db)):
#     return get_trips(db)