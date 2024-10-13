from ..model.creature import Creature

fake_creatures = [
    Creature(
        name="Vampire",
        country="ROM",
        area="Castle",
        description="bla-bla-bla",
        aka="blood",
    ),
    Creature(
        name="Butcher",
        country="FR",
        area="Paris",
        description="bla-bla-bla",
        aka="knife keeper",
    ),
]


def get_all_explores() -> list[Creature]:
    return fake_creatures


def get_one_explorer(name: str) -> Creature | None:
    for creature in fake_creatures:
        if creature.name == name:
            return creature
    return None


def create_explorer(creature: Creature) -> Creature:
    return creature


def update_explorer(creature: Creature) -> Creature:
    return creature


def replace_explorer(creature: Creature) -> Creature:
    return creature


def delete_explorer(name: str) -> Creature | None:
    for creature in fake_creatures:
        if creature.name == name:
            fake_creatures.remove(creature)
            return creature
    return None
