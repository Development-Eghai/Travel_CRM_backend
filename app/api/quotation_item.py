from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from typing import List
from app.schemas.quotation_item import QuotationItemCreate, QuotationItemOut
from app.models.quotation_item import QuotationItem
from app.core.database import get_db

router = APIRouter()

@router.post("/", response_model=QuotationItemOut)
def create_item(item_in: QuotationItemCreate, db: Session = Depends(get_db)):
    item = QuotationItem(**item_in.model_dump())
    db.add(item)
    db.commit()
    db.refresh(item)
    return item

@router.get("/", response_model=List[QuotationItemOut])
def get_all_items(db: Session = Depends(get_db)):
    return db.query(QuotationItem).order_by(QuotationItem.created_at.desc()).all()

@router.get("/{quotation_id}", response_model=List[QuotationItemOut])
def get_items_for_quotation(quotation_id: int, db: Session = Depends(get_db)):
    return db.query(QuotationItem).filter(QuotationItem.quotation_id == quotation_id).order_by(QuotationItem.sort_order).all()

@router.put("/{item_id}", response_model=QuotationItemOut)
def update_item(item_id: int, item_in: QuotationItemCreate, db: Session = Depends(get_db)):
    item = db.query(QuotationItem).filter(QuotationItem.id == item_id).first()
    if not item:
        raise HTTPException(status_code=404, detail="Item not found")
    for key, value in item_in.model_dump().items():
        setattr(item, key, value)
    db.commit()
    db.refresh(item)
    return item

@router.delete("/{item_id}")
def delete_item(item_id: int, db: Session = Depends(get_db)):
    item = db.query(QuotationItem).filter(QuotationItem.id == item_id).first()
    if not item:
        raise HTTPException(status_code=404, detail="Item not found")
    db.delete(item)
    db.commit()
    return {"detail": "Item deleted"}