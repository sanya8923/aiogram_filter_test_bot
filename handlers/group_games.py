from aiogram import Router
from aiogram.enums.dice_emoji import DiceEmoji
from aiogram.types.message import Message
from aiogram.filters.command import Command

from filters.chat_type import ChatTypeFilter


router = Router()


@router.message(ChatTypeFilter(chat_type=['group', 'supergroup']), commands='Dice')
async def cmd_dice_in_group(message: Message):
    await message.answer_dice(emoji=DiceEmoji.DICE)

