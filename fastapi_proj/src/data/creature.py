from data.init import cur
from model.creature import Creature

cur.execute(
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
        aka=aka
    )


def model_to_dict(creature: Creature) -> dict:
    return creature.dict()


def get_one(name: str) -> Creature:
    query = "SELECT * FROM Creature WHERE name=:name"
    params = {"name": name}
    cur.execute(query, params)
    row = cur.fetchone()
    return row_to_model(row)


def get_all() -> list[Creature]:
    query = "SELECT * FROM Creature"
    cur.execute(query)
    rows = cur.fetchall()
    return [row_to_model(row) for row in rows]


def create(creature: Creature) -> Creature:
    query = """INSERT INTO Creature VALUES
    (:name, :description, :country, :area, :aka)"""
    params = model_to_dict(creature)
    cur.execute(query, params)
    return get_one(creature.name)


def modify(crature: Creature) -> Creature:
    query = """UPDATE Creature SET
    name=:name,
    country=:country,
    description=:description,
    area=:area,
    aka=:aka
    WHERE name=:name_from_query
    """
    params = model_to_dict(crature)
    params["name_from_query"] = crature.name
    cur.execute(query, params)
    return get_one(creature.name)


def delete(craeture: Creature) -> bool:
    query = "DELETE FROM Creatures WHERE name=:name"
    params = {"name": craeture.name}
    result = cur.execute(query, params)
    return bool(result)
