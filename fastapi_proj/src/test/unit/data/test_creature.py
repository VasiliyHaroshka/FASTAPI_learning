import pytest
import os

from error import Duplicate, Missing
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


def test_get_one(sample):
    result = creature.get_one(sample.name)
    assert result == sample

def test_get_one_missing(sample):
    with pytest.raises(Missing):
        _ = creature.get_one("Loki")