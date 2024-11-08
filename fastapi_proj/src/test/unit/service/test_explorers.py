import os

import pytest

from fastapi import HTTPException

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
