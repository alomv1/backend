import uuid
from typing import List

from fastapi import APIRouter, status, Depends
from sqlalchemy.orm import Session

from database import get_db
from schemas.category import CategoryCreate, CategoryOut
import services.category_service as category_service

router = APIRouter()

@router.post("/category", response_model=CategoryOut, status_code=status.HTTP_201_CREATED)
def create_category(category: CategoryCreate, db: Session = Depends(get_db)):
    return category_service.create_category_service(category, db)

@router.get("/category", response_model=List[CategoryOut], status_code=status.HTTP_200_OK)
def get_categories(db: Session = Depends(get_db)):
    return category_service.get_categories_service(db)

@router.delete("/category/{category_id}", status_code=status.HTTP_204_NO_CONTENT)
def delete_category(category_id: uuid.UUID, db: Session = Depends(get_db)):
    category_service.delete_category_service(category_id, db)