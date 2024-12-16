
from aiogram.filters import BaseFilter
from aiogram import types

from .bot import bot
from .checkers import check_user_demand_exists
from .checkers import *
from db.models import *
from misc.static_text.english import *
from misc.static_text.ukrainian import *


class IsAdminFilter(BaseFilter):
    required_auth_level = administrator_kw
    creator = creator_kw
    async def __call__(self, message: types.Message) -> bool:
        chat_id = message.chat.id
        user_id = message.from_user.id
        member = await bot.get_chat_member(chat_id, user_id)
        is_admin = member.status == self.required_auth_level or member.status == self.creator
        if is_admin:
            return True
        else:
            await message.answer(is_administrator_check_fail_chat_message)
            return False


class NoUserDemandFilter(BaseFilter):
    async def __call__(self, message: types.Message, session: AsyncSession) -> bool:
        user_id = message.from_user.id
        user_search_demand_exists = await check_user_demand_exists(user_id)
        if not user_search_demand_exists:
            return True
        else:
            await message.answer(no_user_demand_check_fail_chat_message)
            return False


class UserDemandExistsFilter(BaseFilter):
    async def __call__(self, message: types.Message, session: AsyncSession) -> bool:
        user_id = message.from_user.id
        user_search_demand_exists = await check_user_demand_exists(user_id)
        if user_search_demand_exists:
            return True
        else:
            await message.answer(user_demand_exists_check_fail_chat_message)
            return False

