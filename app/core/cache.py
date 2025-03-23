from typing import Any, Optional
import pickle
import redis
from app.core.config import settings

class RedisCache:
    def __init__(self):
        self.redis_client = redis.Redis(
            host=settings.REDIS_HOST,
            port=settings.REDIS_PORT,
            db=settings.REDIS_DB,
            decode_responses=False  # Mantém os dados binários para pickle
        )
        self.default_ttl = 3600  # 1 hora em segundos

    def get(self, key: str) -> Optional[Any]:
        """Recupera um valor do cache."""
        data = self.redis_client.get(key)
        if data:
            return pickle.loads(data)
        return None

    def set(self, key: str, value: Any, ttl: Optional[int] = None) -> bool:
        """Armazena um valor no cache."""
        try:
            serialized_value = pickle.dumps(value)
            return self.redis_client.set(
                key,
                serialized_value,
                ex=ttl or self.default_ttl
            )
        except Exception:
            return False

    def delete(self, key: str) -> bool:
        """Remove um valor do cache."""
        return bool(self.redis_client.delete(key))

    def clear_pattern(self, pattern: str) -> bool:
        """Remove todas as chaves que correspondem ao padrão."""
        try:
            keys = self.redis_client.keys(pattern)
            if keys:
                self.redis_client.delete(*keys)
            return True
        except Exception:
            return False

    def get_or_set(self, key: str, callback, ttl: Optional[int] = None) -> Any:
        """Recupera um valor do cache ou executa uma função para obtê-lo."""
        value = self.get(key)
        if value is None:
            value = callback()
            self.set(key, value, ttl)
        return value

# Instância global do cache
cache = RedisCache() 