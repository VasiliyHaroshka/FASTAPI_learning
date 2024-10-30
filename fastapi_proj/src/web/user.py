import os

from fastapi import APIRouter, HTTPException
from fastapi.security import OAuth2PasswordBearer

if os.getenv("CREATURE_UNIT_TEST"):
    from fake.user import fake_users as service
else:
    from service import user as service

ACCESS_TOKEN_EXPIRE_MINUTES = 30

router = APIRouter(prefix="/user")

# this dependency return assess token
oauth2_dependency = OAuth2PasswordBearer(tokenUrl="token")


def unauthorised():
    raise HTTPException(
        status_code=401,
        detail="Error! Wrong username or password",
        headers={"WWW-Authenticate": "Bearer"},
    )