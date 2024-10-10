from aiogram_dialog import Dialog, Window
from aiogram_dialog.widgets.kbd import Row, Radio, Start, Next, Back
from aiogram_dialog.widgets.text import Format

from core.enums import Language, NewsForTime
from .getters import get_langs, start_menu_getter
from application.states import StartMenuSG, CreateSourceSG, NewsSG
from .handlers import change_lang_handler
from application.utils.button_checker import SetButtonChecked

dialog = Dialog(
    Window(
        Format('{menu_start_message}'),
        Start(text=Format('{create_source_button}'), state=CreateSourceSG.create, id='add_source'),

        Start(text=Format('{get_new_for_hour_button}'),
              id='get_new_for_hour',
              state=NewsSG.list_news,
              data={'time': NewsForTime.HOUR}),

        Start(text=Format('{get_new_for_day_button}'),
              id='get_new_for_day',
              state=NewsSG.list_news,
              data={'time': NewsForTime.DAY}),
        Next(Format('{help_button}')),
        Row(
            Radio(
                checked_text=Format('🔘 {item[1]}'),
                unchecked_text=Format('⚪️ {item[1]}'),
                id=Language.WIDGET_KEY,
                item_id_getter=lambda x: x[0],
                on_state_changed=change_lang_handler,
                items='languages',
            ),
        ),
        getter=get_langs,
        state=StartMenuSG.menu,
    ),
    Window(
        Format('{help_message}'),
        Back(Format('{back}')),
        state=StartMenuSG.help,
    ),
    on_start=SetButtonChecked(Language),
    getter=start_menu_getter
)