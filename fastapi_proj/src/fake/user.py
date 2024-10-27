from error import Missing
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
