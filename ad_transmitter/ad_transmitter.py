
import asyncio

import sqlalchemy
from sqlalchemy.ext.asyncio import AsyncSession

from db.session_delivery import session_delivery
from db.models import *
from bot.ad_transmitter.handlers import *

import os


class AdTransmitter:

    @classmethod
    @session_delivery.deliver_session
    async def trasmit_ads(cls, session: AsyncSession) -> None:
        all_demands_to_transmit_query = (
            sqlalchemy.select(SearchDemand)
            .where(SearchDemand.transmit == False)
            .where(SearchDemand.collect == True)
        )
        all_demands_to_transmit = await session.scalars(all_demands_to_transmit_query)
        for demand in all_demands_to_transmit:
            await transmit_ads_handler(demand)
            demand.transmit = True
            await session.merge(demand)
        await session.commit()


