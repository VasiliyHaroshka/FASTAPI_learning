import os
from datetime import timedelta

from fastapi import APIRouter, HTTPException
from fastapi.params import Depends
from fastapi.security import OAuth2PasswordBearer, OAuth2PasswordRequestForm

from error import Missing, Duplicate
from model.user import User

if os.getenv("CREATURE_UNIT_TEST"):
    from fake.user import fake_users as service
else:
    from service import user as service

ACCESS_TOKEN_EXPIRE_MINUTES = 30

router = APIRouter(prefix="/user")

# this dependency return access token
oauth2_dependency = OAuth2PasswordBearer(tokenUrl="token")


def unauthorised():
    raise HTTPException(
        status_code=401,
        detail="Error! Wrong username or password",
        headers={"WWW-Authenticate": "Bearer"},
    )


@router.post("/token")
async def create_access_token(form_data: OAuth2PasswordRequestForm = Depends()):
    user = service.auth_user(
        form_data.username,
        form_data.password,
    )
    if not user:
        unauthorised()
    expires = timedelta(minutes=ACCESS_TOKEN_EXPIRE_MINUTES)
    access_token = service.create_access_token(
        data={"sub": user.username},
        expires=expires,
    )
    return {"access_token": access_token, "token_type": "bearer"}


@router.get("/token")
def get_access_token(token: str = Depends(oauth2_dependency)) -> dict:
    """Return current access token"""
    return {"token": token}


@router.get("/")
def get_all() -> list[User]:
    return service.get_all()


@router.get("/{name}")
def get_one(name: str) -> User:
    try:
        return service.get_one(name)
    except Missing as e:
        raise HTTPException(status_code=404, detail=e.msg)


@router.post("/", status_code=201)
def create(user: User) -> User:
    try:
        return service.create(user)
    except Duplicate as e:
        raise HTTPException(status_code=409, detail=e.msg)


@router.patch("/{name}")
def modify(name: str, user: User) -> User:
    try:
        return service.modify(name, user)
    except Missing as e:
        raise HTTPException(status_code=404, detail=e.msg)


@router.delete("/{name}")
def delete(name: str) -> None:
    try:
        service.delete(name)
    except Missing as e:
        raise HTTPException(status_code=404, detail=e.msg)
