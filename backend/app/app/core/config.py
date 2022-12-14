import pathlib
from typing import List, Optional, Union

from pydantic import AnyHttpUrl, BaseSettings, EmailStr, validator

# Project Directory
ROOT = pathlib.Path(__file__).resolve().parent.parent


class Settings(BaseSettings):
    API_V1_STR: str = "/api/v1"
    # BACKEND_CORS_ORIGINS is a JSON-formatted list of origins
    # e.g: '["http://localhost", "http://localhost:4200", "http://localhost:3000"]'
    BACKEND_CORS_ORIGINS: List[AnyHttpUrl] = [
        "http://localhost:3000",
        "http://localhost:8001",
        "https://fastapi-recipe-app.herokuapp.com"
    ]
    # Origins that match this regex OR are in the above list are allowed
    BACKEND_CORS_ORIGIN_REGEX: Optional[str] = "https.*\\.(netlify.app|herokuapp.com)"

    @validator("BACKEND_CORS_ORIGINS", pre=True)
    def assemble_cors_origins(cls, v: Union[str, List[str]]) -> Union[List[str], str]:
        if isinstance(v, str) and not v.startswith("["):
            return [i.strip() for i in v.split(",")]
        elif isinstance(v, (list, str)):
            return v
        raise ValueError(v)

    DATABASE_URI: Optional[str] = "sqlite:///example.db"
    FIRST_SUPERUSER: EmailStr = "admin@recipeapi.com"
    FIRST_SUPERUSER_PW: str = "CHANGEME"

    JWT_SECRET: str = "TEST_SECRET_DO_NOT_USE_IN_PROD"
    ALGORITHM: str = "HS256"
    # 60 minutes * 24 hours * 8 days = 8 days
    ACCESS_TOKEN_EXPIRE_MINUTES: int = 60 * 24 * 8

    class Config:
        case_sensitive = True


settings = Settings()
