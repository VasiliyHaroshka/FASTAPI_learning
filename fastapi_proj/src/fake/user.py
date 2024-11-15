from typing import List

from error import Missing, Duplicate
from model.user import User

fake_users = [
    User(
        name="Don",
        hash="1234",
    ),
    User(
        name="Poll",
        hash="qwerty",
    ),
]


def find(name: str) -> User | None:
    for user in fake_users:
        if user.name == name:
            return user
    return None


def check_missing(name: str):
    if not find(name):
        raise Missing(msg=f"User with name = {name} is not found")


def check_duplicate(name: str):
    if find(name):
        raise Duplicate(msg=f"User with name = {name} has duplicate in db")


def get_all() -> list[User]:
    return fake_users


def get_one(name: str) -> User:
    check_missing(name)
    return find(name)


def create(user: User) -> User:
    check_duplicate(user.name)
    return user


def modify(name: str, user: User) -> User:
    check_missing(name)
    return user


def delete(name: str) -> None:
    check_missing(name)
    return None
