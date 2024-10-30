import os

from fastapi import APIRouter

if os.getenv("CREATURE_UNIT_TEST"):
    from fake.user import fake_users as service
else:
    from service import user as service

router = APIRouter(prefix="/user")
