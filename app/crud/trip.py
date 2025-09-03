from sqlalchemy.orm import Session
from models.trip import Trip
from schemas.trip import TripCreate

def create_trip(db: Session, trip: TripCreate):
    db_trip = Trip(**trip.dict())
    db.add(db_trip)
    db.commit()
    db.refresh(db_trip)
    return db_trip

def get_trips(db: Session):
    return db.query(Trip).all()