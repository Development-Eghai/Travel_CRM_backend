from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from core.database import get_db
from models.quotation import Quotation
from schemas.quotation import QuotationCreate, QuotationOut
from utils.response import api_json_response_format  # Adjust path if needed

router = APIRouter()

@router.post("/")
def create_quotation(quotation_in: QuotationCreate, db: Session = Depends(get_db)):
    try:
        quotation = Quotation(**quotation_in.model_dump())
        db.add(quotation)
        db.commit()
        db.refresh(quotation)
        return api_json_response_format(True, "Quotation created successfully.", 201, QuotationOut.model_validate(quotation).model_dump())
    except Exception as e:
        return api_json_response_format(False, f"Error creating quotation: {e}", 500, {})

@router.get("/lead/{lead_id}")
def get_quotations_for_lead(lead_id: int, db: Session = Depends(get_db)):
    try:
        quotations = db.query(Quotation).filter(Quotation.lead_id == lead_id).order_by(Quotation.created_at.desc()).all()
        data = [QuotationOut.model_validate(q).model_dump() for q in quotations]
        return api_json_response_format(True, "Quotations for lead retrieved successfully.", 200, data)
    except Exception as e:
        return api_json_response_format(False, f"Error retrieving quotations for lead: {e}", 500, {})

@router.get("/{quotation_id}")
def get_quotation_by_id(quotation_id: int, db: Session = Depends(get_db)):
    try:
        quotation = db.query(Quotation).filter(Quotation.id == quotation_id).first()
        if not quotation:
            return api_json_response_format(False, "Quotation not found", 404, {})
        return api_json_response_format(True, "Quotation retrieved successfully.", 200, QuotationOut.model_validate(quotation).model_dump())
    except Exception as e:
        return api_json_response_format(False, f"Error retrieving quotation: {e}", 500, {})

@router.delete("/{quotation_id}")
def delete_quotation(quotation_id: int, db: Session = Depends(get_db)):
    try:
        quotation = db.query(Quotation).filter(Quotation.id == quotation_id).first()
        if not quotation:
            return api_json_response_format(False, "Quotation not found", 404, {})
        db.delete(quotation)
        db.commit()
        return api_json_response_format(True, "Quotation deleted successfully.", 200, {})
    except Exception as e:
        return api_json_response_format(False, f"Error deleting quotation: {e}", 500, {})