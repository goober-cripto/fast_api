from fastapi import APIRouter, Depends, HTTPException, status

from app.api.dependencies import get_categori_service
from app.shemas.category import CategoriRead, CategoriUpdate, CategoriCreate
from app.services.category import CategoriesNotFoundError, CategoriService


router = APIRouter(prefix="/categories", tags=["categories"])


@router.get("", response_model=list[CategoriRead])
def get_tasks(service: CategoriService = Depends(get_categori_service)) -> list[CategoriRead]:
    return service.list_categories()


@router.post("", response_model=CategoriRead, status_code=status.HTTP_201_CREATED)
def create_task(
    payload: CategoriCreate,
    service: CategoriService = Depends(get_categori_service),
) -> CategoriRead:
    return service.create_categori(payload)


@router.patch("/{categories_id}", response_model=CategoriRead)
def update_task(
    categories_id: str,
    payload: CategoriUpdate,
    service: CategoriService = Depends(get_categori_service),
) -> CategoriRead:
    try:
        return service.update_categori(categories_id, payload)
    except CategoriesNotFoundError:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Категория не найдена",
        )


@router.delete("/{categories_id}", status_code=status.HTTP_204_NO_CONTENT)
def delete_task(
    categories_id: str,
    service: CategoriService = Depends(get_categori_service),
) -> None:
    try:
        service.delete_categori(categories_id)
    except CategoriesNotFoundError:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Категория не найдена",
        )