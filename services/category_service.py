from fastapi import HTTPException, status
from schemas.category import CategoryCreate, CategoryOut
from typing import List

categories = {}

def create_category_service(category: CategoryCreate) -> CategoryOut:
    category_out = CategoryOut(name=category.name)
    categories[category_out.id] = category_out
    return category_out

def get_categories_service() -> List[CategoryOut]:
    return list(categories.values())

def delete_category_service(category_id: str) -> None:
    if category_id not in categories:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Category not found")
    del categories[category_id]
    return
