from typing import Optional

from aiogram.types import (InlineKeyboardButton, InlineKeyboardMarkup,
                           KeyboardButton, ReplyKeyboardMarkup)
from aiogram.types.web_app_info import WebAppInfo
from aiogram.utils.keyboard import InlineKeyboardBuilder, ReplyKeyboardBuilder

from src.utils.text import CANCEL, DEFAULT_MESSAGE, SEND


class ButtonsBuilders:

    @staticmethod
    def inline_builder(
        buttons: list[InlineKeyboardButton], size: Optional[tuple[int]] = ()
    ) -> InlineKeyboardMarkup:
        builder = InlineKeyboardBuilder()

        builder.add(*buttons)

        keyboard = builder.adjust(*size).as_markup()
        keyboard.resize_keyboard = True
        return keyboard

    @staticmethod
    def reply_markup_builder(
        buttons: list[KeyboardButton], size: Optional[tuple[int]] = ()
    ) -> ReplyKeyboardMarkup:
        builder = ReplyKeyboardBuilder()

        builder.add(*buttons)

        keyboard = builder.adjust(*size).as_markup()
        keyboard.resize_keyboard = True
        return keyboard

    @property
    def cancel_button(self):
        return KeyboardButton(text=CANCEL)

    @property
    def cancel(self):
        return ReplyKeyboardMarkup(keyboard=[[self.cancel_button]])


class Buttons(ButtonsBuilders):

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
    def send_button(self):
        return self.reply_markup_builder([KeyboardButton(text=SEND)])

    @property
    def send_default(self):
        return self.reply_markup_builder(
            [KeyboardButton(text=DEFAULT_MESSAGE), self.cancel_button], (1, 1)
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


buttons = Buttons()
