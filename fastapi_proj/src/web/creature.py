from fastapi import APIRouter

from service import creature as service
from model.creature import Creature

router = APIRouter(prefix="/creature")


@router.get("/")
def get_all() -> list[Creature]:
    return service.get_all()


@router.get("/{name}")
def get_one(name: str) -> Creature:
    return service.get_one(name)


@router.post("/")
def create(creature: Creature) -> Creature:
    return service.create(creature)


@router.patch("/")
def create(creature: Creature) -> Creature:
    return service.modify(creature)


@router.put("/")
def create(creature: Creature) -> Creature:
    return service.replace(creature)


@router.delete("/{name}")
def delete(creature: Creature) -> bool:
    return service.delete(creature)
