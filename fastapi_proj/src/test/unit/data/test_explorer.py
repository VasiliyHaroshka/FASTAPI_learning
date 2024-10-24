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


def test_get_one(sample):
    result = explorer.get_one(sample.name)
    assert result == sample


def test_get_one_missing():
    with pytest.raises(Missing):
        _ = explorer.get_one("Mike")


def test_modify(sample):
    explorer.country = "D"
    result = explorer.modify(sample.name, sample)
    assert result == sample


def test_modify_missing():
    another_sample: Explorer = Explorer(
        name="Bob",
        country="PL",
        description="pan Bob",
    )
    with pytest.raises(Missing):
        _ = explorer.modify(another_sample.name, another_sample)


def test_delete(sample):
    result = explorer.delete(sample.name)
    assert result is None


def test_delete_missing(sample):
    with pytest.raises(Missing):
        _ = explorer.delete(sample.name)
