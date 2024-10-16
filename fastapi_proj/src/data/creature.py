from model.creature import Creature
import sqlite3

DB_NAME = "Creature.db"
conn = sqlite3.connect(DB_NAME)
cur = conn.cursor()


def init():
    cur.execute(
        """CREATE TABLE Creature 
        IF NOT EXISTS 
        (name, description, country, area, aka)"""
    )


def row_to_model(row: tuple) -> Creature:
    name, description, country, area, aka = row
    return Creature(name, description, country, area, aka)


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
    rows = list(cur.fetchmany())
    return [row_to_model(row) for row in rows]


def create(creature: Creature):
    query = """INSERT INTO Creature VALUES
    (:name, :description, :country, :area, :aka)"""
    params = model_to_dict(creature)
    cur.execute(query, params)


def modify(crature: Creature) -> Creature:
    return creature

def replace(crature: Creature) -> Creature:
    return creature

def delete(craeture: Creature):
    query = "DELETE FROM Creatures WHERE name=:name"
    params = {"name": craeture.name}
    cur.execute(query, params)