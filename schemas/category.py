from pydantic import BaseModel, Field
from uuid import uuid4

class CategoryCreate(BaseModel):
    name: str = Field(..., title="Category name", description="Enter category name")

class CategoryOut(CategoryCreate):
    id: str = Field(default_factory=uuid4)
