from datetime import datetime
from uuid import UUID
from pydantic import BaseModel, Field, ConfigDict

class RecordCreate(BaseModel):
    user_id: UUID = Field(..., description="User ID")
    category_id: UUID = Field(..., description="Category ID")
    amount: float = Field(..., gt=0, description="Amount of expenses")

class RecordOut(RecordCreate):
    id: UUID
    created_at: datetime

    model_config = ConfigDict(from_attributes=True)