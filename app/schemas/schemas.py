from datetime import date
from typing import Optional
from pydantic import BaseModel
from app.schemas.base import BaseSchema
from app.models.models import PropulsionType, PurchaseType

# Location Schemas
class LocationBase(BaseModel):
    market: str
    country: str
    province: str
    city: str

class LocationCreate(LocationBase):
    pass

class Location(LocationBase, BaseSchema):
    pass

# Supplier Schemas
class SupplierBase(BaseModel):
    name: str
    location_id: int

class SupplierCreate(SupplierBase):
    pass

class Supplier(SupplierBase, BaseSchema):
    location: Location

# Vehicle Schemas
class VehicleBase(BaseModel):
    model: str
    prod_date: date
    year: int
    propulsion: PropulsionType

class VehicleCreate(VehicleBase):
    pass

class Vehicle(VehicleBase, BaseSchema):
    pass

# Part Schemas
class PartBase(BaseModel):
    name: str
    supplier_id: int
    last_purchase_id: int

class PartCreate(PartBase):
    pass

class Part(PartBase, BaseSchema):
    supplier: Supplier

# Purchase Schemas
class PurchaseBase(BaseModel):
    purchase_type: PurchaseType
    purchase_date: date
    part_id: int

class PurchaseCreate(PurchaseBase):
    pass

class Purchase(PurchaseBase, BaseSchema):
    part: Part

# Warranty Schemas
class WarrantyBase(BaseModel):
    vehicle_id: int
    repair_date: date
    client_comment: Optional[str] = None
    tech_comment: str
    part_id: int
    classified_failure: str
    location_id: int
    purchase_id: int

class WarrantyCreate(WarrantyBase):
    pass

class Warranty(WarrantyBase, BaseSchema):
    vehicle: Vehicle
    part: Part
    location: Location
    purchase: Purchase 