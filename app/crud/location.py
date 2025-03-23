from typing import Any, Dict, Optional, Union, List
from sqlalchemy.orm import Session

from app.crud.base import CRUDBase
from app.models.location import Location
from app.schemas.location import LocationCreate, LocationUpdate

class CRUDLocation(CRUDBase[Location, LocationCreate, LocationUpdate]):
    def get_by_market(self, db: Session, *, market: str) -> List[Location]:
        return db.query(self.model).filter(self.model.market == market).all()

    def get_by_country(self, db: Session, *, country: str) -> List[Location]:
        return db.query(self.model).filter(self.model.country == country).all()

location = CRUDLocation(Location) 