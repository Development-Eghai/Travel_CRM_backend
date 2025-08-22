from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from typing import List
from app.schemas.blog_category import BlogCategoryCreate, BlogCategoryOut
from app.models.blog_category import BlogCategory
from app.core.database import get_db

router = APIRouter()

@router.post("/", response_model=BlogCategoryOut)
def create_blog_category(cat_in: BlogCategoryCreate, db: Session = Depends(get_db)):
    category = BlogCategory(**cat_in.model_dump())
    db.add(category)
    db.commit()
    db.refresh(category)
    return category

@router.get("/", response_model=List[BlogCategoryOut])
def list_blog_categories(db: Session = Depends(get_db)):
    return db.query(BlogCategory).filter(BlogCategory.is_active == True).order_by(BlogCategory.sort_order).all()

@router.get("/{category_id}", response_model=BlogCategoryOut)
def get_blog_category(category_id: int, db: Session = Depends(get_db)):
    category = db.query(BlogCategory).filter(BlogCategory.id == category_id).first()
    if not category:
        raise HTTPException(status_code=404, detail="Category not found")
    return category

@router.put("/{category_id}", response_model=BlogCategoryOut)
def update_blog_category(category_id: int, cat_in: BlogCategoryCreate, db: Session = Depends(get_db)):
    category = db.query(BlogCategory).filter(BlogCategory.id == category_id).first()
    if not category:
        raise HTTPException(status_code=404, detail="Category not found")
    for key, value in cat_in.model_dump().items():
        setattr(category, key, value)
    db.commit()
    db.refresh(category)
    return category

@router.delete("/{category_id}")
def delete_blog_category(category_id: int, db: Session = Depends(get_db)):
    category = db.query(BlogCategory).filter(BlogCategory.id == category_id).first()
    if not category:
        raise HTTPException(status_code=404, detail="Category not found")
    db.delete(category)
    db.commit()
    return {"detail": "Category deleted"}