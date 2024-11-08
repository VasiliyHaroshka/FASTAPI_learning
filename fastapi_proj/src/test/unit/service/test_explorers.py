import os

import pytest

from fastapi import HTTPException

os.environ["CREATURE_UNIT_TEST"] = "true"

from model.explorer import Explorer
from web import explorer


@pytest.fixture
def sample():
    return Explorer(
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
