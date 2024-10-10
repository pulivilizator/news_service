from aiogram.enums import ContentType
from aiogram_dialog import Dialog, Window
from aiogram_dialog.widgets.input import TextInput, MessageInput
from aiogram_dialog.widgets.kbd import Cancel
from aiogram_dialog.widgets.text import Format

from .filters import rss_link_filter
from .getters import create_source_getter
from .handlers import incorrect_input, create_source
from application.states import CreateSourceSG

dialog = Dialog(
    Window(
        Format('{create_source_message}'),
        TextInput(
            type_factory=rss_link_filter,
            on_success=create_source,
            on_error=incorrect_input,
            id='create_source'
        ),
        MessageInput(
            content_types=ContentType.ANY,
            func=incorrect_input,
        ),
        Cancel(Format('{back}')),
        state=CreateSourceSG.create,
        getter=create_source_getter
    )
)