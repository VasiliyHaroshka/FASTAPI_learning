from model.explorer import Explorer

fake_explores = [
    Explorer(
        name="Bob",
        country="GB",
        description="bla-bla-bla",
    ),
    Explorer(
        name="Tom",
        country="USA",
        description="bla-bla-bla",
    ),
]


def get_all() -> list[Explorer]:
    return fake_explores


def get_one(name: str) -> Explorer | None:
    for explorer in fake_explores:
        if explorer.name == name:
            return explorer
    return None


def create(explorer: Explorer) -> Explorer:
    return explorer


def modify(explorer: Explorer) -> Explorer:
    return explorer


def replace(explorer: Explorer) -> Explorer:
    return explorer


def delete(name: str) -> Explorer | None:
    for explorer in fake_explores:
        if explorer.name == name:
            fake_explores.remove(explorer)
            return None
