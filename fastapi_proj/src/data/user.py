from model.user import User
from error import Duplicate, Missing
from .init import curs, IntegrityError

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


def get_all() -> list[User]:
    query = "SELECT * FROM User"
    curs.execute(query)
    return [row_to_model(row) for row in curs.fetchall()]


def create(user: User, table: str = "user") -> User:
    query = f"INSERT INTO {table} (name, hash) VALUES (:name, :hash)"
    params = model_to_dict(user)
    try:
        curs.execute(query, params)
    except IntegrityError:
        raise Duplicate(f"User with username = {user.name} is already exists in the table {table}")
    return user


def modify(name: str, user: User) -> User:
    query = """UPDATE User SET name=:name, hash=:hash
    WHERE name=:name_from_query"""
    params = {
        "name": user.name,
        "hash": user.hash,
        "name_from_query": name,
    }
    curs.execute(query, params)
    if curs.rowcount == 1:
        return get_one(user.name)
    raise Missing(msg=f"User with username = {name} is not found")


def delete(name: str) -> None:
    user = get_one(name)
    query = "DELETE FROM User WHERE name=:name"
    params = {"name": name}
    curs.execute(query, params)
    if curs.rowcount != 1:
        raise Missing(f"User with username = {name} is not found")
    create(user, table="xuser")
