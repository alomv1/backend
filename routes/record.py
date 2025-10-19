from typing import List, Optional

from fastapi import APIRouter, status

from schemas.record import RecordCreate, RecordOut
from services.record_service import create_record_service, get_record_service, get_records_service, \
    delete_record_service

router = APIRouter()


@router.post("/record", response_model=RecordOut, status_code=status.HTTP_201_CREATED)
def create_record(record: RecordCreate):
    return create_record_service(record)


@router.get("/record", response_model=List[RecordOut], status_code=status.HTTP_200_OK)
def get_records(user_id: Optional[str], category_id: Optional[str]):
    return get_records_service(user_id=user_id, category_id=category_id)


@router.get("/record/{record_id}", response_model=RecordOut, status_code=status.HTTP_200_OK)
def get_record(record_id: str):
    return get_record_service(record_id)


@router.delete("/record/{record_id}", status_code=status.HTTP_204_NO_CONTENT)
def delete_record(record_id: str):
    delete_record_service(record_id)
