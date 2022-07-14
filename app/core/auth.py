from datetime import datetime, timedelta
from typing import Optional

from fastapi.security import OAuth2PasswordBearer
from jose import jwt
from sqlalchemy.orm.session import Session

from app.core.config import settings
from app.core.security import verify_password
from app.models.user import User

oauth2_scheme = OAuth2PasswordBearer(tokenUrl=f"{settings.API_V1_STR}/auth/login")


def authenticate(*, email: str, password: str, db: Session) -> Optional[User]:
    user = db.query(User).filter(User.email == email).first()
    if not user:
        return None
    if not verify_password(password, user.hashed_password):
        return None
    return user


def create_access_token(*, sub: str) -> str:
    return _create_token(
        token_type="access_token",
        lifetime=timedelta(minutes=settings.ACCESS_TOKEN_EXPIRE_MINUTES),
        sub=sub,
    )


def _create_token(token_type: str, lifetime: timedelta, sub: str) -> str:
    payload = {"type": token_type}

    # https://datatracker.ietf.org/doc/html/rfc7519#section-4.1.3
    # The "exp" claim identifies the expiration time on or after which the JWT MUST NOT be accepted for processing.
    payload["exp"] = datetime.utcnow() + lifetime

    # The "iat" (issued at) claim identifies the time at which the JWT was issued.
    payload["iat"] = datetime.utcnow()

    # The "sub" (subject) claim identifies the principal that is the subject of the JWT
    payload["sub"] = sub

    return jwt.encode(claims=payload, key=settings.JWT_SECRET, algorithm=settings.ALGORITHM)
