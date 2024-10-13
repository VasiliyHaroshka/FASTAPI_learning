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


def get_all_explores() -> list[Explorer]:
    return fake_explores


def get_one_explorer(name: str) -> Explorer | None:
    for explorer in fake_explores:
        if explorer.name == name:
            return explorer
    return None


def create_explorer(explorer: Explorer) -> Explorer:
    return explorer


def update_explorer(explorer: Explorer) -> Explorer:
    return explorer


def replace_explorer(explorer: Explorer) -> Explorer:
    return explorer


def delete_explorer(name: str) -> Explorer | None:
    for explorer in fake_explores:
        if explorer.name == name:
            fake_explores.remove(explorer)
            return explorer
    return None
