import os

import pytest
from fastapi import HTTPException

os.environ["CREATURE_UNIT_TEST"] = "true"
from model.user import User
from service import user
