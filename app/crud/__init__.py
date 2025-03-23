from app.crud.base import CRUDBase
from app.crud.user import user
from app.crud.location import location
from app.crud.supplier import supplier
from app.crud.vehicle import vehicle
from app.crud.part import part
from app.crud.purchase import purchase
from app.crud.warranty import warranty
from app.crud.warranty_part import warranty_part

__all__ = [
    "CRUDBase",
    "user",
    "location",
    "supplier",
    "vehicle",
    "part",
    "purchase",
    "warranty",
    "warranty_part",
] 