
import asyncio

from .bot import bot
from .dispatcher import dispatcher
from .middleware import *

def set_all_middleware():
    dispatcher.update.middleware(DBSessionDeliveryMiddleware())


async def main():
    set_all_middleware()
    await dispatcher.start_polling(bot)