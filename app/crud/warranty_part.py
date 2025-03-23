from typing import Any, Dict, Optional, Union, List
from sqlalchemy.orm import Session

from app.crud.base import CRUDBase
from app.models.warranty_part import WarrantyPart
from app.schemas.warranty_part import WarrantyPartCreate, WarrantyPartUpdate

class CRUDWarrantyPart(CRUDBase[WarrantyPart, WarrantyPartCreate, WarrantyPartUpdate]):
    def get_by_warranty(self, db: Session, *, warranty_id: int) -> List[WarrantyPart]:
        return db.query(self.model).filter(self.model.warranty_id == warranty_id).all()

    def get_by_part(self, db: Session, *, part_id: int) -> List[WarrantyPart]:
        return db.query(self.model).filter(self.model.part_id == part_id).all()

    def get_by_supplier(self, db: Session, *, supplier_id: int) -> List[WarrantyPart]:
        return db.query(self.model).filter(self.model.supplier_id == supplier_id).all()

warranty_part = CRUDWarrantyPart(WarrantyPart) 