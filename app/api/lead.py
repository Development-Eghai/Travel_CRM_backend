from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from core.database import get_db
from models.lead import Lead
from schemas.lead import LeadCreate, LeadOut
from utils.response import api_json_response_format  # Adjust path if needed

router = APIRouter()

@router.post("/")
def create_lead(lead_in: LeadCreate, db: Session = Depends(get_db)):
    try:
        lead = Lead(**lead_in.model_dump())
        db.add(lead)
        db.commit()
        db.refresh(lead)
        return api_json_response_format(True, "Lead created successfully.", 201, LeadOut.model_validate(lead).model_dump())
    except Exception as e:
        return api_json_response_format(False, f"Error creating lead: {e}", 500, {})

@router.get("/")
def get_all_leads(db: Session = Depends(get_db)):
    try:
        leads = db.query(Lead).all()
        data = [LeadOut.model_validate(l).model_dump() for l in leads]
        return api_json_response_format(True, "Leads retrieved successfully.", 200, data)
    except Exception as e:
        return api_json_response_format(False, f"Error retrieving leads: {e}", 500, {})

@router.get("/{lead_id}")
def get_lead_by_id(lead_id: int, db: Session = Depends(get_db)):
    try:
        lead = db.query(Lead).filter(Lead.id == lead_id).first()
        if not lead:
            return api_json_response_format(False, "Lead not found", 404, {})
        return api_json_response_format(True, "Lead retrieved successfully.", 200, LeadOut.model_validate(lead).model_dump())
    except Exception as e:
        return api_json_response_format(False, f"Error retrieving lead: {e}", 500, {})

@router.put("/{lead_id}")
def update_lead(lead_id: int, lead_in: LeadCreate, db: Session = Depends(get_db)):
    try:
        lead = db.query(Lead).filter(Lead.id == lead_id).first()
        if not lead:
            return api_json_response_format(False, "Lead not found", 404, {})
        for key, value in lead_in.model_dump().items():
            setattr(lead, key, value)
        db.commit()
        db.refresh(lead)
        return api_json_response_format(True, "Lead updated successfully.", 200, LeadOut.model_validate(lead).model_dump())
    except Exception as e:
        return api_json_response_format(False, f"Error updating lead: {e}", 500, {})

@router.delete("/{lead_id}")
def delete_lead(lead_id: int, db: Session = Depends(get_db)):
    try:
        lead = db.query(Lead).filter(Lead.id == lead_id).first()
        if not lead:
            return api_json_response_format(False, "Lead not found", 404, {})
        db.delete(lead)
        db.commit()
        return api_json_response_format(True, "Lead deleted successfully.", 200, {})
    except Exception as e:
        return api_json_response_format(False, f"Error deleting lead: {e}", 500, {})