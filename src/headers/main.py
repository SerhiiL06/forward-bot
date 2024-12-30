from logging import Logger

from aiogram import F, Router, types
from aiogram.exceptions import TelegramBadRequest
from aiogram.filters import Command, CommandStart
from aiogram.fsm.context import FSMContext
from aiogram_tonconnect import ATCManager
from aiogram_tonconnect.tonconnect.models import ConnectWalletCallbacks

from core.settings import ADMIN_IDS, bot
from src.utils.buttons import buttons
from src.utils.logic import hello_windows, main_menu, send_default_message
from src.utils.states import UserState
from src.utils.text import CANCEL, DEFAULT_MESSAGE, SEND

main_router = Router(name=__name__)


logger = Logger(name="main")


@main_router.message(CommandStart())
@main_router.callback_query(UserState.main_menu)
async def on_start(message: types.Message, atc_manager: ATCManager):
    await hello_windows(message.from_user, atc_manager)


@main_router.message(F.text == CANCEL)
async def cancel_action(message: types.Message, state: FSMContext):

    await message.answer("Action was canceled", reply_markup=buttons.send_button)
    await state.clear()


@main_router.callback_query(UserState.connect_wallet)
async def connect_wallet(query: types.CallbackQuery, atc_manager: ATCManager):
    callbacks = ConnectWalletCallbacks(
        before_callback=hello_windows,
        after_callback=main_menu,
    )
    await atc_manager.connect_wallet(callbacks, check_proof=True)
    await query.answer()


@main_router.message(Command("send"))
@main_router.message(F.text == SEND)
async def choose_channel_for_post(message: types.Message, state: FSMContext):

    if message.from_user.id not in ADMIN_IDS:
        return

    await message.answer("Enter the chat id channel", reply_markup=buttons.cancel)

    await state.set_state(UserState.chat_id.state)


@main_router.message(UserState.chat_id)
async def send_message_to_channel(message: types.Message, state: FSMContext):

    await state.update_data({"id": message.text})

    await message.answer("send message for post", reply_markup=buttons.send_default)

    await state.set_state(UserState.message.state)


@main_router.message(UserState.message)
async def send_message_to_channel(message: types.Message, state: FSMContext):
    try:

        data = await state.get_data()
        destination_chat_id = data.get("id")

        if message.text == DEFAULT_MESSAGE:
            await send_default_message(bot, destination_chat_id)
            await state.clear()
            await message.answer(
                "Defaut message was sent", reply_markup=buttons.send_button
            )
            return

        await bot.copy_message(
            f"-100{destination_chat_id}", message.chat.id, message.message_id
        )
        await state.clear()

    except TelegramBadRequest as e:
        await message.answer("Check the username of channel")
        logger.error(e)
        await state.set_state(UserState.chat_id.state)
        return

    await message.answer("Message was sent", reply_markup=buttons.send_button)
