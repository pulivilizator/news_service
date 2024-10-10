from typing import Annotated

from asyncpg import UniqueViolationError
from fastapi import APIRouter, Body
from dishka.integrations.fastapi import DishkaRoute, FromDishka
from sqlalchemy.exc import IntegrityError
from starlette import status

from core import dto
from services import SourceService

router = APIRouter(route_class=DishkaRoute, prefix='/sources')

@router.post(path='/',
             status_code=status.HTTP_201_CREATED,
             response_model=dto.Source | None)
async def create_source(
        new_source: Annotated[dto.CreateSource, Body()],
        service: FromDishka[SourceService]
):
    try:
        source = await service.create_source(new_source)
    except IntegrityError:
        return
    else:
        return source