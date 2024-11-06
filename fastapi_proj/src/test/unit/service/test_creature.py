import os

import pytest

from error import Duplicate, Missing

os.environ["CREATURE_UNIT_TEST"] = "true"

from model.creature import Creature
from data import creature as data

@pytest.fixture
def sample():
    return Creature(
        name="Vampire",
        country="ROM",
        area="Castle",
        description="bla-bla-bla",
        aka="blood",
    )


def test_create(sample: Creature):
    assert data.create(sample) == sample

def test_create_duplicate(sample: Creature):
    result = data.create(sample)
    assert result == sample
    with pytest.raises(Duplicate):
        result = data.create(sample)

def test_get_one(sample: Creature):
    result = data.create(sample)
    assert result == sample
    result = data.get_one(sample.name)
    assert result == sample


def test_get_one_missing():
    with pytest.raises(Missing):
        _ = data.get_one("Devil")

