from typing import Any, List
from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session

from app import crud, schemas
from app.api import deps

router = APIRouter()

@router.get("/", response_model=List[schemas.Supplier])
def read_suppliers(
    db: Session = Depends(deps.get_db),
    skip: int = 0,
    limit: int = 100,
) -> Any:
    """
    Retrieve suppliers.
    """
    suppliers = crud.supplier.get_multi(db, skip=skip, limit=limit)
    return suppliers

@router.post("/", response_model=schemas.Supplier)
def create_supplier(
    *,
    db: Session = Depends(deps.get_db),
    supplier_in: schemas.SupplierCreate,
) -> Any:
    """
    Create new supplier.
    """
    supplier = crud.supplier.create(db=db, obj_in=supplier_in)
    return supplier

@router.put("/{supplier_id}", response_model=schemas.Supplier)
def update_supplier(
    *,
    db: Session = Depends(deps.get_db),
    supplier_id: int,
    supplier_in: schemas.SupplierUpdate,
) -> Any:
    """
    Update a supplier.
    """
    supplier = crud.supplier.get(db=db, id=supplier_id)
    if not supplier:
        raise HTTPException(status_code=404, detail="Supplier not found")
    supplier = crud.supplier.update(db=db, db_obj=supplier, obj_in=supplier_in)
    return supplier

@router.get("/{supplier_id}", response_model=schemas.Supplier)
def read_supplier(
    *,
    db: Session = Depends(deps.get_db),
    supplier_id: int,
) -> Any:
    """
    Get supplier by ID.
    """
    supplier = crud.supplier.get(db=db, id=supplier_id)
    if not supplier:
        raise HTTPException(status_code=404, detail="Supplier not found")
    return supplier

@router.delete("/{supplier_id}", response_model=schemas.Supplier)
def delete_supplier(
    *,
    db: Session = Depends(deps.get_db),
    supplier_id: int,
) -> Any:
    """
    Delete a supplier.
    """
    supplier = crud.supplier.get(db=db, id=supplier_id)
    if not supplier:
        raise HTTPException(status_code=404, detail="Supplier not found")
    supplier = crud.supplier.remove(db=db, id=supplier_id)
    return supplier

@router.get("/location/{location_id}", response_model=List[schemas.Supplier])
def read_suppliers_by_location(
    *,
    db: Session = Depends(deps.get_db),
    location_id: int,
) -> Any:
    """
    Get suppliers by location.
    """
    suppliers = crud.supplier.get_by_location(db=db, location_id=location_id)
    return suppliers

@router.get("/name/{name}", response_model=schemas.Supplier)
def read_supplier_by_name(
    *,
    db: Session = Depends(deps.get_db),
    name: str,
) -> Any:
    """
    Get supplier by name.
    """
    supplier = crud.supplier.get_by_name(db=db, name=name)
    if not supplier:
        raise HTTPException(status_code=404, detail="Supplier not found")
    return supplier 