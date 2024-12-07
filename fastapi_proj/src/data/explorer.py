from typing import Annotated

from fastapi import Depends
from sqlalchemy import select
from sqlalchemy.ext.asyncio import AsyncSession

from data.init import curs, IntegrityError
from db import get_session
from error import Duplicate, Missing
from model.explorer import Explorer
from schemas.explorer import ExplorerAddSchema, ExplorerGetSchema

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


async def get_one(data: ExplorerGetSchema, session: Depends(get_session)) -> Explorer:
    query = select(Explorer).where(name=data.name)
    result = await session.execute(query)
    if result:
        return result.scalars().one()
    raise Missing(msg=f"Explorer {data.name} is not found")


async def get_all(session: Depends(get_session)) -> list[Explorer] | dict:
    query = select(Explorer)
    result = await session.execute(query)
    if result:
        return result.scalars().all()
    return {"message": "there is no explorers yet"}


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


async def create(data: ExplorerAddSchema, session: Depends(get_session)):
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
