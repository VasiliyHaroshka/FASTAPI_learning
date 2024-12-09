import os

from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session

from db import get_session
from error import Duplicate, Missing
from model.explorer import Explorer

if os.getenv("CREATURE_UNIT_TEST"):
    from fake import explorer as service
else:
    from service import explorer as service

router = APIRouter(prefix="/explorer")


@router.get("/")
def get_all(session = Depends(get_session)) -> list[Explorer]:
    return service.get_all(session)


@router.get("/{name}")
def get_one(name: str) -> Explorer:
    try:
        return service.get_one(name)
    except Missing as exc:
        raise HTTPException(status_code=404, detail=exc.msg)


@router.post("/", status_code=201)
def create(explorer: Explorer) -> Explorer:
    try:
        return service.create(explorer)
    except Duplicate as exc:
        raise HTTPException(status_code=409, detail=exc.msg)


@router.patch("/")
def modify(name: str, explorer: Explorer) -> Explorer:
    try:
        return service.modify(name, explorer)
    except Missing as exc:
        raise HTTPException(status_code=404, detail=exc.msg)


@router.delete("/{name}", status_code=204)
def delete(name: str):
    try:
        return service.delete(name)
    except Missing as exc:
        raise HTTPException(status_code=404, detail=exc.msg)
