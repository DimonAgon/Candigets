
from aiogram import BaseMiddleware

from db.session_delivery import session_delivery

from typing import Callable, Awaitable, Any, Dict
from sqlalchemy.ext.asyncio import AsyncSession

from aiogram.types import TelegramObject


class DBSessionDeliveryMiddleware(BaseMiddleware):

    @session_delivery.deliver_session
    async def __call__(
            self,
            handler: Callable[[TelegramObject, Dict[str, Any]], Awaitable[Any]],
            event: TelegramObject,
            data: Dict[str, Any],
            session: AsyncSession,
    ) -> Any:
        data['session'] = session
        return await handler(event, data)

