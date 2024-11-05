import os
from http.client import HTTPException

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


def assert_duplicates(exc):
    assert exc.value.status_code == 409
    assert "is already exists in db" in exc.value.msg


def assert_missing(exc):
    assert exc.value.status_code == 404
    assert "is not found" in exc.value.msg


def test_create(sample):
    assert creature.create(sample) == sample


def test_create_duplicate(fakes):
    with pytest.raises(HTTPException) as exc:
        _ = creature.create(fakes[0])
        assert_duplicates(exc)


def test_get_one(fakes):
    assert creature.get_one(fakes[0].name) == fakes[0]


def test_get_one_missing():
    with pytest.raises(HTTPException) as exc:
        _ = creature.get_one("Golem")
        assert_missing(exc)
