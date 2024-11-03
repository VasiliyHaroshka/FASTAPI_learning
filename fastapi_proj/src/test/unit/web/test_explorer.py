import os

import pytest
from fastapi import HTTPException

from model.explorer import Explorer
from web import explorer

os.environ["CREATURE_UNIT_TEST"] = "true"


@pytest.fixture
def sample():
    return Explorer(name="Ron",
                    country="ND",
                    description="Bro",
                    )


@pytest.fixture
def fakes() -> list[Explorer]:
    return explorer.get_all()
