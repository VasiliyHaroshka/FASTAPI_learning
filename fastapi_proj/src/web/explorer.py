from fastapi import APIRouter

from service import explorer as service
from model.explorer import Explorer

router = APIRouter(prefix="/explorer")


@router.get("/")
def get_all() -> list[Explorer]:
    return service.get_all()


@router.get("/{name}")
def get_one(name: str) -> Explorer:
    return service.get_one(name)


@router.post("/")
def create(explorer: Explorer) -> Explorer:
    return service.create(explorer)


@router.patch("/")
def create(explorer: Explorer) -> Explorer:
    return service.modify(explorer)


@router.put("/")
def create(explorer: Explorer) -> Explorer:
    return service.create(explorer)


@router.delete("/{name}")
def delete(explorer: Explorer) -> bool:
    return service.delete(explorer)
