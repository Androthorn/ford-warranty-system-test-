from typing import Optional
from pydantic import BaseModel

from app.schemas.base import BaseSchema

class LocationBase(BaseModel):
    name: str
    address: str
    city: str
    state: str
    country: str
    postal_code: str

class LocationCreate(LocationBase):
    pass

class LocationUpdate(LocationBase):
    name: Optional[str] = None
    address: Optional[str] = None
    city: Optional[str] = None
    state: Optional[str] = None
    country: Optional[str] = None
    postal_code: Optional[str] = None

class Location(LocationBase, BaseSchema):
    pass 