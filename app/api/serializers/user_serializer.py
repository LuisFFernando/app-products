from datetime import date
from pydantic import BaseModel
from pydantic import validator
from typing import Optional

from enum import Enum

class CreateUserSerializer(BaseModel):
    first_name: str
    last_name: str
    nid: str
    address: str
    phone: str
    email: str
    user_profile: int


class Order(str, Enum):
    asc = 'ASC'
    desc = 'DESC'


class ParamUserGetSerializer(BaseModel):
    """."""
    id: Optional[int]
    nid: Optional[int]
    email: Optional[str]
    phone: Optional[int]


class UserDeserializer(BaseModel):
    id : int
    first_name: str
    last_name: str
    nid: str
    address: str
    phone: str
    email: str
    list_profile: Optional[list] = []
    active: bool
    created_at:  Optional[date] = None
    updated_at: Optional[date] = None
    deleted_at: Optional[date] = None

    @validator("created_at")
    def cast_created_at(cls, created_at):
        return str(created_at)

    @validator("created_at")
    def cast_updated_at(cls, updated_at):
        return str(updated_at)

    @validator("deleted_at")
    def cast_deleted_at(cls, deleted_at):
        return str(deleted_at)

    class Config:
        orm_mode = True
        arbitrary_types_allowed = True
        use_enum_values = True
