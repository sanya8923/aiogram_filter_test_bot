import logging
import asyncio

import config

import config_reader
from aiogram import Bot, Dispatcher


async def main():
    logging.basicConfig(level=logging.INFO)
    bot = Bot(token=config_reader.config.bot_token.get_secret_value())

if __name__ == '__main__':
    asyncio.run(main())