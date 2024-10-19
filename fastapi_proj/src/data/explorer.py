from data.init import curs
from model.explorer import Explorer

curs.execute("""
    CREATE TABLE IF NOT EXISTS Explorer(
    name text PRIMARY KEY,
    country text,
    description text)""")


def row_to_model(row: tuple) -> Explorer:
    return Explorer(
        name=row[0],
        country=row[1],
        description=row[2],
    )


def model_to_dict(explorer: Explorer) -> dict:
    if explorer:
        return explorer.dict()


def get_one(name: str) -> Explorer:
    query = "SELECT * FROM Explorer WHERE name=:name"
    params = {"name": name}
    curs.execute(query, params)
    return row_to_model(curs.fetchone())


def get_all() -> list[Explorer]:
    query = "SELECT * FROM Explorer"
    curs.execute(query).fetchall()
    return [row_to_model(explorer) for explorer in curs.fetchall()]


def create(explorer: Explorer) -> Explorer:
    query = """INSERT INTO Explorer (name, country, description)
                VALUES (:name, :country, :description)"""
    params = model_to_dict(explorer)
    _ = curs.execute(query, params)
    return get_one(explorer.name)


def modify(name: str, explorer: Explorer) -> Explorer:
    query = """UPDATE Explorer SET 
    name=:name,
    country=:country,
    description=:description
    WHERE name:=name_from_query"""
    params = model_to_dict(explorer)
    params["name_from_query"] = explorer.name
    curs.execute(query, params)
    new_explorer = get_one(explorer.name)
    return new_explorer


def delete(explorer: Explorer) -> bool:
    query = """DELETE FROM Explorer WHERE name=:name"""
    params = {"name": explorer.name}
    result = curs.execute(query, params)
    return bool(result)