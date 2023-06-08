import logging
import asyncio

from aiogram import Bot, Dispatcher


async def main():
    logging.basicConfig(level=logging.INFO)


if __name__ == '__main__':
    asyncio.run(main())