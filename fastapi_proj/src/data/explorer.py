from fastapi import Depends
from sqlalchemy import select, update, delete

from data.init import curs
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
    query = select(Explorer).filter(Explorer.id == data.name)
    result = await session.execute(query)
    if result:
        return result.scalars().first()
    raise Missing(msg=f"Explorer {data.name} is not found")


async def get_all(session) -> list[Explorer] | dict:
    query = select(Explorer)
    result = await session.execute(query)
    if result:
        return result.scalars().all()
    return {"message": "there is no explorers yet"}


async def create(data: ExplorerAddSchema, session: Depends(get_session)):
    new_explorer = Explorer(
        name=data.name,
        country=data.country,
        description=data.description,
    )
    all_explorers = select(Explorer)
    if new_explorer in all_explorers:
        raise Duplicate(msg=f"User with username = {new_explorer.name} is already exists in db")
    session.add(new_explorer)
    await session.commit()
    return get_one(new_explorer.name)


async def modify(
        new_data: ExplorerAddSchema,
        session=Depends(get_session)):
    stmt = (
        update(Explorer)
        .filter(Explorer.name == new_data.name)
        .values(
            name=new_data.name,
            country=new_data.country,
            description=new_data.description,
        )
    )
    session.add(stmt)
    await session.commit()
    explorer = get_one(data=new_data, session=session)
    return explorer


def delete_explorer(name: ExplorerGetSchema, session = Depends(get_session)):
    if not name:
        raise Missing(msg=f"Explorer {name} is not found")
    stmt = delete(Explorer).filter(Explorer.name == name)
    session.execute(stmt)
    return True
