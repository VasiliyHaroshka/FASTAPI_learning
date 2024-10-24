from data.init import curs
from error import Missing
from model.creature import Creature

curs.execute(
    """CREATE TABLE IF NOT EXISTS Creature(
    name text PRIMARY KEY, 
    country text, 
    area text, 
    description text, 
    aka text)""")


def row_to_model(row: tuple) -> Creature:
    name, country, area, description, aka = row
    return Creature(
        name=name,
        country=country,
        area=area,
        description=description,
        aka=aka,
    )


def model_to_dict(creature: Creature) -> dict:
    if creature:
        return creature.model_dump()


def get_one(name: str) -> Creature:
    query = "SELECT * FROM Creature WHERE name=:name"
    params = {"name": name}
    curs.execute(query, params)
    row = curs.fetchone()
    if row:
        return row_to_model(row)
    else:
        raise Missing(msg=f"Creature {name} is not found")


def get_all() -> list[Creature]:
    query = "SELECT * FROM Creature"
    curs.execute(query)
    return [row_to_model(row) for row in curs.fetchall()]


def create(creature: Creature) -> Creature:
    query = """INSERT INTO Creature (name, country, area, description, aka)
    VALUES (:name, :country, :area, :description, :aka)"""
    params = model_to_dict(creature)
    curs.execute(query, params)
    return get_one(creature.name)


def modify(name: str, creature: Creature) -> Creature:
    query = """UPDATE Creature SET
    name=:name,
    country=:country,
    area=:area,
    description=:description,
    aka=:aka
    WHERE name=:name_from_query
    """
    params = model_to_dict(creature)
    params["name_from_query"] = name
    curs.execute(query, params)
    if curs.rowcount == 1:
        return get_one(creature.name)
    else:
        raise Missing(msg=f"Creature {name} not found")


def delete(name: str):
    if not name:
        return False
    query = "DELETE FROM Creature WHERE name=:name"
    params = {"name": name}
    curs.execute(query, params)
    if curs.rowcount == 1:
        raise Missing(msg=f"Creature {name} is not found")
