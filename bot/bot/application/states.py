from aiogram.fsm.state import StatesGroup, State

class StartMenuSG(StatesGroup):
    menu = State()
    help = State()

class CreateSourceSG(StatesGroup):
    create = State()

class NewsSG(StatesGroup):
    list_news = State()
    current = State()