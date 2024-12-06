from typing import Annotated

from fastapi import Depends
from sqlalchemy.ext.asyncio import AsyncSession

from data.init import curs, IntegrityError
from db import get_session
from error import Duplicate, Missing
from model.explorer import Explorer
from schemas.explorer import ExplorerAddSchema

Session_dep = Annotated[AsyncSession, Depends(get_session)]

curs.execute("""
    CREATE TABLE IF NOT EXISTS Explorer(
    name text PRIMARY KEY,
    country text,
    description text)""")


def row_to_model(row: tuple) -> Explorer:
    name, country, description = row
    return Explorer(
        name=name,
        country=country,
        description=description,
    )


def model_to_dict(explorer: Explorer) -> dict:
    if explorer:
        return explorer.model_dump()


def get_one(name: str) -> Explorer:
    query = "SELECT * FROM Explorer WHERE name=:name"
    params = {"name": name}
    curs.execute(query, params)
    row = curs.fetchone()
    if row:
        return row_to_model(row)
    raise Missing(msg=f"Explorer {name} is not found")


def get_all() -> list[Explorer]:
    query = "SELECT * FROM Explorer"
    curs.execute(query)
    return [row_to_model(row) for row in curs.fetchall()]


# def create(explorer: Explorer) -> Explorer:
#     if not explorer:
#         return None
#     query = """INSERT INTO Explorer (name, country, description)
#                 VALUES (:name, :country, :description)"""
#     params = model_to_dict(explorer)
#     try:
#         curs.execute(query, params)
#     except IntegrityError:
#         raise Duplicate(msg=f"Explorer {explorer.name} is already exists in db")
#     return get_one(explorer.name)


async def create(data: ExplorerAddSchema, session: Session_dep):
    new_explorer = Explorer(
        name=data.name,
        country=data.country,
        description=data.description,
    )
    session.add(new_explorer)
    await session.commit()
    return get_one(new_explorer.name)


def modify(name: str, explorer: Explorer) -> Explorer:
    query = """UPDATE Explorer SET 
    name=:name,
    country=:country,
    description=:description
    WHERE name=:name_from_query"""
    params = model_to_dict(explorer)
    params["name_from_query"] = explorer.name
    curs.execute(query, params)
    if curs.rowcount == 1:
        return get_one(explorer.name)
    raise Missing(msg=f"Explorer {name} is not found")


def delete(name: str):
    if not name:
        return False
    query = """DELETE FROM Explorer WHERE name=:name"""
    params = {"name": name}
    curs.execute(query, params)
    if curs.rowcount != 1:
        raise Missing(msg=f"Explorer {name} is not found")
