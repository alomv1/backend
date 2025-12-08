import uuid
from typing import List

from fastapi import APIRouter, status, Depends
from sqlalchemy.orm import Session

from database import get_db
from schemas.user import UserOut, UserCreate
import services.user_service as user_service

router = APIRouter()

@router.post('/user', response_model=UserOut, status_code=status.HTTP_201_CREATED)
def create_user(user: UserCreate, db: Session = Depends(get_db)):
    return user_service.create_user_service(user, db)

@router.get('/users', response_model=List[UserOut], status_code=status.HTTP_200_OK)
def get_users(db: Session = Depends(get_db)):
    return user_service.get_users_service(db)

@router.get('/user/{user_id}', response_model=UserOut, status_code=status.HTTP_200_OK)
def get_user(user_id: uuid.UUID, db: Session = Depends(get_db)):
    return user_service.get_user_service(user_id, db)

@router.delete('/user/{user_id}', status_code=status.HTTP_204_NO_CONTENT)
def delete_user(user_id: uuid.UUID, db: Session = Depends(get_db)):
    user_service.delete_user_service(user_id, db)