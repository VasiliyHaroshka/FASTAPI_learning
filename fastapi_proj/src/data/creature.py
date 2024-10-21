from data.init import curs
from model.creature import Creature

curs.execute(
    """CREATE TABLE IF NOT EXISTS Creature(
    name text PRIMARY KEY, 
    description text, 
    country text, 
    area text, 
    aka text
    )"""
)


def row_to_model(row: tuple) -> Creature:
    name, description, country, area, aka = row
    return Creature(
        name=name,
        description=description,
        country=country,
        area=area,
        aka=aka,
    )


def model_to_dict(creature: Creature) -> dict:
    if creature:
        return creature.dict()


def get_one(name: str) -> Creature:
    query = "SELECT * FROM Creature WHERE name=:name"
    params = {"name": name}
    curs.execute(query, params)
    row = curs.fetchone()
    return row_to_model(row)


def get_all() -> list[Creature]:
    query = "SELECT * FROM Creature"
    curs.execute(query)
    rows = curs.fetchall()
    return [row_to_model(row) for row in rows]


def create(creature: Creature) -> Creature:
    query = """INSERT INTO Creature (name, country, area, description, aka)
    VALUES (:name, :country, :area, :description, :aka)"""
    params = model_to_dict(creature)
    curs.execute(query, params)
    return get_one(creature.name)


def modify(creature: Creature) -> Creature:
    query = """UPDATE Creature SET
    name=:name,
    country=:country,
    description=:description,
    area=:area,
    aka=:aka
    WHERE name=:name_from_query
    """
    params = model_to_dict(creature)
    params["name_from_query"] = creature.name
    curs.execute(query, params)
    return get_one(creature.name)


def delete(name: str) -> bool:
    query = "DELETE FROM Creatures WHERE name=:name"
    params = {"name": name}
    result = curs.execute(query, params)
    return bool(result)
