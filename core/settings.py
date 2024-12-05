from aiogram import Bot, Dispatcher
from aiogram.client.default import DefaultBotProperties
from aiogram.enums import ParseMode
from aiogram.fsm.storage.redis import RedisStorage
from pydantic_settings import BaseSettings, SettingsConfigDict


class Config(BaseSettings):
    model_config = SettingsConfigDict(env_file=".env")
    bot_token: str
    channel_username: str
    manifest_url: str


ADMIN_IDS = [391103075]


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

storage = RedisStorage.from_url("redis://redis")

bot = Bot(
    token=config.bot_token, default=DefaultBotProperties(parse_mode=ParseMode.HTML)
)

dp = Dispatcher(storage=storage)
