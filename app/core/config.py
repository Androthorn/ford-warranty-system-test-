from pydantic_settings import BaseSettings
from typing import Optional

class Settings(BaseSettings):
    PROJECT_NAME: str = "API de Gestão de Clientes e Transações"
    VERSION: str = "1.0.0"
    API_V1_STR: str = "/api/v1"
    
    POSTGRES_SERVER: str = "localhost"
    POSTGRES_USER: str = "postgres"
    POSTGRES_PASSWORD: str = "postgres"
    POSTGRES_DB: str = "ford_db"
    SQLALCHEMY_DATABASE_URI: Optional[str] = None
    
    # Configurações de segurança
    SECRET_KEY: str = "your-secret-key-here"  # Em produção, usar variável de ambiente
    ALGORITHM: str = "HS256"
    ACCESS_TOKEN_EXPIRE_MINUTES: int = 30
    
    # Configuração do Redis
    REDIS_HOST: str = "localhost"
    REDIS_PORT: int = 6379
    
    class Config:
        case_sensitive = True
        env_file = ".env"

    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        if not self.SQLALCHEMY_DATABASE_URI:
            self.SQLALCHEMY_DATABASE_URI = (
                f"postgresql://{self.POSTGRES_USER}:{self.POSTGRES_PASSWORD}"
                f"@{self.POSTGRES_SERVER}/{self.POSTGRES_DB}"
            )

settings = Settings() 