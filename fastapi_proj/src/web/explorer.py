from fastapi import APIRouter

from fake import explorer as service
from model.explorer import Explorer

router = APIRouter(prefix="/explorer")


@router.get("/")
def get_all() -> list[Explorer]:
    return service.get_all_explores()


@router.get("/{name}")
def get_one(name: str) -> Explorer:
    return service.get_one_explorer(name)


@router.post("/")
def create(explorer: Explorer) -> Explorer:
    return service.create_explorer(explorer)


@router.patch("/")
def create(explorer: Explorer) -> Explorer:
    return service.update_explorer(explorer)


@router.put("/")
def create(explorer: Explorer) -> Explorer:
    return service.replace_explorer(explorer)


@router.delete("/{name}")
def create(name: str) -> Explorer:
    return service.delete_explorer(name)
