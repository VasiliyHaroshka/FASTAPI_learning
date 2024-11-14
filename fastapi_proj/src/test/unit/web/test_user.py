import os

import pytest

from fastapi import HTTPException

os.environ["CREATURE_UNIT_TEST"] = "true"

from error import Duplicate, Missing
from model.user import User
from web import user


@pytest.fixture
def sample():
    return User(
        name="Max",
        hash="MaxPain1990",
    )


@pytest.fixture
def fakes() -> list[User]:
    return user.get_all()


def assert_duplicates(exc):
    assert exc.value.status_code == 409
    assert "is already exists" in exc.value.msg


def assert_missing(exc):
    assert exc.value.status_code == 404
    assert "is not found" in exc.value.msg
