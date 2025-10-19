import uuid

from fastapi import status, HTTPException
from typing import List
from schemas.user import UserOut, UserCreate

users = {}


def create_user_service(user: UserCreate) -> UserOut:
    user_out = UserOut(name=user.name)

    users[user_out.id] = user_out

    return user_out


def get_users_service() -> List[UserOut]:
    return list(users.values())


def get_user_service(user_id: uuid.UUID) -> UserOut:
    user = users.get(user_id)

    if not user:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail='User was not found')

    return user


def delete_user_service(user_id: uuid.UUID) -> None:
    if user_id not in users:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail='User was not found')

    del users[user_id]

    return
