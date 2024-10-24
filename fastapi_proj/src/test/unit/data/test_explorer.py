import os
import pytest

from error import Duplicate, Missing
from model.explorer import Explorer

os.environ["EXPLORER_SQLITE_DB"] = ":memory:"
from data import explorer


@pytest.fixture
def sample() -> Explorer:
    return Explorer(
        name="John",
        country="US",
        description="Superman",
    )
