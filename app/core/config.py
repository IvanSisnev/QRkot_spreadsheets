"""
Конфигурация приложения.
"""
from typing import Optional
from pydantic import BaseSettings


class Settings(BaseSettings): # noqa
    db_url: str = 'sqlite+aiosqlite:///./qrkot.db'
    app_title: str = 'QRKot'
    app_description: str = 'Приложение для Благотворительного фонда QRKot'
    secret: str = 'secret'

    # Переменные Google API
    type: Optional[str] = None
    project_id: Optional[str] = None
    private_key_id: Optional[str] = None
    private_key: Optional[str] = None
    client_email: Optional[str] = None
    client_id: Optional[str] = None
    auth_uri: Optional[str] = None
    token_uri: Optional[str] = None
    auth_provider_x509_cert_url: Optional[str] = None
    client_x509_cert_url: Optional[str] = None
    email: Optional[str] = None
    # уровни доступа Google API
    scopes = [
        'https://www.googleapis.com/auth/spreadsheets',
        'https://www.googleapis.com/auth/drive'
    ]

    class Config: # noqa
        env_file = '.env'


settings = Settings()
