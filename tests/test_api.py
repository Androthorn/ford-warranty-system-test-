from fastapi.testclient import TestClient
from sqlalchemy.orm import Session
import pytest
from datetime import date

from app.main import app
from app import crud
from app.schemas.user import UserCreate
from app.core.config import settings

client = TestClient(app)

def test_create_user(db: Session):
    user_in = UserCreate(
        email="test@example.com",
        password="testpassword123",
        full_name="Test User",
        is_active=True,
        is_superuser=False,
    )
    user = crud.user.create(db, obj_in=user_in)
    assert user.email == user_in.email
    assert user.full_name == user_in.full_name
    assert user.is_active == user_in.is_active
    assert user.is_superuser == user_in.is_superuser

def test_login():
    response = client.post(
        "/api/v1/auth/login/access-token",
        data={
            "username": "test@example.com",
            "password": "testpassword123",
        },
    )
    assert response.status_code == 200
    assert "access_token" in response.json()
    assert response.json()["token_type"] == "bearer"

def test_create_warranty():
    # First login to get the token
    login_response = client.post(
        "/api/v1/auth/login/access-token",
        data={
            "username": "test@example.com",
            "password": "testpassword123",
        },
    )
    token = login_response.json()["access_token"]
    
    # Create a warranty
    warranty_data = {
        "vehicle_id": 1,
        "part_id": 1,
        "location_id": 1,
        "failure_type": "mechanical",
        "failure_date": str(date.today()),
        "description": "Test warranty",
        "status": "pending"
    }
    
    response = client.post(
        "/api/v1/warranties/",
        json=warranty_data,
        headers={"Authorization": f"Bearer {token}"}
    )
    assert response.status_code == 200
    data = response.json()
    assert data["vehicle_id"] == warranty_data["vehicle_id"]
    assert data["part_id"] == warranty_data["part_id"]
    assert data["location_id"] == warranty_data["location_id"]
    assert data["failure_type"] == warranty_data["failure_type"]
    assert data["status"] == warranty_data["status"]

def test_create_warranty_part():
    # First login to get the token
    login_response = client.post(
        "/api/v1/auth/login/access-token",
        data={
            "username": "test@example.com",
            "password": "testpassword123",
        },
    )
    token = login_response.json()["access_token"]
    
    # Create a warranty part
    warranty_part_data = {
        "warranty_id": 1,
        "part_id": 1,
        "supplier_id": 1,
        "quantity": 2,
        "unit_price": 100.0,
        "total_price": 200.0,
        "notes": "Test warranty part"
    }
    
    response = client.post(
        "/api/v1/warranty-parts/",
        json=warranty_part_data,
        headers={"Authorization": f"Bearer {token}"}
    )
    assert response.status_code == 200
    data = response.json()
    assert data["warranty_id"] == warranty_part_data["warranty_id"]
    assert data["part_id"] == warranty_part_data["part_id"]
    assert data["supplier_id"] == warranty_part_data["supplier_id"]
    assert data["quantity"] == warranty_part_data["quantity"]
    assert data["unit_price"] == warranty_part_data["unit_price"]
    assert data["total_price"] == warranty_part_data["total_price"]

def test_get_warranties_summary():
    # First login to get the token
    login_response = client.post(
        "/api/v1/auth/login/access-token",
        data={
            "username": "test@example.com",
            "password": "testpassword123",
        },
    )
    token = login_response.json()["access_token"]
    
    # Get warranties summary
    response = client.get(
        "/api/v1/reports/warranties/summary",
        headers={"Authorization": f"Bearer {token}"}
    )
    assert response.status_code == 200
    data = response.json()
    assert "total_warranties" in data
    assert "status_counts" in data

def test_get_warranty_costs():
    # First login to get the token
    login_response = client.post(
        "/api/v1/auth/login/access-token",
        data={
            "username": "test@example.com",
            "password": "testpassword123",
        },
    )
    token = login_response.json()["access_token"]
    
    # Get warranty costs
    response = client.get(
        "/api/v1/reports/warranties/costs",
        headers={"Authorization": f"Bearer {token}"}
    )
    assert response.status_code == 200
    data = response.json()
    assert "total_cost" in data
    assert "costs_by_status" in data 