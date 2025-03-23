from typing import Any, Dict, Optional, Union, List
from datetime import date
from sqlalchemy.orm import Session

from app.crud.base import CRUDBase
from app.models.warranty import Warranty
from app.schemas.warranty import WarrantyCreate, WarrantyUpdate

class CRUDWarranty(CRUDBase[Warranty, WarrantyCreate, WarrantyUpdate]):
    def get_by_vehicle(self, db: Session, *, vehicle_id: int) -> List[Warranty]:
        return db.query(self.model).filter(self.model.vehicle_id == vehicle_id).all()

    def get_by_part(self, db: Session, *, part_id: int) -> List[Warranty]:
        return db.query(self.model).filter(self.model.part_id == part_id).all()

    def get_by_location(self, db: Session, *, location_id: int) -> List[Warranty]:
        return db.query(self.model).filter(self.model.location_id == location_id).all()

    def get_by_date_range(
        self, db: Session, *, start_date: date, end_date: date
    ) -> List[Warranty]:
        return (
            db.query(self.model)
            .filter(self.model.failure_date.between(start_date, end_date))
            .all()
        )

    def get_by_failure_type(self, db: Session, *, failure_type: str) -> List[Warranty]:
        return db.query(self.model).filter(self.model.failure_type == failure_type).all()

warranty = CRUDWarranty(Warranty) 