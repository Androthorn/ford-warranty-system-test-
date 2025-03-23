import pytest
from datetime import date, timedelta
from fastapi.testclient import TestClient
from app.main import app
from app.core.cache import cache

client = TestClient(app)

@pytest.fixture
def mock_cache():
    with pytest.MonkeyPatch.context() as m:
        m.setattr(cache, 'get', lambda key: None)
        m.setattr(cache, 'set', lambda key, value, ttl: True)
        yield cache

def test_warranties_summary_cache(mock_cache):
    # Arrange
    start_date = date.today() - timedelta(days=30)
    end_date = date.today()
    
    # Act
    response = client.get(
        f"/api/v1/reports/warranties/summary?start_date={start_date}&end_date={end_date}"
    )
    
    # Assert
    assert response.status_code == 200
    assert "total_warranties" in response.json()
    assert "status_counts" in response.json()

def test_warranty_costs_cache(mock_cache):
    # Arrange
    start_date = date.today() - timedelta(days=30)
    end_date = date.today()
    
    # Act
    response = client.get(
        f"/api/v1/reports/warranties/costs?start_date={start_date}&end_date={end_date}"
    )
    
    # Assert
    assert response.status_code == 200
    assert "total_cost" in response.json()
    assert "costs_by_status" in response.json()

def test_failure_types_cache(mock_cache):
    # Arrange
    start_date = date.today() - timedelta(days=30)
    end_date = date.today()
    
    # Act
    response = client.get(
        f"/api/v1/reports/warranties/failure-types?start_date={start_date}&end_date={end_date}"
    )
    
    # Assert
    assert response.status_code == 200
    assert isinstance(response.json(), dict)

def test_warranty_parts_cache(mock_cache):
    # Arrange
    start_date = date.today() - timedelta(days=30)
    end_date = date.today()
    
    # Act
    response = client.get(
        f"/api/v1/reports/warranties/parts?start_date={start_date}&end_date={end_date}"
    )
    
    # Assert
    assert response.status_code == 200
    assert isinstance(response.json(), list) 