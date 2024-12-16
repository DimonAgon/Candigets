
from aiogram_forms.forms.base import Field

from constants import *

from typing import Any


class VoidAcceptingField(Field):

    async def validate(self, value: Any) -> None:
        if value == VOID_SYMBOL: pass
        else:
            await Field.validate(self, value)