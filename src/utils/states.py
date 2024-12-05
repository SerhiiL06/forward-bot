from aiogram.fsm.state import StatesGroup, State


class UserState(StatesGroup):
    connect_wallet = State()
    main_menu = State()
