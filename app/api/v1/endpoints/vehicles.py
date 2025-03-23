from typing import Any, List
from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session

from app import crud, schemas
from app.api import deps

router = APIRouter()

@router.get("/", response_model=List[schemas.Vehicle])
def read_vehicles(
    db: Session = Depends(deps.get_db),
    skip: int = 0,
    limit: int = 100,
) -> Any:
    """
    Retrieve vehicles.
    """
    vehicles = crud.vehicle.get_multi(db, skip=skip, limit=limit)
    return vehicles

@router.post("/", response_model=schemas.Vehicle)
def create_vehicle(
    *,
    db: Session = Depends(deps.get_db),
    vehicle_in: schemas.VehicleCreate,
) -> Any:
    """
    Create new vehicle.
    """
    vehicle = crud.vehicle.create(db=db, obj_in=vehicle_in)
    return vehicle

@router.put("/{vehicle_id}", response_model=schemas.Vehicle)
def update_vehicle(
    *,
    db: Session = Depends(deps.get_db),
    vehicle_id: int,
    vehicle_in: schemas.VehicleUpdate,
) -> Any:
    """
    Update a vehicle.
    """
    vehicle = crud.vehicle.get(db=db, id=vehicle_id)
    if not vehicle:
        raise HTTPException(status_code=404, detail="Vehicle not found")
    vehicle = crud.vehicle.update(db=db, db_obj=vehicle, obj_in=vehicle_in)
    return vehicle

@router.get("/{vehicle_id}", response_model=schemas.Vehicle)
def read_vehicle(
    *,
    db: Session = Depends(deps.get_db),
    vehicle_id: int,
) -> Any:
    """
    Get vehicle by ID.
    """
    vehicle = crud.vehicle.get(db=db, id=vehicle_id)
    if not vehicle:
        raise HTTPException(status_code=404, detail="Vehicle not found")
    return vehicle

@router.delete("/{vehicle_id}", response_model=schemas.Vehicle)
def delete_vehicle(
    *,
    db: Session = Depends(deps.get_db),
    vehicle_id: int,
) -> Any:
    """
    Delete a vehicle.
    """
    vehicle = crud.vehicle.get(db=db, id=vehicle_id)
    if not vehicle:
        raise HTTPException(status_code=404, detail="Vehicle not found")
    vehicle = crud.vehicle.remove(db=db, id=vehicle_id)
    return vehicle

@router.get("/model/{model}", response_model=List[schemas.Vehicle])
def read_vehicles_by_model(
    *,
    db: Session = Depends(deps.get_db),
    model: str,
) -> Any:
    """
    Get vehicles by model.
    """
    vehicles = crud.vehicle.get_by_model(db=db, model=model)
    return vehicles

@router.get("/year/{year}", response_model=List[schemas.Vehicle])
def read_vehicles_by_year(
    *,
    db: Session = Depends(deps.get_db),
    year: int,
) -> Any:
    """
    Get vehicles by year.
    """
    vehicles = crud.vehicle.get_by_year(db=db, year=year)
    return vehicles

@router.get("/propulsion/{propulsion}", response_model=List[schemas.Vehicle])
def read_vehicles_by_propulsion(
    *,
    db: Session = Depends(deps.get_db),
    propulsion: str,
) -> Any:
    """
    Get vehicles by propulsion type.
    """
    vehicles = crud.vehicle.get_by_propulsion(db=db, propulsion=propulsion)
    return vehicles 