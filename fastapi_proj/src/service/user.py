import os
from pydoc import plain

from passlib.context import CryptContext

if os.getenv("CREATURE_UNIT_TEST"):
    from fake import user as data
else:
    from data import user as data

SECRET_KEY = "SECRET_KEY"
ALGORITHM = "HS256"
pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")


def verify_password(plain: str, hash: str) -> bool:
    return pwd_context.verify(plain, hash)
