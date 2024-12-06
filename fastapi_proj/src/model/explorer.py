from sqlalchemy.orm import Mapped, mapped_column

from base import Base


class Explorer(Base):
    __tablename__ = "explorer"

    id: Mapped[int] = mapped_column(primary_key=True)
    name: Mapped[str] = mapped_column()
    country: Mapped[str] = mapped_column()
    description: Mapped[str] = mapped_column()
