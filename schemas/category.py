from pydantic import BaseModel, Field, ConfigDict
from uuid import UUID


class CategoryCreate(BaseModel):
    name: str = Field(..., title="Category name", description="Enter category name")


class CategoryOut(CategoryCreate):
    id: UUID

    model_config = ConfigDict(from_attributes=True)