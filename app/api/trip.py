from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from app.core.database import SessionLocal
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
def create(trip: TripCreate, db: Session = Depends(get_db)):
    return create_trip(db, trip)

@router.get("/", response_model=list[TripOut])
def read_all(db: Session = Depends(get_db)):
    return get_trips(db)