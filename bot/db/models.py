from sqlalchemy.dialects.postgresql import BIGINT
from sqlalchemy.orm import mapped_column, Mapped, DeclarativeBase


class Base(DeclarativeBase):
    pass


class User(Base):
    __tablename__ = "users"

    id: Mapped[int] = mapped_column(BIGINT, primary_key=True, autoincrement=False)
    balance: Mapped[int] = mapped_column(BIGINT, nullable=False, default=0)
