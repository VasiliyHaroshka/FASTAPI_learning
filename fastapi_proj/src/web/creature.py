from fastapi import APIRouter

from fake import creature as service
from model.creature import Creature

router = APIRouter(prefix="/creature")


@router.get("/")
def get_all() -> list[Creature]:
    return service.get_all_creatures()


@router.get("/{name}")
def get_one(name: str) -> Creature:
    return service.get_one_creature(name)


@router.post("/")
def create(creature: Creature) -> Creature:
    return service.create_creature(creature)


@router.patch("/")
def create(creature: Creature) -> Creature:
    return service.update_creature(creature)


@router.put("/")
def create(creature: Creature) -> Creature:
    return service.replace_creature(creature)


@router.delete("/{name}")
def create(name: str) -> Creature:
    return service.delete_creature(name)
