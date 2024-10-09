from .base import Base

class Wolf(Base, table=True):
    __tablename__ = "wolves"

    name: str
    power: int