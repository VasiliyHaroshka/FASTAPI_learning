import os

import pytest

from model.creature import Creature
from web import creature

os.environ["CREATURE_UNIT_TEST"] = "true"


@pytest.fixture
def sample() -> Creature:
    return Creature(
        name="Predator",
        country="S",
        area="Jungle",
        description="it hunts you",
        aka="supervision",
    )


@pytest.fixture
def fakes() -> list[Creature]:
    return creature.get_all()
