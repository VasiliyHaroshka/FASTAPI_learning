import os

import pytest

from fastapi import HTTPException

os.environ["CREATURE_UNIT_TEST"] = "true"

from error import Duplicate, Missing
from model.user import User

