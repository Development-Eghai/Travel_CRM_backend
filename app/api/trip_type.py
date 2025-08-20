from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from app.schemas.trip_type import TripTypeCreate, TripTypeOut
from app.models.trip_type import TripType
from app.core.database import get_db

router = APIRouter()

@router.post("/", response_model=TripTypeOut)
def create_trip_type(trip_type_in: TripTypeCreate, db: Session = Depends(get_db)):
    trip_type = TripType(**trip_type_in.model_dump())
    db.add(trip_type)
    db.commit()
    db.refresh(trip_type)
    return trip_type

@router.get("/", response_model=list[TripTypeOut])
def get_all_trip_types(db: Session = Depends(get_db)):
    return db.query(TripType).all()

@router.get("/{trip_type_id}", response_model=TripTypeOut)
def get_trip_type_by_id(trip_type_id: int, db: Session = Depends(get_db)):
    trip_type = db.query(TripType).filter(TripType.id == trip_type_id).first()
    if not trip_type:
        raise HTTPException(status_code=404, detail="Trip type not found")
    return trip_type

@router.put("/{trip_type_id}", response_model=TripTypeOut)
def update_trip_type(trip_type_id: int, trip_type_in: TripTypeCreate, db: Session = Depends(get_db)):
    trip_type = db.query(TripType).filter(TripType.id == trip_type_id).first()
    if not trip_type:
        raise HTTPException(status_code=404, detail="Trip type not found")
    for key, value in trip_type_in.model_dump().items():
        setattr(trip_type, key, value)
    db.commit()
    db.refresh(trip_type)
    return trip_type

@router.delete("/{trip_type_id}")
def delete_trip_type(trip_type_id: int, db: Session = Depends(get_db)):
    trip_type = db.query(TripType).filter(TripType.id == trip_type_id).first()
    if not trip_type:
        raise HTTPException(status_code=404, detail="Trip type not found")
    db.delete(trip_type)
    db.commit()
    return {"detail": "Trip type deleted successfully"}