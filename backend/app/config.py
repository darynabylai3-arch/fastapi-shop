from pydantic_settings import BaseModel

class Settings(BaseModel):
    app_name: str = 'Fastapi Shop'
    debug : bool = True
    database_url = str = 'sqlite:///.shop.db'
    cors_origin: list = [
        'http://localhost:5173',
        'http://localhost:3000',
        'http://127.0.0.1:5173',
        'http://127.0.0.1:3000'
    ]

    static_dir: str = 'static'
    images : str = 'static/images'

    class Config:
        env_file = '.env'

    
settings = Settings()