from typing import Optional
from pydantic import BaseModel, validator

from app.schemas.base import BaseSchema

class WarrantyPartBase(BaseModel):
    warranty_id: int
    part_id: int
    supplier_id: int
    quantity: int
    unit_price: float
    total_price: float
    notes: Optional[str] = None

    @validator('quantity')
    def validate_quantity(cls, v):
        if v <= 0:
            raise ValueError('Quantity must be greater than 0')
        return v

    @validator('unit_price')
    def validate_unit_price(cls, v):
        if v <= 0:
            raise ValueError('Unit price must be greater than 0')
        return v

    @validator('total_price')
    def validate_total_price(cls, v, values):
        if 'quantity' in values and 'unit_price' in values:
            expected_total = values['quantity'] * values['unit_price']
            if abs(v - expected_total) > 0.01:  # Allow small floating point differences
                raise ValueError(f'Total price must be equal to quantity * unit_price ({expected_total})')
        return v

class WarrantyPartCreate(WarrantyPartBase):
    pass

class WarrantyPartUpdate(WarrantyPartBase):
    warranty_id: Optional[int] = None
    part_id: Optional[int] = None
    supplier_id: Optional[int] = None
    quantity: Optional[int] = None
    unit_price: Optional[float] = None
    total_price: Optional[float] = None
    notes: Optional[str] = None

class WarrantyPart(WarrantyPartBase, BaseSchema):
    pass 