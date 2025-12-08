import uuid
from typing import List, Optional
from sqlalchemy.orm import Session
from fastapi import HTTPException, status

from models import Record
from schemas.record import RecordCreate


def create_record_service(record: RecordCreate, db: Session) -> Record:
    db_record = Record(**record.model_dump())

    db.add(db_record)
    db.commit()
    db.refresh(db_record)

    return db_record


def get_record_service(record_id: uuid.UUID, db: Session) -> Record:
    record = db.query(Record).filter(Record.id == record_id).first()

    if not record:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Record not found"
        )
    return record


def get_records_service(
        db: Session,
        user_id: Optional[uuid.UUID] = None,
        category_id: Optional[uuid.UUID] = None
) -> List[Record]:
    query = db.query(Record)

    if user_id:
        query = query.filter(Record.user_id == user_id)
    if category_id:
        query = query.filter(Record.category_id == category_id)

    if not user_id and not category_id:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail="At least one filter (user_id or category_id) must be provided"
        )

    return query.all()


def delete_record_service(record_id: uuid.UUID, db: Session) -> None:
    record = db.query(Record).filter(Record.id == record_id).first()

    if not record:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Record not found"
        )

    db.delete(record)
    db.commit()