
from aiogram import Dispatcher, Router

from aiogram_forms import dispatcher as forms_dispatcher


dispatcher = Dispatcher()
demands_router = Router()
dispatcher.include_router(demands_router)
forms_dispatcher.attach(dispatcher)