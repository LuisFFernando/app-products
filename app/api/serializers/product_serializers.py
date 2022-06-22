from datetime import date
from pydantic import BaseModel, Field
from pydantic import validator
from typing import Optional

from enum import Enum


class CreateProductSerializer(BaseModel):
    name: str
    brand: str
    quantity: str
    sku: str
    initial_value: str
    description: str
    profit_percentage: str
    extra_data: str
    user_id: int
    category_id: int


class Order(str, Enum):
    asc = 'ASC'
    desc = 'DESC'


class ParamProductGetSerializer(BaseModel):
    """."""
    id: Optional[int]
    name: Optional[str]
    sku: Optional[str]
    brand: Optional[str]
    # order: Order
    item_per_page: int
    page: int = Field(1, ge=1)


class ProductDeserializer(BaseModel):
    id: int
    name: str
    brand: str
    quantity: str
    sku: str
    initial_value: str
    description: str
    profit_percentage: str
    extra_data: str
    category_id: int
    category_name: str
    history_query: int

    user_id: int
    active: bool
    created_at:  Optional[date] = None
    updated_at: Optional[date] = None
    deleted_at: Optional[date] = None

    @validator("created_at")
    def cast_created_at(cls, created_at):
        return str(created_at)

    @validator("updated_at")
    def cast_updated_at(cls, updated_at):
        return str(updated_at)

    @validator("deleted_at")
    def cast_deleted_at(cls, deleted_at):
        return str(deleted_at)

    class Config:
        orm_mode = True
        arbitrary_types_allowed = True
        use_enum_values = True


class UpdateProductSerializer(BaseModel):
    name: str
    brand: str
    quantity: str
    sku: str
    initial_value: str
    profit_percentage: str
    category_id: int
