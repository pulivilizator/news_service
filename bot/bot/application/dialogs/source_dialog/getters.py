from typing import TYPE_CHECKING

from aiogram_dialog import DialogManager
from fluentogram import TranslatorRunner

if TYPE_CHECKING:
    from bot.locales.stub import TranslatorRunner

async def create_source_getter(dialog_manager: DialogManager,
                               i18n: TranslatorRunner,
                               **kwargs) -> dict[str, tuple | str]:
    return {
        'create_source_message': i18n.source.create.message(),
        'back': i18n.back.button()
    }