import uuid
from typing import List
from sqlalchemy.orm import Session

from models import Category
from schemas.category import CategoryCreate


def create_category_service(category: CategoryCreate, db: Session) -> Category:
    db_category = Category(name=category.name)

    db.add(db_category)
    db.commit()
    db.refresh(db_category)

    return db_category


def get_categories_service(db: Session) -> List[Category]:
    return db.query(Category).all()


def delete_category_service(category_id: uuid.UUID, db: Session) -> None:
    category = db.query(Category).filter(Category.id == category_id).first()
    db.delete(category)
    db.commit()