from typing import Any, List
from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session

from app import crud, schemas
from app.api import deps

router = APIRouter()

@router.get("/", response_model=List[schemas.WarrantyPart])
def read_warranty_parts(
    db: Session = Depends(deps.get_db),
    skip: int = 0,
    limit: int = 100,
) -> Any:
    """
    Retrieve warranty parts.
    """
    warranty_parts = crud.warranty_part.get_multi(db, skip=skip, limit=limit)
    return warranty_parts

@router.post("/", response_model=schemas.WarrantyPart)
def create_warranty_part(
    *,
    db: Session = Depends(deps.get_db),
    warranty_part_in: schemas.WarrantyPartCreate,
) -> Any:
    """
    Create new warranty part.
    """
    warranty_part = crud.warranty_part.create(db=db, obj_in=warranty_part_in)
    return warranty_part

@router.put("/{warranty_part_id}", response_model=schemas.WarrantyPart)
def update_warranty_part(
    *,
    db: Session = Depends(deps.get_db),
    warranty_part_id: int,
    warranty_part_in: schemas.WarrantyPartUpdate,
) -> Any:
    """
    Update a warranty part.
    """
    warranty_part = crud.warranty_part.get(db=db, id=warranty_part_id)
    if not warranty_part:
        raise HTTPException(status_code=404, detail="Warranty part not found")
    warranty_part = crud.warranty_part.update(db=db, db_obj=warranty_part, obj_in=warranty_part_in)
    return warranty_part

@router.get("/{warranty_part_id}", response_model=schemas.WarrantyPart)
def read_warranty_part(
    *,
    db: Session = Depends(deps.get_db),
    warranty_part_id: int,
) -> Any:
    """
    Get warranty part by ID.
    """
    warranty_part = crud.warranty_part.get(db=db, id=warranty_part_id)
    if not warranty_part:
        raise HTTPException(status_code=404, detail="Warranty part not found")
    return warranty_part

@router.delete("/{warranty_part_id}", response_model=schemas.WarrantyPart)
def delete_warranty_part(
    *,
    db: Session = Depends(deps.get_db),
    warranty_part_id: int,
) -> Any:
    """
    Delete a warranty part.
    """
    warranty_part = crud.warranty_part.get(db=db, id=warranty_part_id)
    if not warranty_part:
        raise HTTPException(status_code=404, detail="Warranty part not found")
    warranty_part = crud.warranty_part.remove(db=db, id=warranty_part_id)
    return warranty_part

@router.get("/warranty/{warranty_id}", response_model=List[schemas.WarrantyPart])
def read_warranty_parts_by_warranty(
    *,
    db: Session = Depends(deps.get_db),
    warranty_id: int,
) -> Any:
    """
    Get warranty parts by warranty.
    """
    warranty_parts = crud.warranty_part.get_by_warranty(db=db, warranty_id=warranty_id)
    return warranty_parts

@router.get("/part/{part_id}", response_model=List[schemas.WarrantyPart])
def read_warranty_parts_by_part(
    *,
    db: Session = Depends(deps.get_db),
    part_id: int,
) -> Any:
    """
    Get warranty parts by part.
    """
    warranty_parts = crud.warranty_part.get_by_part(db=db, part_id=part_id)
    return warranty_parts

@router.get("/supplier/{supplier_id}", response_model=List[schemas.WarrantyPart])
def read_warranty_parts_by_supplier(
    *,
    db: Session = Depends(deps.get_db),
    supplier_id: int,
) -> Any:
    """
    Get warranty parts by supplier.
    """
    warranty_parts = crud.warranty_part.get_by_supplier(db=db, supplier_id=supplier_id)
    return warranty_parts 