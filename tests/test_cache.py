import pytest
from unittest.mock import Mock, patch
from app.core.cache import RedisCache

@pytest.fixture
def mock_redis():
    with patch('redis.Redis') as mock:
        yield mock

@pytest.fixture
def cache(mock_redis):
    return RedisCache()

def test_get(cache, mock_redis):
    # Arrange
    mock_redis.return_value.get.return_value = b'cached_value'
    
    # Act
    result = cache.get('test_key')
    
    # Assert
    assert result == 'cached_value'
    mock_redis.return_value.get.assert_called_once_with('test_key')

def test_get_none(cache, mock_redis):
    # Arrange
    mock_redis.return_value.get.return_value = None
    
    # Act
    result = cache.get('test_key')
    
    # Assert
    assert result is None

def test_set(cache, mock_redis):
    # Arrange
    mock_redis.return_value.set.return_value = True
    
    # Act
    result = cache.set('test_key', 'test_value')
    
    # Assert
    assert result is True
    mock_redis.return_value.set.assert_called_once()

def test_set_with_ttl(cache, mock_redis):
    # Arrange
    mock_redis.return_value.set.return_value = True
    
    # Act
    result = cache.set('test_key', 'test_value', ttl=60)
    
    # Assert
    assert result is True
    mock_redis.return_value.set.assert_called_once_with(
        'test_key',
        b'test_value',
        ex=60
    )

def test_delete(cache, mock_redis):
    # Arrange
    mock_redis.return_value.delete.return_value = 1
    
    # Act
    result = cache.delete('test_key')
    
    # Assert
    assert result is True
    mock_redis.return_value.delete.assert_called_once_with('test_key')

def test_clear_pattern(cache, mock_redis):
    # Arrange
    mock_redis.return_value.keys.return_value = [b'key1', b'key2']
    mock_redis.return_value.delete.return_value = 2
    
    # Act
    result = cache.clear_pattern('test*')
    
    # Assert
    assert result is True
    mock_redis.return_value.keys.assert_called_once_with('test*')
    mock_redis.return_value.delete.assert_called_once_with(b'key1', b'key2')

def test_get_or_set(cache, mock_redis):
    # Arrange
    mock_redis.return_value.get.return_value = None
    mock_redis.return_value.set.return_value = True
    callback = Mock(return_value='new_value')
    
    # Act
    result = cache.get_or_set('test_key', callback)
    
    # Assert
    assert result == 'new_value'
    callback.assert_called_once()
    mock_redis.return_value.set.assert_called_once()

def test_get_or_set_cached(cache, mock_redis):
    # Arrange
    mock_redis.return_value.get.return_value = b'cached_value'
    callback = Mock()
    
    # Act
    result = cache.get_or_set('test_key', callback)
    
    # Assert
    assert result == 'cached_value'
    callback.assert_not_called()
    mock_redis.return_value.set.assert_not_called() 