from .base import Base
from sqlmodel import Field

class House(Base, table=True):
    __tablename__ = "houses"

    type: str
    sturdiness: int
    pig_id: int = Field(default=None, foreign_key="pigs.id")