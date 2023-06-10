from typing import Union

from aiogram.filters import BaseFilter, Filter
from aiogram.types import Message


class ChatTypeFilter(BaseFilter):
    def __init__(self, chat_type: Union[str, list]):
        self.chat_type = chat_type

    async def __call__(self, message: Message) -> bool:

        if isinstance(self.chat_type, str):
            return message.chat.type == self.chat_type
        else:
            return message.chat.type in self.chat_type


# class ChatTypeFilter2(Filter):
#     def __init__(self, is_group: Bool):
#         self.is_group = is_group
#
#     async def __call__(self, message: Message) -> bool:
#         if message.chat.type == 'group':
#             return True
#         elif message.chat.type == 'supergroup':
#             return True
#         else

