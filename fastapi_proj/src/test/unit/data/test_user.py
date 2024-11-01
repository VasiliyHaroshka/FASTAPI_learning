import os
import pytest

from model.user import User

os.environ["CREATURE_SQLITE_DB"] = ":memory:"
from data import user


@pytest.fixture
def sample():
    return User(
        name="Max",
        hash="secret",
    )
