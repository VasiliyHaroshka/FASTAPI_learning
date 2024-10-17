from data import explorer as data
from model.explorer import Explorer


def get_all() -> list[Explorer]:
    return data.get_all()


def get_one(name: str) -> Explorer:
    return data.get_one(name)


def create(explorer: Explorer) -> Explorer:
    return data.create(explorer)


def modify(explorer: Explorer) -> Explorer:
    return data.modify(explorer)


def delete(explorer: Explorer) -> bool:
    return data.delete(explorer)
