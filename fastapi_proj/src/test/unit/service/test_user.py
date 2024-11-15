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


def assert_duplicates(exc):
    assert exc.value.status_code == 409
    assert "is already exists" in exc.value.msg


def assert_missing(exc):
    assert exc.value.status_code == 404
    assert "is not found" in exc.value.msg


def test_get_one(sample):
    assert user.create(sample) == sample


def test_get_one_missing():
    with pytest.raises(HTTPException) as exc:
        _ = user.get_one("Jake")
        assert assert_missing(exc)


def test_create(sample):
    return user.create(sample) == sample


def test_create_duplicate(fakes):
    with pytest.raises(HTTPException) as exc:
        _ = user.create(fakes[0])
        assert_duplicates(exc)


def test_modify(fakes):
    return user.modify(fakes[0].name) == fakes[0]


def test_modify_missing(sample):
    with pytest.raises(HTTPException) as exc:
        _ = user.modify(sample.name, sample)
        assert_missing(exc)
