from pydantic import BaseModel, Field
from uuid import uuid4

class UserCreate(BaseModel):
    name: str = Field(..., title='username', description='enter username:')

class UserOut(UserCreate):
    id: str = Field(default_factory=uuid4)