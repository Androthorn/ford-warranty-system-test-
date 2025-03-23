from typing import Any, List
from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from datetime import date

from app import crud, schemas
from app.api import deps

router = APIRouter()

@router.get("/", response_model=List[schemas.Warranty])
def read_warranties(
    db: Session = Depends(deps.get_db),
    skip: int = 0,
    limit: int = 100,
) -> Any:
    """
    Retrieve warranties.
    """
    warranties = crud.warranty.get_multi(db, skip=skip, limit=limit)
    return warranties

@router.post("/", response_model=schemas.Warranty)
def create_warranty(
    *,
    db: Session = Depends(deps.get_db),
    warranty_in: schemas.WarrantyCreate,
) -> Any:
    """
    Create new warranty.
    """
    warranty = crud.warranty.create(db=db, obj_in=warranty_in)
    return warranty

@router.put("/{warranty_id}", response_model=schemas.Warranty)
def update_warranty(
    *,
    db: Session = Depends(deps.get_db),
    warranty_id: int,
    warranty_in: schemas.WarrantyUpdate,
) -> Any:
    """
    Update a warranty.
    """
    warranty = crud.warranty.get(db=db, id=warranty_id)
    if not warranty:
        raise HTTPException(status_code=404, detail="Warranty not found")
    warranty = crud.warranty.update(db=db, db_obj=warranty, obj_in=warranty_in)
    return warranty

@router.get("/{warranty_id}", response_model=schemas.Warranty)
def read_warranty(
    *,
    db: Session = Depends(deps.get_db),
    warranty_id: int,
) -> Any:
    """
    Get warranty by ID.
    """
    warranty = crud.warranty.get(db=db, id=warranty_id)
    if not warranty:
        raise HTTPException(status_code=404, detail="Warranty not found")
    return warranty

@router.delete("/{warranty_id}", response_model=schemas.Warranty)
def delete_warranty(
    *,
    db: Session = Depends(deps.get_db),
    warranty_id: int,
) -> Any:
    """
    Delete a warranty.
    """
    warranty = crud.warranty.get(db=db, id=warranty_id)
    if not warranty:
        raise HTTPException(status_code=404, detail="Warranty not found")
    warranty = crud.warranty.remove(db=db, id=warranty_id)
    return warranty

@router.get("/vehicle/{vehicle_id}", response_model=List[schemas.Warranty])
def read_warranties_by_vehicle(
    *,
    db: Session = Depends(deps.get_db),
    vehicle_id: int,
) -> Any:
    """
    Get warranties by vehicle.
    """
    warranties = crud.warranty.get_by_vehicle(db=db, vehicle_id=vehicle_id)
    return warranties

@router.get("/part/{part_id}", response_model=List[schemas.Warranty])
def read_warranties_by_part(
    *,
    db: Session = Depends(deps.get_db),
    part_id: int,
) -> Any:
    """
    Get warranties by part.
    """
    warranties = crud.warranty.get_by_part(db=db, part_id=part_id)
    return warranties

@router.get("/location/{location_id}", response_model=List[schemas.Warranty])
def read_warranties_by_location(
    *,
    db: Session = Depends(deps.get_db),
    location_id: int,
) -> Any:
    """
    Get warranties by location.
    """
    warranties = crud.warranty.get_by_location(db=db, location_id=location_id)
    return warranties

@router.get("/date-range/", response_model=List[schemas.Warranty])
def read_warranties_by_date_range(
    *,
    db: Session = Depends(deps.get_db),
    start_date: date,
    end_date: date,
) -> Any:
    """
    Get warranties by date range.
    """
    warranties = crud.warranty.get_by_date_range(
        db=db, start_date=start_date, end_date=end_date
    )
    return warranties

@router.get("/failure-type/{failure_type}", response_model=List[schemas.Warranty])
def read_warranties_by_failure_type(
    *,
    db: Session = Depends(deps.get_db),
    failure_type: str,
) -> Any:
    """
    Get warranties by failure type.
    """
    warranties = crud.warranty.get_by_failure_type(db=db, failure_type=failure_type)
    return warranties 