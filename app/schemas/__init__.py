from app.schemas.base import BaseSchema
from app.schemas.user import User, UserCreate, UserUpdate
from app.schemas.location import Location, LocationCreate, LocationUpdate
from app.schemas.supplier import Supplier, SupplierCreate, SupplierUpdate
from app.schemas.vehicle import Vehicle, VehicleCreate, VehicleUpdate
from app.schemas.part import Part, PartCreate, PartUpdate
from app.schemas.purchase import Purchase, PurchaseCreate, PurchaseUpdate
from app.schemas.warranty import Warranty, WarrantyCreate, WarrantyUpdate
from app.schemas.warranty_part import WarrantyPart, WarrantyPartCreate, WarrantyPartUpdate

__all__ = [
    "BaseSchema",
    "User",
    "UserCreate",
    "UserUpdate",
    "Location",
    "LocationCreate",
    "LocationUpdate",
    "Supplier",
    "SupplierCreate",
    "SupplierUpdate",
    "Vehicle",
    "VehicleCreate",
    "VehicleUpdate",
    "Part",
    "PartCreate",
    "PartUpdate",
    "Purchase",
    "PurchaseCreate",
    "PurchaseUpdate",
    "Warranty",
    "WarrantyCreate",
    "WarrantyUpdate",
    "WarrantyPart",
    "WarrantyPartCreate",
    "WarrantyPartUpdate",
] 