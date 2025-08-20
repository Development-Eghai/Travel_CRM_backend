from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from app.core.database import get_db
from app.models.quotation import Quotation
from app.schemas.quotation import QuotationCreate, QuotationOut

router = APIRouter()

@router.post("/", response_model=QuotationOut)
def create_quotation(quotation_in: QuotationCreate, db: Session = Depends(get_db)):
    quotation = Quotation(**quotation_in.dict())
    db.add(quotation)
    db.commit()
    db.refresh(quotation)
    return quotation

@router.get("/lead/{lead_id}", response_model=list[QuotationOut])
def get_quotations_for_lead(lead_id: int, db: Session = Depends(get_db)):
    return db.query(Quotation).filter(Quotation.lead_id == lead_id).order_by(Quotation.created_at.desc()).all()

@router.get("/{quotation_id}", response_model=QuotationOut)
def get_quotation_by_id(quotation_id: int, db: Session = Depends(get_db)):
    quotation = db.query(Quotation).filter(Quotation.id == quotation_id).first()
    if not quotation:
        raise HTTPException(status_code=404, detail="Quotation not found")
    return quotation

@router.delete("/{quotation_id}")
def delete_quotation(quotation_id: int, db: Session = Depends(get_db)):
    quotation = db.query(Quotation).filter(Quotation.id == quotation_id).first()
    if not quotation:
        raise HTTPException(status_code=404, detail="Quotation not found")
    db.delete(quotation)
    db.commit()
    return {"detail": "Quotation deleted successfully"}