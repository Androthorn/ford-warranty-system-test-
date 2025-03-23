from typing import Any, List
from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session

from app import crud, schemas
from app.api import deps

router = APIRouter()

@router.get("/", response_model=List[schemas.Part])
def read_parts(
    db: Session = Depends(deps.get_db),
    skip: int = 0,
    limit: int = 100,
) -> Any:
    """
    Retrieve parts.
    """
    parts = crud.part.get_multi(db, skip=skip, limit=limit)
    return parts

@router.post("/", response_model=schemas.Part)
def create_part(
    *,
    db: Session = Depends(deps.get_db),
    part_in: schemas.PartCreate,
) -> Any:
    """
    Create new part.
    """
    part = crud.part.create(db=db, obj_in=part_in)
    return part

@router.put("/{part_id}", response_model=schemas.Part)
def update_part(
    *,
    db: Session = Depends(deps.get_db),
    part_id: int,
    part_in: schemas.PartUpdate,
) -> Any:
    """
    Update a part.
    """
    part = crud.part.get(db=db, id=part_id)
    if not part:
        raise HTTPException(status_code=404, detail="Part not found")
    part = crud.part.update(db=db, db_obj=part, obj_in=part_in)
    return part

@router.get("/{part_id}", response_model=schemas.Part)
def read_part(
    *,
    db: Session = Depends(deps.get_db),
    part_id: int,
) -> Any:
    """
    Get part by ID.
    """
    part = crud.part.get(db=db, id=part_id)
    if not part:
        raise HTTPException(status_code=404, detail="Part not found")
    return part

@router.delete("/{part_id}", response_model=schemas.Part)
def delete_part(
    *,
    db: Session = Depends(deps.get_db),
    part_id: int,
) -> Any:
    """
    Delete a part.
    """
    part = crud.part.get(db=db, id=part_id)
    if not part:
        raise HTTPException(status_code=404, detail="Part not found")
    part = crud.part.remove(db=db, id=part_id)
    return part

@router.get("/supplier/{supplier_id}", response_model=List[schemas.Part])
def read_parts_by_supplier(
    *,
    db: Session = Depends(deps.get_db),
    supplier_id: int,
) -> Any:
    """
    Get parts by supplier.
    """
    parts = crud.part.get_by_supplier(db=db, supplier_id=supplier_id)
    return parts

@router.get("/name/{name}", response_model=schemas.Part)
def read_part_by_name(
    *,
    db: Session = Depends(deps.get_db),
    name: str,
) -> Any:
    """
    Get part by name.
    """
    part = crud.part.get_by_name(db=db, name=name)
    if not part:
        raise HTTPException(status_code=404, detail="Part not found")
    return part 