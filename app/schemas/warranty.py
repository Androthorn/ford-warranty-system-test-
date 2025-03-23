from typing import Optional
from datetime import date
from pydantic import BaseModel, validator

from app.schemas.base import BaseSchema

class WarrantyBase(BaseModel):
    vehicle_id: int
    part_id: int
    location_id: int
    failure_type: str
    failure_date: date
    description: str
    status: str
    resolution_date: Optional[date] = None
    resolution_description: Optional[str] = None

    @validator('resolution_date')
    def validate_resolution_date(cls, v, values):
        if v and 'failure_date' in values and v < values['failure_date']:
            raise ValueError('Resolution date must be after failure date')
        return v

    @validator('status')
    def validate_status(cls, v):
        valid_statuses = ['pending', 'in_progress', 'resolved', 'cancelled']
        if v not in valid_statuses:
            raise ValueError(f'Status must be one of {valid_statuses}')
        return v

class WarrantyCreate(WarrantyBase):
    pass

class WarrantyUpdate(WarrantyBase):
    vehicle_id: Optional[int] = None
    part_id: Optional[int] = None
    location_id: Optional[int] = None
    failure_type: Optional[str] = None
    failure_date: Optional[date] = None
    description: Optional[str] = None
    status: Optional[str] = None
    resolution_date: Optional[date] = None
    resolution_description: Optional[str] = None

class Warranty(WarrantyBase, BaseSchema):
    pass 