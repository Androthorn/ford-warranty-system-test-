from typing import Any, List
from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from datetime import date

from app import crud, schemas
from app.api import deps

router = APIRouter()

@router.get("/", response_model=List[schemas.Purchase])
def read_purchases(
    db: Session = Depends(deps.get_db),
    skip: int = 0,
    limit: int = 100,
) -> Any:
    """
    Retrieve purchases.
    """
    purchases = crud.purchase.get_multi(db, skip=skip, limit=limit)
    return purchases

@router.post("/", response_model=schemas.Purchase)
def create_purchase(
    *,
    db: Session = Depends(deps.get_db),
    purchase_in: schemas.PurchaseCreate,
) -> Any:
    """
    Create new purchase.
    """
    purchase = crud.purchase.create(db=db, obj_in=purchase_in)
    return purchase

@router.put("/{purchase_id}", response_model=schemas.Purchase)
def update_purchase(
    *,
    db: Session = Depends(deps.get_db),
    purchase_id: int,
    purchase_in: schemas.PurchaseUpdate,
) -> Any:
    """
    Update a purchase.
    """
    purchase = crud.purchase.get(db=db, id=purchase_id)
    if not purchase:
        raise HTTPException(status_code=404, detail="Purchase not found")
    purchase = crud.purchase.update(db=db, db_obj=purchase, obj_in=purchase_in)
    return purchase

@router.get("/{purchase_id}", response_model=schemas.Purchase)
def read_purchase(
    *,
    db: Session = Depends(deps.get_db),
    purchase_id: int,
) -> Any:
    """
    Get purchase by ID.
    """
    purchase = crud.purchase.get(db=db, id=purchase_id)
    if not purchase:
        raise HTTPException(status_code=404, detail="Purchase not found")
    return purchase

@router.delete("/{purchase_id}", response_model=schemas.Purchase)
def delete_purchase(
    *,
    db: Session = Depends(deps.get_db),
    purchase_id: int,
) -> Any:
    """
    Delete a purchase.
    """
    purchase = crud.purchase.get(db=db, id=purchase_id)
    if not purchase:
        raise HTTPException(status_code=404, detail="Purchase not found")
    purchase = crud.purchase.remove(db=db, id=purchase_id)
    return purchase

@router.get("/type/{purchase_type}", response_model=List[schemas.Purchase])
def read_purchases_by_type(
    *,
    db: Session = Depends(deps.get_db),
    purchase_type: str,
) -> Any:
    """
    Get purchases by type.
    """
    purchases = crud.purchase.get_by_type(db=db, purchase_type=purchase_type)
    return purchases

@router.get("/part/{part_id}", response_model=List[schemas.Purchase])
def read_purchases_by_part(
    *,
    db: Session = Depends(deps.get_db),
    part_id: int,
) -> Any:
    """
    Get purchases by part.
    """
    purchases = crud.purchase.get_by_part(db=db, part_id=part_id)
    return purchases

@router.get("/date-range/", response_model=List[schemas.Purchase])
def read_purchases_by_date_range(
    *,
    db: Session = Depends(deps.get_db),
    start_date: date,
    end_date: date,
) -> Any:
    """
    Get purchases by date range.
    """
    purchases = crud.purchase.get_by_date_range(
        db=db, start_date=start_date, end_date=end_date
    )
    return purchases 