from data.init import cur
from model.explorer import Explorer

cur.execute("""
    CREATE TABLE IF NOT EXISTS Explorer(
    name PRIMARY KEY,
    country text,
    description text)
""")


def row_to_model(row: tuple) -> Explorer:
    name, country, description = row
    return Explorer(name, country, description)


def model_to_dict(explorer: Explorer) -> dict:
    if explorer:
        return explorer.dict()


def get_one(name: str) -> Explorer:
    query = "SELECT * FROM Explorer WHERE name=:name"
    params = {"name": name}
    cur.execute(query, params)
    return row_to_model(cur.fetchone())


def get_all() -> list[Explorer]:
    query = "SELECT * FROM Explorer"
    cur.execute(query).fetchall()
    return [row_to_model(explorer) for explorer in cur.fetchall()]


def create(explorer: Explorer) -> Explorer:
    query = """INSERT INTO Explorer name, country, description
                VALUES(:name, :country, :description)"""
    params = model_to_dict(explorer)
    cur.execute(query, params)
    return get_one(explorer.name)


def modify(name: str, explorer: Explorer) -> Explorer:
    query = """UPDATE Explorer SET 
    name=:name,
    country=:country,
    description=:description
    WHERE name:=name_from_query"""
    params = model_to_dict(explorer)
    params["name_from_query"] = explorer.name
    cur.execute(query, params)
    new_explorer = get_one(explorer.name)
    return new_explorer


def delete(explorer: Explorer) -> bool:
    query = """DELETE FROM Explorer WHERE name=:name"""
    params = {"name": explorer.name}
    result = cur.execute(query, params)
    return bool(result)