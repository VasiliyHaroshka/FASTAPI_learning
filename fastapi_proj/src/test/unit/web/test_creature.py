import pytest
import os

from error import Duplicate
from model.creature import Creature

os.environ["CREATURE_SQLITE_DB"] = ":memory:"
from data import creature


@pytest.fixture
def sample() -> Creature:
    return Creature(
        name="Vampire",
        country="ROM",
        area="Transinvania",
        description="Blood sucker",
        aka="Nosferatu",
    )


def test_create(sample):
    result = creature.create(sample)
    assert sample == result


def test_create_duclicate(sample):
   with pytest.raises(Duplicate):
       _ = creature.create(sample)