from pydantic import BaseModel


class BaseSchema(BaseModel):
    pass


class ExplorerAddSchema(BaseSchema):
    name: str
    country: str
    description: str


class ExplorerGetSchema(ExplorerAddSchema):
    id: int
