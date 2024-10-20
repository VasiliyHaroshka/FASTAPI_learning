class Missing(Exception):
    """Error for missing object in db"""

    def __init__(self, msg: str):
        self.msg = msg


class Duplicate(Exception):
    """Error when there is a duplicate in db"""

    def __init__(self, msg: str):
        self.msg = msg
