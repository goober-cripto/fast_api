from pydantic import BaseModel, ConfigDict


class CategoriRead(BaseModel):
    model_config = ConfigDict(from_attributes=True)

    id: str
    name: str


class CategoriCreate(BaseModel):
    name: str


class CategoriUpdate(BaseModel):
    name: str
