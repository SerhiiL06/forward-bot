from typing import Optional

from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup
from aiogram.utils.keyboard import InlineKeyboardBuilder
from aiogram.types.web_app_info import WebAppInfo


class Buttons:

    @property
    def open_bot_button(self):
        return self.inline_builder(
            [
                InlineKeyboardButton(
                    text="Click button",
                    url="https://t.me/test_hamster_key_bot?start=start",
                )
            ]
        )

    @property
    def start_button(self):
        return self.inline_builder(
            [
                InlineKeyboardButton(
                    text="Open website",
                    web_app=WebAppInfo(url="https://pump.fun"),
                ),
                InlineKeyboardButton(
                    text="connect wallet",
                    callback_data="connect",
                ),
            ],
            (1,),
        )

    @staticmethod
    def inline_builder(
        buttons: list[InlineKeyboardButton], size: Optional[tuple[int]] = ()
    ) -> InlineKeyboardMarkup:
        builder = InlineKeyboardBuilder()

        builder.add(*buttons)

        keyboard = builder.adjust(*size).as_markup()
        keyboard.resize_keyboard = True
        return keyboard


buttons = Buttons()
