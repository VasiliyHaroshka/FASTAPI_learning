import os

import pytest
from fastapi import HTTPException

os.environ["CREATURE_UNIT_TEST"] = "true"
from model.user import User
from service import user


@pytest.fixture
def sample() -> User:
    return User(
        name="Shon",
        hash="321",
    )


@pytest.fixture
def fakes() -> list[User]:
    return user.get_all()
