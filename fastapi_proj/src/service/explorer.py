from fake import explorer as data
from model.explorer import Explorer


def get_all() -> list[Explorer]:
    return data.get_all_explores()


def get_one(name: str) -> Explorer | None:
    return data.get_one_explorer(name)


def create(explorer: Explorer) -> Explorer:
    return data.create_explorer(explorer)


def replace(explorer: Explorer) -> Explorer:
    return data.replace_explorer(explorer)


def modify(explorer: Explorer) -> Explorer:
    return data.update_explorer(explorer)


def delete(name: str) -> Explorer | None:
    return data.delete_explorer(name)
