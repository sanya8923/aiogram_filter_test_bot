from typing import List

from aiogram import Router, F
from aiogram.types import Message

from filter.find_username import HasUsernamesFilter


router = Router()


@router.message(F.text, HasUsernamesFilter())
async def message_with_username(message: Message, usernames: List[str]):
    await message.reply(f"Thanks for link {', '.join(usernames)}")

