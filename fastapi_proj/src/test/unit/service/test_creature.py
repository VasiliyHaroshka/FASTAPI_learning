from model.creature import Creature
from service import creature as from_my_code

sample = Creature(
    name="Vampire",
    country="ROM",
    area="Castle",
    description="bla-bla-bla",
    aka="blood",
)


def test_create():
    result = from_my_code.create(sample)
    assert result == sample

def test_get_and_exist():
    result = from_my_code.get_one(sample.name)
    assert result == sample

def test_get_not_found():
    result = from_my_code.get_one("boris")
    assert result is None
