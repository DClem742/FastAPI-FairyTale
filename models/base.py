from sqlmodel import SQLModel, Field

class Base(SQLModel):
    id: int = Field(
        primary_key=True,
        default=None,
        index=True,
        nullable=False
    )
