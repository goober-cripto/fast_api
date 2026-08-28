from sqlalchemy.orm import Session

from app.repositories.categori import CategoriRepository
from app.shemas.category import CategoriRead, CategoriUpdate, CategoriCreate


class CategoriesNotFoundError(Exception):
    pass


class CategoriService:
    """Ключевые операции с задачами, включая бизнес-логику, валидацию и прочее"""

    def __init__(self, db: Session):
        self.db = db
        self.repository = CategoriRepository(db)

    def list_categories(self) -> list[CategoriRead]:
        categories = self.repository.get_all()
        return [CategoriRead.model_validate(categori) for categori in categories]

    def create_categori(self, payload: CategoriCreate) -> CategoriRead:
        categori = self.repository.create(name=payload.name)
        self.db.commit()
        return CategoriRead.model_validate(categori)

    def update_categori(self, categori_id: str, payload: CategoriUpdate) -> CategoriRead:
        categori = self.repository.get_by_id(categori_id)

        if categori.name is not None:
            categori.name = payload.name

        self.db.commit()
        return CategoriRead.model_validate(categori)

    def delete_categori(self, task_id: str) -> None:
        categori = self.repository.get_by_id(task_id)

        self.repository.delete(categori)
        self.db.commit()