from aiogram_dialog import Dialog, Window
from aiogram_dialog.widgets.kbd import ScrollingGroup, ListGroup, Cancel, SwitchTo, Back
from aiogram_dialog.widgets.text import Format

from application.dialogs.news_dialog.getters import news_getter, current_news_getter
from application.states import NewsSG
from application.utils.kbd import get_scroll_buttons

dialog = Dialog(
    Window(
        Format('{news_message}'),
        ScrollingGroup(
            ListGroup(SwitchTo(text=Format('{item[0]}'), id='new', state=NewsSG.current),
                      items='news',
                      id='news_list',
                      item_id_getter=lambda x: x[1]),
            id='news',
            height=5,
            hide_pager=True
        ),
        get_scroll_buttons('news'),
        Cancel(text=Format('{back}')),
        getter=news_getter,
        state=NewsSG.list_news
    ),
    Window(
        Format('{news_current_message}'),
        Back(text=Format('{back}')),
        getter=current_news_getter,
        state=NewsSG.current
    )
)