from fastapi import Depends
from sqlalchemy.orm import Session

from app.db.session import get_db
from app.services.task import TaskService
from app.services.category import CategoriService

def get_task_service(db: Session = Depends(get_db)) -> TaskService:
    return TaskService(db)

def get_categori_service(db: Session = Depends(get_db)) -> CategoriService:
    return CategoriService(db)