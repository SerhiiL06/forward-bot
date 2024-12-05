import asyncio

from aiogram_tonconnect.handlers import AiogramTonConnectHandlers
from aiogram_tonconnect.middleware import AiogramTonConnectMiddleware
from aiogram_tonconnect.tonconnect.storage.base import ATCRedisStorage

from core.settings import EXCLUDE_WALLETS, bot, config, dp, storage
from src.headers.main import main_router


async def application():

    dp.update.middleware.register(
        AiogramTonConnectMiddleware(
            storage=ATCRedisStorage(storage.redis),
            manifest_url=config.manifest_url,
            exclude_wallets=EXCLUDE_WALLETS,
        )
    )
    AiogramTonConnectHandlers().register(dp)
    dp.include_router(main_router)
    await dp.start_polling(bot)


if __name__ == "__main__":
    asyncio.run(application())
