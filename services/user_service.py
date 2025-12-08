import uuid

from sqlalchemy.orm import Session
from fastapi import HTTPException, status

from models import User
from schemas.user import UserCreate


def create_user_service(user: UserCreate, db: Session) -> User:
    db_user = User(name=user.name)

    db.add(db_user)
    db.commit()
    db.refresh(db_user)

    return db_user


def get_users_service(db: Session) -> list[type[User]]:
    return db.query(User).all()


def get_user_service(user_id: uuid.UUID, db: Session) -> User:
    user = db.query(User).filter(User.id == user_id).first()

    if not user:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="User was not found"
        )
    return user


def delete_user_service(user_id: uuid.UUID, db: Session) -> None:
    user = db.query(User).filter(User.id == user_id).first()

    if not user:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="User was not found"
        )

    db.delete(user)
    db.commit()