import os

import pytest

from error import Duplicate

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



