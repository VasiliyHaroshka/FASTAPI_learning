import os

import pytest

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
