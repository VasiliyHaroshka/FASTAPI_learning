import os
import pytest

from error import Duplicate, Missing
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


def test_create_duplicate(sample):
    with pytest.raises(Duplicate):
        _ = user.create(sample)


def test_get_one(sample):
    result = user.get_one(sample.name)
    assert result == sample


def test_get_one_missing():
    with pytest.raises(Missing):
        _ = user.get_one("Pit")


def test_modify(sample):
    sample.hash = "abc"
    result = user.modify(sample.name, sample)
    assert result == sample


def test_modify_missing():
    other_user: User = User(name="Poll", hash="Poll's hash")
    with pytest.raises(Missing):
        _ = user.modify(other_user.name, other_user)


def test_delete(sample):
    result = user.delete(sample.name)
    assert result is None
