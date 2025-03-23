from typing import Any, List
from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session

from app import crud, schemas
from app.api import deps

router = APIRouter()

@router.get("/", response_model=List[schemas.Location])
def read_locations(
    db: Session = Depends(deps.get_db),
    skip: int = 0,
    limit: int = 100,
) -> Any:
    """
    Retrieve locations.
    """
    locations = crud.location.get_multi(db, skip=skip, limit=limit)
    return locations

@router.post("/", response_model=schemas.Location)
def create_location(
    *,
    db: Session = Depends(deps.get_db),
    location_in: schemas.LocationCreate,
) -> Any:
    """
    Create new location.
    """
    location = crud.location.create(db=db, obj_in=location_in)
    return location

@router.put("/{location_id}", response_model=schemas.Location)
def update_location(
    *,
    db: Session = Depends(deps.get_db),
    location_id: int,
    location_in: schemas.LocationUpdate,
) -> Any:
    """
    Update a location.
    """
    location = crud.location.get(db=db, id=location_id)
    if not location:
        raise HTTPException(status_code=404, detail="Location not found")
    location = crud.location.update(db=db, db_obj=location, obj_in=location_in)
    return location

@router.get("/{location_id}", response_model=schemas.Location)
def read_location(
    *,
    db: Session = Depends(deps.get_db),
    location_id: int,
) -> Any:
    """
    Get location by ID.
    """
    location = crud.location.get(db=db, id=location_id)
    if not location:
        raise HTTPException(status_code=404, detail="Location not found")
    return location

@router.delete("/{location_id}", response_model=schemas.Location)
def delete_location(
    *,
    db: Session = Depends(deps.get_db),
    location_id: int,
) -> Any:
    """
    Delete a location.
    """
    location = crud.location.get(db=db, id=location_id)
    if not location:
        raise HTTPException(status_code=404, detail="Location not found")
    location = crud.location.remove(db=db, id=location_id)
    return location

@router.get("/market/{market}", response_model=List[schemas.Location])
def read_locations_by_market(
    *,
    db: Session = Depends(deps.get_db),
    market: str,
) -> Any:
    """
    Get locations by market.
    """
    locations = crud.location.get_by_market(db=db, market=market)
    return locations

@router.get("/country/{country}", response_model=List[schemas.Location])
def read_locations_by_country(
    *,
    db: Session = Depends(deps.get_db),
    country: str,
) -> Any:
    """
    Get locations by country.
    """
    locations = crud.location.get_by_country(db=db, country=country)
    return locations 