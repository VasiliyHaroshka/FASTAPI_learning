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


def test_create(sample):
    result = explorer.create(sample)
    assert result == sample


def test_crate_duplicate(sample):
    with pytest.raises(Duplicate):
        _ = explorer.create(sample)
