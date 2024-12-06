from sqlalchemy.orm import Mapped, mapped_column

from base import Base


class Explorer(Base):
    __tablename__ = "explorer"

    id: Mapped[int] = mapped_column(primary_key=True, autoincrement=True)
    name: Mapped[str] = mapped_column(nullable=False)
    country: Mapped[str] = mapped_column(nullable=False)
    description: Mapped[str] = mapped_column(nullable=True)
