from typing import Optional
from sqlalchemy.orm import Mapped, mapped_column
from datetime import datetime

from models.base import Base


class Application(Base):
    __tablename__ = "requests"
    
    id: Mapped[Optional[int]] = mapped_column( primary_key=True, autoincrement=True)
    user_name: Mapped[str] = mapped_column(nullable=False)
    description: Mapped[str] = mapped_column(nullable=True)
    created_at: Mapped[datetime] = mapped_column(
        default=datetime.utcnow, nullable=False
    )

    def __repr__(self) -> str:
        return (
            f"{self.__class__.__name__}(id={self.id}, user_name={self.user_name},"
            f"description={self.description}, created_at={self.created_at})"
        )
