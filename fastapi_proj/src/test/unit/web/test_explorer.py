import os
from dataclasses import MISSING

import pytest
from fastapi import HTTPException

from model.explorer import Explorer

os.environ["CREATURE_UNIT_TEST"] = "true"
from web import explorer


@pytest.fixture
def sample() -> Explorer:
    return Explorer(name="Ron",
                    country="ND",
                    description="Bro",
                    )


@pytest.fixture
def fakes() -> list[Explorer]:
    return explorer.get_all()


def assert_duplicates(exc: Exception):
    assert exc.value.status_code == 404
    assert "is already exists in db" in exc.value.msg


def assert_missing(exc: Exception):
    assert exc.value.status_code == 404
    assert "is not found" in exc.value.msg


def test_create(sample):
    assert explorer.create(sample) == sample


def test_create_duplicates(fakes):
    with pytest.raises(HTTPException) as exc:
        _ = explorer.create(fakes[0])
        assert_duplicates(exc)


def test_get_one(fakes):
    assert explorer.get_one(fakes[0].name) == fakes[0]


def test_get_one_missing():
    with pytest.raises(HTTPException) as exc:
        _ = explorer.get_one("Nobody")
        assert_missing(exc)


def test_modify(fakes):
    assert explorer.modify(fakes[0]) == fakes[0]


def test_modify_missing(sample):
    with pytest.raises(HTTPException) as exc:
        _ = explorer.modify(sample.name, sample)
        assert_missing(exc)
