from typing import Union, Dict, Any

from aiogram.filters import BaseFilter
from aiogram.types import Message
from test_func import TestFuncs


class HasUsernamesFilter(BaseFilter):
    async def __call__(self, message: Message) -> Union[bool, Dict[str, Any]]:
        entities = message.entities or []

        found_usernames = [
            item.extract_from(message.text) for item in entities
            if item.type == "mention"
        ]
        print(f'found_usernames: {found_usernames}')

        if len(found_usernames) > 0:
            return {"usernames": found_usernames}
        return False
