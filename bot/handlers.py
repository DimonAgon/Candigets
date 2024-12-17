
from aiogram.filters import Command, CommandStart
from aiogram.types import Message
from aiogram import F
from aiogram.fsm.context import FSMContext

from aiogram_forms import FormsManager

import sqlalchemy
from sqlalchemy.ext.asyncio import AsyncSession

from .dispatcher import dispatcher
from .filters import *
from db.models import *
from misc.static_text.ukrainian import bot_instruction_text

from misc.static_text.english import *


@dispatcher.message(CommandStart())
async def start_command(message: Message):
    await message.answer(bot_instruction_text)


demand_command_filters_config = (
    Command(commands=[demand_kw, 'dem', 'd']),
    NoUserDemandFilter()
)
@dispatcher.message(*demand_command_filters_config, F.chat.type.in_({'private'}))
@dispatcher.message(*demand_command_filters_config, F.chat.type.in_({'group', 'supergroup'}), IsAdminFilter())
async def demand_command(message: Message, forms: FormsManager) -> None:
    await forms.show(candidate_search_demand_form_name)


@dispatcher.message(Command(commands='clear_demand'), UserDemandExistsFilter())
async def clear_demand_command(message: Message, session: AsyncSession) -> None:
    user_id = message.from_user.id
    demand_deletion_query = sqlalchemy.delete(SearchDemand).where(SearchDemand.user_id == user_id)
    try:
        all_demand_ads_deletion_query = \
            sqlalchemy.delete(CandidateAd).where(CandidateAd.search_demand.user_id == user_id)
        await session.execute(all_demand_ads_deletion_query)
    except AttributeError:
        pass
    await session.execute(demand_deletion_query)
    await session.commit()
    await message.answer(search_demand_on_deletion_success_chat_message)


@dispatcher.message(Command(commands='cancel'))
async def cancel(message: Message, state: FSMContext) -> None:
    await state.clear()
    await message.answer(on_cancelling_chat_message)
