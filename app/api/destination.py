from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from schemas.destination import DestinationCreate, DestinationOut
from models.destination import Destination
from core.database import get_db
from utils.response import api_json_response_format  # Adjust path if needed

router = APIRouter()

@router.post("/")
def create_destination(destination_in: DestinationCreate, db: Session = Depends(get_db)):
    try:
        destination = Destination(**destination_in.model_dump())
        db.add(destination)
        db.commit()
        db.refresh(destination)
        return api_json_response_format(True, "Destination created successfully.", 201, DestinationOut.model_validate(destination).model_dump())
    except Exception as e:
        return api_json_response_format(False, f"Error creating destination: {e}", 500, {})

@router.get("/{destination_id}")
def get_destination_by_id(destination_id: int, db: Session = Depends(get_db)):
    try:
        destination = db.query(Destination).filter(Destination.id == destination_id).first()
        if not destination:
            return api_json_response_format(False, "Destination not found", 404, {})
        return api_json_response_format(True, "Destination retrieved successfully.", 200, DestinationOut.model_validate(destination).model_dump())
    except Exception as e:
        return api_json_response_format(False, f"Error retrieving destination: {e}", 500, {})

@router.get("/")
def get_all_destinations(db: Session = Depends(get_db)):
    try:
        destinations = db.query(Destination).all()
        data = [DestinationOut.model_validate(d).model_dump() for d in destinations]
        return api_json_response_format(True, "Destinations retrieved successfully.", 200, data)
    except Exception as e:
        return api_json_response_format(False, f"Error retrieving destinations: {e}", 500, {})

@router.put("/{destination_id}")
def update_destination(destination_id: int, destination_in: DestinationCreate, db: Session = Depends(get_db)):
    try:
        destination = db.query(Destination).filter(Destination.id == destination_id).first()
        if not destination:
            return api_json_response_format(False, "Destination not found", 404, {})
        for key, value in destination_in.model_dump().items():
            setattr(destination, key, value)
        db.commit()
        db.refresh(destination)
        return api_json_response_format(True, "Destination updated successfully.", 200, DestinationOut.model_validate(destination).model_dump())
    except Exception as e:
        return api_json_response_format(False, f"Error updating destination: {e}", 500, {})

@router.delete("/{destination_id}")
def delete_destination(destination_id: int, db: Session = Depends(get_db)):
    try:
        destination = db.query(Destination).filter(Destination.id == destination_id).first()
        if not destination:
            return api_json_response_format(False, "Destination not found", 404, {})
        db.delete(destination)
        db.commit()
        return api_json_response_format(True, "Destination deleted successfully.", 200, {})
    except Exception as e:
        return api_json_response_format(False, f"Error deleting destination: {e}", 500, {})