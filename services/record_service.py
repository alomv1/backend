from fastapi import HTTPException, status
from typing import List, Optional
from schemas.record import RecordCreate, RecordOut

records = {}


def create_record_service(record: RecordCreate) -> RecordOut:
    record_out = RecordOut(**record.model_dump())
    records[str(record_out.id)] = record_out
    return record_out


def get_record_service(record_id: str) -> RecordOut:
    record = records.get(str(record_id))
    if not record:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Record not found")
    return record


def get_records_service(user_id: Optional[str] = None, category_id: Optional[str] = None) -> List[RecordOut]:
    if not user_id and not category_id:
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail="At least one filter must be provided")

    filtered = list(records.values())

    if user_id:
        filtered = [r for r in filtered if str(r.user_id) == user_id]
    if category_id:
        filtered = [r for r in filtered if str(r.category_id) == category_id]

    return filtered


def delete_record_service(record_id: str):
    if record_id not in records:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Record not found")
    del records[record_id]