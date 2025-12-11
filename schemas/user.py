from pydantic import BaseModel, Field, ConfigDict
from uuid import UUID

class UserCreate(BaseModel):
    name: str = Field(..., title='username', description='enter username:')
    password: str = Field(..., min_length=5, description="User password")

class UserOut(UserCreate):
    id: UUID

    model_config = ConfigDict(from_attributes=True)