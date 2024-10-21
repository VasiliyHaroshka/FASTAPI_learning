import pytest
import os

from model.creature import Creature

os.environ["CREATURE_SQLITE_DB"] = ":memory:"


@pytest.fixture
def sample() -> Creature:
    return Creature(
        name="Vampire",
        country="ROM",
        area="Transinvania",
        description="Blood sucker",
        aka="Nosferatu",
    )
