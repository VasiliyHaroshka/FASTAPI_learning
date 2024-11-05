import os

import pytest

from error import Duplicate
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


def assert_duplicates(exc):
    assert exc.value.status_code == 409
    assert "is already exists in db" in exc.value.msg


def assert_missing(exc):
    assert exc.value.status_code == 404
    assert "is not found" in exc.value.msg


def test_create(sample):
    assert creature.create(sample) == sample

def test_create_duplicate(fakes):
    with pytest.raises(Duplicate) as exc:
        _ = creature.create(fakes[0])
        assert_duplicates(exc)
