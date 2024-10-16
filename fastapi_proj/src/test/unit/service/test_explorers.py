from model.explorer import Explorer
from service import explorer as my_code

sample = Explorer(
    name="Bob",
    country="GB",
    description="bla-bla-bla",
)


def test_create():
    result = my_code.create(sample)
    assert result == sample


def test_get_and_exist():
    result = my_code.get_one(sample.name)
    assert result == sample


def test_not_found():
    result = my_code.get_one("Max")
    assert None is result
