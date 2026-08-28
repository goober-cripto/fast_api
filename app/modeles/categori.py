from sqlalchemy.orm import Mapped, mapped_column

from app.modeles.base import Base


class CategoriORM(Base):
    """Модель задачи в БД"""

    __tablename__ = "categories"

    name: Mapped[str]
    