import os
import pytest

from model.user import User

os.environ["CREATURE_SQLITE_DB"] = ":memory:"
from data import user


@pytest.fixture
def sample() -> User:
    return User(
        name="Max",
        hash="secret",
    )


def test_create(sample):
    result = user.create(sample)
    assert sample == result
