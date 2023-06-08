from aiogram import Router
from aiogram.enums.dice_emoji import DiceEmoji
from aiogram.types.message import Message
from aiogram.filters.command import Command

from filters.chat_type import ChatTypeFilter


router = Router()


# @router.message(ChatTypeFilter(chat_type=['group', 'supergroup']),
#                 Command(commands=['dice']))
# async def cmd_dice_in_group(message: Message):
#     await message.answer_dice(emoji=DiceEmoji.DICE)
#
#
# @router.message(ChatTypeFilter(chat_type=['group', 'supergroup']),
#                 Command(commands=['basketball']))
# async def cmd_basketball_in_group(message: Message):
#     await message.answer_dice(emoji=DiceEmoji.BASKETBALL)
#
#
router.message.filter(ChatTypeFilter(chat_type=['group', 'supergroup']))


@router.message(Command('dice'))
async def cmd_dice_in_group(message: Message):
    await message.answer_dice(emoji=DiceEmoji.DICE)


@router.message(Command('basketball'))
async def cmd_basketball_in_group(message: Message):
    await message.answer_dice(emoji=DiceEmoji.BASKETBALL)


