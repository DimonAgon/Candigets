
from .session_maker import session_maker

from functools import wraps

from typing import Callable, Any


class SessionDelivery:
    def __init__(self, session_pool): #TODO: annotate session_pool type
        self.session_pool = session_pool


    def deliver_session(self, function: Callable) -> Any:
        @wraps(function)
        async def wrap(*args, **kwargs):
            async with self.session_pool() as session:
                return await function(session=session, *args, **kwargs)

        return wrap

session_delivery = SessionDelivery(session_maker)




