# app/api/categories.py
from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from typing import List
from app.schemas.category import CategoryCreate, CategoryOut
from app.models.category import Category
from app.core.database import get_db

router = APIRouter()

@router.post("/", response_model=CategoryOut)
def create_category(category_in: CategoryCreate, db: Session = Depends(get_db)):
    category = Category(**category_in.model_dump())
    db.add(category)
    db.commit()
    db.refresh(category)
    return category

@router.get("/{category_id}", response_model=CategoryOut)
def get_category_by_id(category_id: int, db: Session = Depends(get_db)):
    category = db.query(Category).filter(Category.id == category_id).first()
    if not category:
        raise HTTPException(status_code=404, detail="Category not found")
    return category

@router.get("/", response_model=List[CategoryOut])
def get_all_categories(db: Session = Depends(get_db)):
    return db.query(Category).all()

@router.put("/{category_id}", response_model=CategoryOut)
def update_category(category_id: int, category_in: CategoryCreate, db: Session = Depends(get_db)):
    category = db.query(Category).filter(Category.id == category_id).first()
    if not category:
        raise HTTPException(status_code=404, detail="Category not found")
    for key, value in category_in.model_dump().items():
        setattr(category, key, value)
    db.commit()
    db.refresh(category)
    return category

@router.delete("/{category_id}")
def delete_category(category_id: int, db: Session = Depends(get_db)):
    category = db.query(Category).filter(Category.id == category_id).first()
    if not category:
        raise HTTPException(status_code=404, detail="Category not found")
    db.delete(category)
    db.commit()
    return {"detail": "Category deleted successfully"}
