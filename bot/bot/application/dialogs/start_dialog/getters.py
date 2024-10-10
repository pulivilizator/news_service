from typing import TYPE_CHECKING

from aiogram_dialog import DialogManager
from dishka.integrations.aiogram_dialog import inject
from dishka import FromDishka
from fluentogram import TranslatorRunner

from core.enums import Language

if TYPE_CHECKING:
    from bot.locales.stub import TranslatorRunner

async def start_menu_getter(dialog_manager: DialogManager,
                           i18n: TranslatorRunner,
                           **kwargs) -> dict[str, tuple | str]:
    return {
        'menu_start_message': i18n.menu.start_message(),
        'create_source_button': i18n.menu.create_source.button(),
        'get_new_for_hour_button': i18n.menu.news_for_hour.button(),
        'get_new_for_day_button': i18n.menu.news_for_day.button(),
        'back': i18n.back.button(),
        'help_button': i18n.menu.help.button(),
        'help_message': i18n.menu.help.message(),

    }

async def get_langs(dialog_manager: DialogManager,
                    i18n: TranslatorRunner,
                    **kwargs) -> dict[str, tuple | str]:
    return {
        'languages': (
            (Language.RU, i18n.lang.ru()),
            (Language.EN, i18n.lang.en())
        )
    }