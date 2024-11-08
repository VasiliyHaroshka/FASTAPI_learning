import os

import pytest

from fastapi import HTTPException

from test.unit.web.test_explorer import assert_duplicates

os.environ["CREATURE_UNIT_TEST"] = "true"

from model.explorer import Explorer
from web import explorer


@pytest.fixture
def sample() -> Explorer:
    return Explorer(
        name="Bob",
        country="GB",
        description="bla-bla-bla",
    )


@pytest.fixture
def fakes() -> list[Explorer]:
    return explorer.get_all()


def assert_duplicate(exc):
    assert exc.value.status_code == 409
    assert "is already exists in db" in exc.value.msg


def assert_missing(exc):
    assert exc.value.status_code == 404
    assert "is not found" in exc.value.msg


def test_create(sample):
    assert explorer.create(sample) == sample


def test_create_duplicate(fakes):
    with pytest.raises(HTTPException) as exc:
        _ = explorer.create(fakes[0])
        assert_duplicates(exc)
