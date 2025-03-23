from typing import Any, List
from datetime import date
from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from sqlalchemy import func

from app import crud, schemas
from app.api import deps
from app.crud import crud_warranty
from app.core.cache import cache

router = APIRouter()

@router.get("/warranties/summary")
def get_warranties_summary(
    start_date: date = None,
    end_date: date = None,
    db: Session = Depends(deps.get_db),
    current_user: Any = Depends(deps.get_current_user)
) -> Any:
    """Retorna um resumo das garantias."""
    cache_key = f"warranties_summary:{start_date}:{end_date}"
    
    def get_summary():
        query = db.query(crud.warranty.model)
        
        if start_date:
            query = query.filter(crud.warranty.model.failure_date >= start_date)
        if end_date:
            query = query.filter(crud.warranty.model.failure_date <= end_date)
        
        total_warranties = query.count()
        status_counts = (
            query.with_entities(
                crud.warranty.model.status,
                func.count(crud.warranty.model.id)
            )
            .group_by(crud.warranty.model.status)
            .all()
        )
        
        return {
            "total_warranties": total_warranties,
            "status_counts": dict(status_counts),
        }
    
    return cache.get_or_set(cache_key, get_summary, ttl=300)  # Cache por 5 minutos

@router.get("/warranties/costs")
def get_warranty_costs(
    start_date: date = None,
    end_date: date = None,
    db: Session = Depends(deps.get_db),
    current_user: Any = Depends(deps.get_current_user)
) -> Any:
    """Retorna estatísticas de custos das garantias."""
    cache_key = f"warranty_costs:{start_date}:{end_date}"
    
    def get_costs():
        query = (
            db.query(crud.warranty_part.model)
            .join(crud.warranty.model)
        )
        
        if start_date:
            query = query.filter(crud.warranty.model.failure_date >= start_date)
        if end_date:
            query = query.filter(crud.warranty.model.failure_date <= end_date)
        
        total_cost = query.with_entities(
            func.sum(crud.warranty_part.model.total_price)
        ).scalar() or 0
        
        costs_by_status = (
            query.with_entities(
                crud.warranty.model.status,
                func.sum(crud.warranty_part.model.total_price)
            )
            .group_by(crud.warranty.model.status)
            .all()
        )
        
        return {
            "total_cost": total_cost,
            "costs_by_status": dict(costs_by_status),
        }
    
    return cache.get_or_set(cache_key, get_costs, ttl=300)  # Cache por 5 minutos

@router.get("/warranties/failure-types")
def get_failure_types(
    start_date: date = None,
    end_date: date = None,
    db: Session = Depends(deps.get_db),
    current_user: Any = Depends(deps.get_current_user)
) -> Any:
    """Retorna estatísticas de tipos de falha."""
    cache_key = f"failure_types:{start_date}:{end_date}"
    
    def get_failures():
        query = db.query(crud.warranty.model)
        
        if start_date:
            query = query.filter(crud.warranty.model.failure_date >= start_date)
        if end_date:
            query = query.filter(crud.warranty.model.failure_date <= end_date)
        
        failure_types = (
            query.with_entities(
                crud.warranty.model.failure_type,
                func.count(crud.warranty.model.id)
            )
            .group_by(crud.warranty.model.failure_type)
            .all()
        )
        
        return dict(failure_types)
    
    return cache.get_or_set(cache_key, get_failures, ttl=300)  # Cache por 5 minutos

@router.get("/warranties/parts")
def get_warranty_parts(
    start_date: date = None,
    end_date: date = None,
    db: Session = Depends(deps.get_db),
    current_user: Any = Depends(deps.get_current_user)
) -> Any:
    """Retorna estatísticas de peças em garantia."""
    cache_key = f"warranty_parts:{start_date}:{end_date}"
    
    def get_parts():
        query = (
            db.query(crud.warranty_part.model)
            .join(crud.warranty.model)
        )
        
        if start_date:
            query = query.filter(crud.warranty.model.failure_date >= start_date)
        if end_date:
            query = query.filter(crud.warranty.model.failure_date <= end_date)
        
        parts_summary = (
            query.with_entities(
                crud.warranty_part.model.part_id,
                func.count(crud.warranty_part.model.id).label('total_occurrences'),
                func.sum(crud.warranty_part.model.quantity).label('total_quantity'),
                func.sum(crud.warranty_part.model.total_price).label('total_cost')
            )
            .group_by(crud.warranty_part.model.part_id)
            .all()
        )
        
        return [
            {
                "part_id": part.part_id,
                "total_occurrences": part.total_occurrences,
                "total_quantity": part.total_quantity,
                "total_cost": part.total_cost
            }
            for part in parts_summary
        ]
    
    return cache.get_or_set(cache_key, get_parts, ttl=300)  # Cache por 5 minutos 