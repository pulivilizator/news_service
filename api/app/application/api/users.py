from typing import Annotated

from fastapi import APIRouter, Body, HTTPException, Path
from dishka.integrations.fastapi import DishkaRoute, FromDishka
from starlette import status

from core import dto
from services import UserService

router = APIRouter(route_class=DishkaRoute, prefix='/user')

@router.post(path='/registration/',
             response_model=dto.User,
             status_code=status.HTTP_201_CREATED)
async def registration(
        user_data: Annotated[dto.UserRegister, Body()],
        service: FromDishka[UserService]
):
    new_user = await service.create_user(data=user_data)
    return new_user

@router.get('/{user_id}/',
            response_model=dto.User)
async def get_user(
        user_id: Annotated[int, Path()],
        service: FromDishka[UserService]
):
    user = await service.get_user(user_id)
    if user is None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail='User not found')
    return user
