
import asyncio

import sqlalchemy
from sqlalchemy.ext.asyncio import AsyncSession

from db.session_delivery import session_delivery
from db.models import *

import os


class AdDeletor:

    @classmethod
    @session_delivery.deliver_session
    async def delete_depleted_demands_and_ads(cls, session: AsyncSession):
        depleted_demands_query = (
            sqlalchemy.select(SearchDemand).
            where(SearchDemand.collect == True).
            where(SearchDemand.transmit == True)
        )
        depleted_demands = await session.scalars(depleted_demands_query)
        for demand in depleted_demands:
            delete_all_demand_ads_query = sqlalchemy.delete(CandidateAd).where(CandidateAd.search_demand == demand)
            await session.execute(delete_all_demand_ads_query)
            await session.delete(demand)
        await session.commit()