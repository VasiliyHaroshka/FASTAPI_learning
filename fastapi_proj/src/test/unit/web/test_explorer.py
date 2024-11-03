import os

import pytest
from fastapi import HTTPException

from model.explorer import Explorer
from web import explorer

os.environ["CREATURE_UNIT_TEST"] = "true"


@pytest.fixture
def sample():
    return Explorer(name="Ron",
                    country="ND",
                    description="Bro",
                    )


@pytest.fixture
def fakes() -> list[Explorer]:
    return explorer.get_all()


def assert_duplicates(exc: Exception):
    assert exc.value.status_code == 404
    assert "is already exists in db" in exc.value.msg


def assert_missing(exc: Exception):
    assert exc.value.status_code == 404
    assert "is not found" in exc.value.msg
