# app/api/blog_post.py
from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from typing import List
from schemas.blog_post import BlogPostCreate, BlogPostOut
from models.blog_post import BlogPost
from core.database import get_db

router = APIRouter()

@router.post("/", response_model=BlogPostOut)
def create_blog(blog_in: BlogPostCreate, db: Session = Depends(get_db)):
    blog = BlogPost(**blog_in.model_dump())
    db.add(blog)
    db.commit()
    db.refresh(blog)
    return blog

@router.get("/", response_model=List[BlogPostOut])
def get_blogs(db: Session = Depends(get_db)):
    return db.query(BlogPost).all()

@router.get("/{blog_id}", response_model=BlogPostOut)
def get_blog(blog_id: int, db: Session = Depends(get_db)):
    blog = db.query(BlogPost).filter(BlogPost.id == blog_id).first()
    if not blog:
        raise HTTPException(status_code=404, detail="Blog post not found")
    return blog

@router.put("/{blog_id}", response_model=BlogPostOut)
def update_blog(blog_id: int, blog_in: BlogPostCreate, db: Session = Depends(get_db)):
    blog = db.query(BlogPost).filter(BlogPost.id == blog_id).first()
    if not blog:
        raise HTTPException(status_code=404, detail="Blog post not found")
    for key, value in blog_in.model_dump().items():
        setattr(blog, key, value)
    db.commit()
    db.refresh(blog)
    return blog

@router.delete("/{blog_id}")
def delete_blog(blog_id: int, db: Session = Depends(get_db)):
    blog = db.query(BlogPost).filter(BlogPost.id == blog_id).first()
    if not blog:
        raise HTTPException(status_code=404, detail="Blog post not found")
    db.delete(blog)
    db.commit()
    return {"detail": "Blog post deleted"}