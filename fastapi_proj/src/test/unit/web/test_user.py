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


def test_create(sample):
    assert user.create(sample) == sample


def test_create_duplicate(fakes):
    with pytest.raises(HTTPException) as exc:
        result = user.create(fakes[0])
        assert_duplicates(exc)


def test_get_one(fakes):
    assert user.get_one(fakes[0].name) == fakes[0]


def test_get_one_missing():
    with pytest.raises(HTTPException) as exc:
        assert user.get_one("Phill")
        assert assert_missing(exc)


def test_modify(fakes):
    assert user.modify(fakes[0].name) == fakes[0]


def test_modify_missing(sample):
    with pytest.raises(HTTPException) as exc:
        result = user.modify(sample.name, sample)
        assert_missing(exc)


def test_delete(fakes):
    assert user.delete(fakes[0].name) is None


def test_delete_missing():
    with pytest.raises(HTTPException) as exc:
        result = user.delete("Mo")
        assert_missing(exc)
