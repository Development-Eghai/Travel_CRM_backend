from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from schemas.destination import DestinationCreate, DestinationOut
from models.destination import Destination
from core.database import get_db

router = APIRouter()

@router.post("/", response_model=DestinationOut)
def create_destination(destination_in: DestinationCreate, db: Session = Depends(get_db)):
    destination = Destination(**destination_in.model_dump())
    db.add(destination)
    db.commit()
    db.refresh(destination)
    return destination

@router.get("/{destination_id}", response_model=DestinationOut)
def get_destination_by_id(destination_id: int, db: Session = Depends(get_db)):
    destination = db.query(Destination).filter(Destination.id == destination_id).first()
    if not destination:
        raise HTTPException(status_code=404, detail="Destination not found")
    return destination

@router.get("/", response_model=list[DestinationOut])
def get_all_destinations(db: Session = Depends(get_db)):
    return db.query(Destination).all()

@router.put("/{destination_id}", response_model=DestinationOut)
def update_destination(destination_id: int, destination_in: DestinationCreate, db: Session = Depends(get_db)):
    destination = db.query(Destination).filter(Destination.id == destination_id).first()
    if not destination:
        raise HTTPException(status_code=404, detail="Destination not found")
    for key, value in destination_in.model_dump().items():
        setattr(destination, key, value)
    db.commit()
    db.refresh(destination)
    return destination

@router.delete("/{destination_id}")
def delete_destination(destination_id: int, db: Session = Depends(get_db)):
    destination = db.query(Destination).filter(Destination.id == destination_id).first()
    if not destination:
        raise HTTPException(status_code=404, detail="Destination not found")
    db.delete(destination)
    db.commit()
    return {"detail": "Destination deleted successfully"}