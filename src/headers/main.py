from aiogram import Router, types
from aiogram.filters import Command, CommandStart
from aiogram.types.input_file import FSInputFile
from aiogram_tonconnect import ATCManager
from aiogram_tonconnect.tonconnect.models import ConnectWalletCallbacks

from core.settings import ADMIN_IDS, bot, config
from src.utils.buttons import buttons
from src.utils.logic import hello_windows, main_menu
from src.utils.states import UserState

main_router = Router(name=__name__)


@main_router.message(CommandStart())
@main_router.callback_query(UserState.main_menu)
async def on_start(message: types.Message, atc_manager: ATCManager):
    await hello_windows(message.from_user, atc_manager)


@main_router.callback_query(UserState.connect_wallet)
async def connect_wallet(query: types.CallbackQuery, atc_manager: ATCManager):
    callbacks = ConnectWalletCallbacks(
        before_callback=hello_windows,
        after_callback=main_menu,
    )
    await atc_manager.connect_wallet(callbacks, check_proof=True)

    await query.answer()


@main_router.message(Command("send"))
async def send_message_on_channel(message: types.Message):

    if message.from_user.id not in ADMIN_IDS:
        return

    file = FSInputFile("./media/file.png")
    await bot.send_photo(
        config.channel_username,
        file,
        caption="some text",
        reply_markup=buttons.open_bot_button,
    )
