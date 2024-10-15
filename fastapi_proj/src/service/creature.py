from fake import creature as data
from model.creature import Creature


def get_all() -> list[Creature]:
    return data.get_all_creatures()


def get_one(name: str) -> Creature | None:
    return data.get_one_creature(name)


def create(creature: Creature) -> Creature:
    return data.create_creature(creature)


def replace(creature: Creature) -> Creature:
    return data.replace_creature(creature)


def modify(creature: Creature) -> Creature:
    return data.update_creature(creature)


def delete(name: str) -> Creature | None:
    return data.delete_creature(name)
