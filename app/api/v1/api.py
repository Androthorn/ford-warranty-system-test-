from fastapi import APIRouter
from app.api.v1.endpoints import auth, locations, suppliers, vehicles, parts, purchases, warranties, warranty_parts, reports

api_router = APIRouter()

api_router.include_router(auth.router, prefix="/auth", tags=["auth"])
api_router.include_router(locations.router, prefix="/locations", tags=["locations"])
api_router.include_router(suppliers.router, prefix="/suppliers", tags=["suppliers"])
api_router.include_router(vehicles.router, prefix="/vehicles", tags=["vehicles"])
api_router.include_router(parts.router, prefix="/parts", tags=["parts"])
api_router.include_router(purchases.router, prefix="/purchases", tags=["purchases"])
api_router.include_router(warranties.router, prefix="/warranties", tags=["warranties"])
api_router.include_router(warranty_parts.router, prefix="/warranty-parts", tags=["warranty-parts"])
api_router.include_router(reports.router, prefix="/reports", tags=["reports"]) 