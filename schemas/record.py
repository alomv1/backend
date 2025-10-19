from datetime import datetime, UTC
from uuid import uuid4, UUID

from pydantic import BaseModel, Field


class RecordCreate(BaseModel):
    user_id: UUID = Field(..., description="User ID")
    category_id: UUID = Field(..., description="Category ID")
    amount: float = Field(..., gt=0, description="Amount of expenses")


class RecordOut(RecordCreate):
    id: UUID = Field(default_factory=uuid4)
    created_at: datetime = Field(default_factory= lambda: datetime.now(UTC))
