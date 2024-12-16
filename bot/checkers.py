
from sqlalchemy.ext.asyncio import AsyncSession
import sqlalchemy

from db.session_delivery import session_delivery
from db.models import *


@session_delivery.deliver_session
async def check_user_demand_exists(user_id: int, session: AsyncSession) -> bool:
    user_search_demand_query = sqlalchemy.select(SearchDemand).where(SearchDemand.user_id == user_id)
    user_search_demand = (await session.execute(user_search_demand_query)).first()
    return bool(user_search_demand)