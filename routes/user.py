from typing import List

from fastapi import APIRouter, status

from schemas.user import UserOut, UserCreate
from services.user_service import create_user_service, get_user_service, get_users_service, delete_user_service

router = APIRouter()


@router.post('/user', response_model=UserOut, status_code=status.HTTP_201_CREATED)
def create_user(user: UserCreate):
    return create_user_service(user)


@router.get('/users', response_model=List[UserOut], status_code=status.HTTP_200_OK)
def get_users():
    return get_users_service


@router.get('/user/{user_id}', response_model=UserOut, status_code=status.HTTP_200_OK)
def get_user(user_id):
    return get_user_service(user_id=user_id)


@router.delete('/user/user_id', status_code=status.HTTP_204_NO_CONTENT)
def delete_user(user_id):
    return delete_user_service(user_id=user_id)
