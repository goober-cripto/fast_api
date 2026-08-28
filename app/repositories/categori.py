from sqlalchemy import select
from sqlalchemy.orm import Session

from app.modeles.categori import CategoriORM


class CategoriRepository:
    """Ключевые операции с таблицей categories в БД"""

    def __init__(self, db: Session):
        self.db = db

    def get_all(self) -> list[CategoriORM]:
        """Получить все записи categories"""
        return self.db.scalars(select(CategoriORM)).all()

    def get_by_id(self, categori_id: str) -> CategoriORM | None:
        """Получить запись categories по id"""
        return self.db.get(CategoriORM, categori_id)

    def create(self, name: str) -> CategoriORM:
        """Создать запись categories"""
        task = CategoriORM(name=name)
        self.db.add(task)
        return task

    def delete(self, categori: CategoriORM) -> None:
        """Удалить запись categories"""
        self.db.delete(categori)