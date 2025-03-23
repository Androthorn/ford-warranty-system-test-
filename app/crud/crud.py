from typing import List, Optional
from sqlalchemy.orm import Session
from sqlalchemy import func

from app.crud.base import CRUDBase
from app.models.models import Location, Supplier, Vehicle, Part, Purchase, Warranty
from app.schemas.schemas import (
    LocationCreate, LocationUpdate,
    SupplierCreate, SupplierUpdate,
    VehicleCreate, VehicleUpdate,
    PartCreate, PartUpdate,
    PurchaseCreate, PurchaseUpdate,
    WarrantyCreate, WarrantyUpdate
)

class CRUDLocation(CRUDBase[Location, LocationCreate, LocationUpdate]):
    def get_by_market(self, db: Session, *, market: str) -> List[Location]:
        return db.query(Location).filter(Location.market == market).all()

    def get_by_country(self, db: Session, *, country: str) -> List[Location]:
        return db.query(Location).filter(Location.country == country).all()

location = CRUDLocation(Location)

class CRUDSupplier(CRUDBase[Supplier, SupplierCreate, SupplierUpdate]):
    def get_by_location(self, db: Session, *, location_id: int) -> List[Supplier]:
        return db.query(Supplier).filter(Supplier.location_id == location_id).all()

    def get_by_name(self, db: Session, *, name: str) -> Optional[Supplier]:
        return db.query(Supplier).filter(Supplier.name == name).first()

supplier = CRUDSupplier(Supplier)

class CRUDVehicle(CRUDBase[Vehicle, VehicleCreate, VehicleUpdate]):
    def get_by_model(self, db: Session, *, model: str) -> List[Vehicle]:
        return db.query(Vehicle).filter(Vehicle.model == model).all()

    def get_by_year(self, db: Session, *, year: int) -> List[Vehicle]:
        return db.query(Vehicle).filter(Vehicle.year == year).all()

    def get_by_propulsion(self, db: Session, *, propulsion: str) -> List[Vehicle]:
        return db.query(Vehicle).filter(Vehicle.propulsion == propulsion).all()

vehicle = CRUDVehicle(Vehicle)

class CRUDPart(CRUDBase[Part, PartCreate, PartUpdate]):
    def get_by_supplier(self, db: Session, *, supplier_id: int) -> List[Part]:
        return db.query(Part).filter(Part.supplier_id == supplier_id).all()

    def get_by_name(self, db: Session, *, name: str) -> Optional[Part]:
        return db.query(Part).filter(Part.name == name).first()

part = CRUDPart(Part)

class CRUDPurchase(CRUDBase[Purchase, PurchaseCreate, PurchaseUpdate]):
    def get_by_type(self, db: Session, *, purchase_type: str) -> List[Purchase]:
        return db.query(Purchase).filter(Purchase.purchase_type == purchase_type).all()

    def get_by_part(self, db: Session, *, part_id: int) -> List[Purchase]:
        return db.query(Purchase).filter(Purchase.part_id == part_id).all()

    def get_by_date_range(self, db: Session, *, start_date: str, end_date: str) -> List[Purchase]:
        return db.query(Purchase).filter(
            Purchase.purchase_date.between(start_date, end_date)
        ).all()

purchase = CRUDPurchase(Purchase)

class CRUDWarranty(CRUDBase[Warranty, WarrantyCreate, WarrantyUpdate]):
    def get_by_vehicle(self, db: Session, *, vehicle_id: int) -> List[Warranty]:
        return db.query(Warranty).filter(Warranty.vehicle_id == vehicle_id).all()

    def get_by_part(self, db: Session, *, part_id: int) -> List[Warranty]:
        return db.query(Warranty).filter(Warranty.part_id == part_id).all()

    def get_by_location(self, db: Session, *, location_id: int) -> List[Warranty]:
        return db.query(Warranty).filter(Warranty.location_id == location_id).all()

    def get_by_date_range(self, db: Session, *, start_date: str, end_date: str) -> List[Warranty]:
        return db.query(Warranty).filter(
            Warranty.repair_date.between(start_date, end_date)
        ).all()

    def get_by_failure_type(self, db: Session, *, failure_type: str) -> List[Warranty]:
        return db.query(Warranty).filter(Warranty.classified_failure == failure_type).all()

warranty = CRUDWarranty(Warranty) 