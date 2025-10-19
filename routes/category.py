from typing import List

from fastapi import APIRouter, status

from schemas.category import CategoryCreate, CategoryOut
from services.category_service import create_category_service, get_categories_service, delete_category_service

router = APIRouter()


@router.post("/category", response_model=CategoryOut, status_code=status.HTTP_201_CREATED)
def create_category(category: CategoryCreate):
    return create_category_service(category)


@router.get("/category", response_model=List[CategoryOut], status_code=status.HTTP_200_OK)
def get_categories():
    return get_categories_service()


@router.delete("/category", status_code=status.HTTP_204_NO_CONTENT)
def delete_category(category_id):
    delete_category_service(category_id)
