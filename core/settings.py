from aiogram import Bot, Dispatcher
from pydantic_settings import BaseSettings, SettingsConfigDict
from aiogram.fsm.storage.redis import RedisStorage
from aiogram.client.default import DefaultBotProperties
from aiogram.enums import ParseMode


class Config(BaseSettings):
    model_config = SettingsConfigDict(env_file=".env")
    bot_token: str
    channel_username: str
    manifest_url: str


ADMIN_IDS = [391103075, 7101814585]


EXCLUDE_WALLETS = [
    "tonkeeper",
    "mytonwallet",
    "bitgetTonWallet",
    "binanceWeb3TonWallet",
    "fintopio-tg",
    "dewallet",
    "safepalwallet",
    "tonhub",
    "okxTonWallet",
    "okxMiniWallet",
    "hot",
    "bybitTonWallet",
    "GateWallet",
    "BitgetWeb3",
    "tobi",
]

config = Config()

storage = RedisStorage.from_url("redis://localhost:6379")

bot = Bot(
    token=config.bot_token, default=DefaultBotProperties(parse_mode=ParseMode.HTML)
)

dp = Dispatcher(storage=storage)
