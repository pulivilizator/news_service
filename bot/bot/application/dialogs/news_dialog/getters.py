from typing import TYPE_CHECKING

from aiogram_dialog import DialogManager
from dishka.integrations.aiogram_dialog import inject
from dishka import FromDishka
from fluentogram import TranslatorRunner
from aiogram import html
from core import dto
from core.enums import NewsForTime
from services.news_service import NewsService

if TYPE_CHECKING:
    from bot.locales.stub import TranslatorRunner

@inject
async def news_getter(dialog_manager: DialogManager,
                      i18n: TranslatorRunner,
                      service: FromDishka[NewsService],
                      **kwargs) -> dict[str, tuple | str]:
    user_id = dialog_manager.event.from_user.id
    time = dialog_manager.start_data.get('time') or NewsForTime.DAY
    news_models = await service.get_news_for_time(time=time, user_id=user_id)
    news_dict = {i: model.model_dump_json() for i, model in enumerate(news_models)}
    dialog_manager.dialog_data.update({'news': news_dict})
    news = [
        (f'{model.title[:35]}...', i)
        for i, model in enumerate(news_models)
    ]

    return {
        'news_message': i18n.news.message(),
        'news': news,
        'back': i18n.back.button(),
        'single_page': len(news) > 5
    }

@inject
async def current_news_getter(dialog_manager: DialogManager,
                              i18n: TranslatorRunner,
                              service: FromDishka[NewsService],
                              **kwargs) -> dict[str, tuple | str]:
    current_news_id = dialog_manager.event.data.split(':')[1]
    current_new = dto.NewsItem.model_validate_json(dialog_manager.dialog_data.get('news')[current_news_id])
    if current_new.category is None and current_new.description is None:
        message = i18n.news.current.minimal(
            title=current_new.title,
            link=current_new.link,
            published_at=current_new.pub_date.strftime('%d.%m.%Y %H:%M')
        )
    elif current_new.category is None and current_new.description:
        message = i18n.news.current.without_category(
            title=current_new.title,
            description=current_new.description,
            link=current_new.link,
            published_at=current_new.pub_date.strftime('%d.%m.%Y %H:%M')
        )
    elif current_new.description is None and current_new.category:
        message = i18n.news.current.without_description(
            title=current_new.title,
            category=current_new.category,
            link=current_new.link,
            published_at=current_new.pub_date.strftime('%d.%m.%Y %H:%M')
        )
    else:
        message = i18n.news.current.full(
            title=current_new.title,
            description=current_new.description,
            category=current_new.category,
            link=current_new.link,
            published_at=current_new.pub_date.strftime('%d.%m.%Y %H:%M')
        )
    return {
        'news_current_message': message,
        'back': i18n.back.button()
    }
