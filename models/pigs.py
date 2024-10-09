from .base import Base

class Pig(Base, table=True):
    __tablename__ = "pigs"

    pig_housee: str
    pig_name: str
