from aiogram.types import User
from aiogram.types.input_file import FSInputFile
from aiogram_tonconnect import ATCManager
from aiogram_tonconnect.tonconnect.models import AccountWallet, AppWallet

from src.utils.buttons import buttons
from src.utils.states import UserState
from src.utils.text import IMAGE_PATH, START_MESSAGE


async def hello_windows(event_from_user: User, atc_manager: ATCManager, **kwargs):
    caption = START_MESSAGE

    file = FSInputFile(IMAGE_PATH)
    await atc_manager._send_photo(file, caption, reply_markup=buttons.start_button)
    await atc_manager.state.set_state(UserState.connect_wallet.state)


async def main_menu(
    atc_manager: ATCManager, app_wallet: AppWallet, account_wallet: AccountWallet, **_
):

    caption = START_MESSAGE
    file = FSInputFile(IMAGE_PATH)
    await atc_manager._send_photo(file, caption, reply_markup=buttons.start_button)
    await atc_manager.state.set_state(UserState.main_menu.state)
