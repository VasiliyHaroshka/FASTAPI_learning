import os
from datetime import timedelta, datetime

from jose import jwt
from jose.exceptions import JWTError
from passlib.context import CryptContext

from model.user import User

if os.getenv("CREATURE_UNIT_TEST"):
    from fake import user as data
else:
    from data import user as data

SECRET_KEY = "SECRET_KEY"
ALGORITHM = "HS256"
pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")


def verify_password(plain: str, hash: str) -> bool:
    return pwd_context.verify(plain, hash)


def get_hash(plain: str) -> str:
    return pwd_context.hash(plain)


def get_jwt_username(token: str) -> str | None:
    try:
        payload = jwt.decode(token, SECRET_KEY, algorithms=[ALGORITHM])
        username = payload.get("sub")
        if not username:
            return None
    except JWTError:
        return None
    return username


def get_user(username: str) -> User | None:
    user = data.get_one(username)
    if user:
        return user
    return None


def get_current_user(token: str) -> User | None:
    username = get_jwt_username(token)
    if not username:
        return None
    user = get_user(username)
    if user:
        return user
    return None


def auth_user(name: str, plain: str) -> User | None:
    user = get_user(name)
    if not user:
        return None
    if not verify_password(plain, user.hash):
        return None
    return user


def create_access_token(data: dict, expires: timedelta | None = None):
    src: dict = data.copy()
    now: datetime = datetime.now()
    if not expires:
        expires = timedelta(minutes=15)
    src.update({"exp": now + expires})
    encode_jwt: str = jwt.encode(src, SECRET_KEY, algorithm=ALGORITHM)
    return encode_jwt
