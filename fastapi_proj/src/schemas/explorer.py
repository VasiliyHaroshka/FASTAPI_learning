from pydantic import BaseModel


class BaseSchema(BaseModel):
    pass


class ExplorerGetSchema(BaseModel):
    name: str


class ExplorerAddSchema(ExplorerGetSchema):
    country: str
    description: str
