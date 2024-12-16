
import sqlalchemy
from sqlalchemy.ext.asyncio import AsyncSession

from types_ import *
from ..bot import bot
from db.session_delivery import session_delivery
from infrastructure.enums import *
from db.utils import *
from misc.static_text.english import *

import json

from typing import List


def prepare_ad_fields_data(ad: CandidateAd) -> List[ParticularFieldData]:
    ad_fields_data = get_db_object_fields_data(ad)
    del ad_fields_data[id_kw]
    del ad_fields_data[external_id_field_name]
    del ad_fields_data[search_demand_id_field_name]
    fields = [
        ParticularFieldData(
            next((particular for particular in AdParticular if particular.name.lower() == field_name), None),
            field_value
        )
        for field_name, field_value in ad_fields_data.items()
    ]
    fields.sort(key=lambda field: field.particular.value)
    return fields

def create_ad_text(ad: CandidateAd) -> str:
    ad_fields_data = prepare_ad_fields_data(ad)
    message_text = ""
    for field in ad_fields_data:
        if field.value:
            if isinstance(field.value, str):
                try:
                    field_value_deserialized = json.loads(field.value)
                    message_text = f"{message_text}\n{field_value_deserialized}"
                except json.JSONDecodeError:
                    message_text = f"{message_text}\n{field.value}"
            else:
                message_text = f"{message_text}\n{field.value}"
    return message_text

async def transmit_ad_handler(ad: CandidateAd, user_id) -> None:
    message_text = create_ad_text(ad)
    await bot.send_message(user_id, message_text)

@session_delivery.deliver_session
async def transmit_ads_handler(demand: SearchDemand, session: AsyncSession) -> None:
    all_demand_candidates_ads_query = sqlalchemy.select(CandidateAd).where(CandidateAd.search_demand==demand)
    all_demand_candidates_ads = await session.scalars(all_demand_candidates_ads_query)
    for ad in all_demand_candidates_ads:
        await transmit_ad_handler(ad, demand.user_id)