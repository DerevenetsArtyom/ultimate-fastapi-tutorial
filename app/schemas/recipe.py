from pydantic import BaseModel, HttpUrl

from typing import Sequence


class RecipeBase(BaseModel):
    label: str
    source: str
    url: HttpUrl


class RecipeCreate(RecipeBase):
    label: str
    source: str
    url: HttpUrl
    submitter_id: int


class RecipeUpdate(RecipeBase):
    label: str


# Properties shared by models stored in DB
class RecipeInDBBase(RecipeBase):
    """
    Why make the distinction between a Recipe and RecipeInDB?
    This allows in future to separate fields which are only relevant for the DB,
    or which we don’t want to return to the client (such as a password field).
    """

    id: int
    submitter_id: int

    class Config:
        # It tells Pydantic model to read the data even if it is not a dict, but an ORM model
        # (or any other arbitrary object with attributes). Without orm_mode, if you returned a SQLAlchemy model
        # from your path operation, it wouldn't include the relationship data.
        orm_mode = True


# Properties to return to client
class Recipe(RecipeInDBBase):
    pass


# Properties stored in DB
class RecipeInDB(RecipeInDBBase):
    pass


class RecipeSearchResults(BaseModel):
    results: Sequence[Recipe]
