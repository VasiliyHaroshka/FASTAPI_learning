from ecdsa.test_pyecdsa import params

from model.user import User
from error import Duplicate, Missing
from .init import curs, get_db, IntegrityError

curs.execute("""
    CREATE TABLE IF NOT EXISTS 
    User(
    name text PRIMARY KEY,
    hash text
    )""")

curs.execute("""
    CREATE TABLE IF NOT EXISTS 
    XUser(
    name text PRIMARY KEY,
    hash text
    )""")


def row_to_model(row: tuple) -> User:
    name, hash = row
    return User(
        name=name,
        hash=hash
    )


def model_to_dict(user: User) -> dict:
    return user.model_dump()


def get_one(name: str) -> User:
    if not name:
        return False
    query = "SELECT * FROM User WHERE name=:name"
    params = {"name": name}
    curs.execute(query, params)
    row = curs.fetchone()
    if row:
        return row_to_model(row)
    raise Missing(f"User with username = {name} is not found")
