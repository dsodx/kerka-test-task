from typing import Dict, Any

from sqlalchemy.dialects.postgresql import BIGINT, BOOLEAN
from sqlalchemy.orm import mapped_column, Mapped, DeclarativeBase


class Base(DeclarativeBase):
    pass


class User(Base):
    __tablename__ = "users"

    id: Mapped[int] = mapped_column(BIGINT, primary_key=True, autoincrement=False)
    balance: Mapped[int] = mapped_column(BIGINT, nullable=False, default=0)
    banned: Mapped[bool] = mapped_column(BOOLEAN, nullable=False, default=False)

    def as_dict(self) -> Dict[str, Any]:
        """
        Получить объект пользователя в виде словаря
        :return: объект пользователя в виде словаря
        """
        return {
            "id": int(self.id),
            "balance": int(self.balance),
            "banned": bool(self.banned)
        }
