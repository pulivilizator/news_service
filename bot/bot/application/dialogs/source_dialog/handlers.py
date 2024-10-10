from typing import TYPE_CHECKING

from aiogram.types import Message
from aiogram_dialog import DialogManager
from aiogram_dialog.widgets.input import MessageInput, ManagedTextInput
from dishka import FromDishka
from dishka.integrations.aiogram_dialog import inject
from fluentogram import TranslatorRunner

from core import dto
from core.enums import ApiUrls
from services.source_service import SourceService

if TYPE_CHECKING:
    from locales.stub import TranslatorRunner

@inject
async def create_source(
        message: Message,
        widget: ManagedTextInput,
        dialog_manager: DialogManager,
        text: str,
        service: FromDishka[SourceService]
):
    i18n: TranslatorRunner = dialog_manager.middleware_data.get('i18n')
    await message.answer(text=i18n.source.save_answer.message())
    await service.create(path=ApiUrls.SOURCE,
                         data=dto.CreateSource(user_id=message.from_user.id,
                                               url=text))

async def incorrect_input(
        message: Message,
        widget: MessageInput,
        dialog_manager: DialogManager,
        error: str | None = None
):
    i18n: TranslatorRunner = dialog_manager.middleware_data.get('i18n')
    await message.answer(i18n.incorrect_message())