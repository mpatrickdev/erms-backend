from pydantic import BaseSettings


class Settings(BaseSettings):
    database_url: str
    # secret_key: str
    database_name: str
    cloudinary_name: str
    cloudinary_api_key: str
    cloudinary_api_secret: str

    class Config:
        env_file = ".env"


settings = Settings()