
from aiogram_forms import dispatcher
from aiogram_forms.forms import Form, FormsManager
from aiogram_forms.forms.fields import TextField

from aiogram.types import Message

import sqlalchemy

from additions.forms.fields import VoidAcceptingField
from db.models import SearchDemand
from db.db_infrastructure.data_types import *
from sqlalchemy.ext.asyncio import AsyncSession
from misc.exceptions import *
from .forms_infrastructure.field_labels import FIELD_CHAT_MESSAGES
from .validators import *
from infrastructure.interactions import *
from infrastructure.choices import *
from constants import *
from misc.static_text.ukrainian import *
from misc.static_text.english import *

from json import dumps

from typing import List


def get_choice_number(choice: str, particular: DemandParticular=None, all_particular_choices: List[str]=None) -> int:
    choice_stripped = choice.strip()
    all_particular_choices = \
        ALL_UNPREDICTABLE_PARTICULARS_CHOICES[particular] if not all_particular_choices else all_particular_choices
    return all_particular_choices.index(choice_stripped) + 1

def get_choices_numbers(
        choices: str,
        particular: DemandParticular=None,
        all_particular_choices: List[str]=None
) -> List[int]:
    choices_inspected_split = choices.split(",")
    choices_numbers = [
        get_choice_number(choice, particular, all_particular_choices) for choice in choices_inspected_split
    ]
    return choices_numbers

def get_choice_boolean(choice: str) -> bool:
    if choice == YES_CHOICE:
        return True
    if choice == NO_CHOICE:
        return False
    raise YesOrNoChoiceException

@dispatcher.register(candidate_search_demand_form_name)
class SearchDemandForm(Form):
    for particular in DemandParticular:
        field_name = particular.name.lower()
        field_chat_message = FIELD_CHAT_MESSAGES[particular]
        if particular in INTERACTION_VARIANTS[InteractionVariant.Writable]:
            field_label = field_chat_message
            particular_data_type = DATA_TYPES[particular]
            field_validators = (validate_is_integer_string,) if particular_data_type == sqlalchemy.INTEGER else []
            field_class = VoidAcceptingField
            field_value_data = {'label': field_label}
        elif particular in INTERACTION_VARIANTS[InteractionVariant.Clickable.SELECTABLE]:
            field_choices = CHOICES[particular]
            field_label = f"{field_chat_message}\n{field_choices}"
            field_validators = (validate_is_sequence_string,ChoicesValidator(field_choices))
            field_class = VoidAcceptingField
            field_value_data = {'label': field_label, 'validators': field_validators}
        elif particular in INTERACTION_VARIANTS[InteractionVariant.Clickable.TOGGLEABLE]:
            field_choices = YES_NO_CHOICES
            field_label = f"{field_chat_message}\n{YES_NO_CHOICES}"
            field_validators = (validate_is_single_word, ChoicesValidator(YES_NO_CHOICES))
            field_class = VoidAcceptingField
            field_value_data = {'label': field_label, 'validators': field_validators}
        locals()[field_name] = field_class(**field_value_data)


    @classmethod
    async def callback(cls, message: Message, forms: FormsManager, session: AsyncSession, *args, **kwargs) -> None:
        user_id = message.from_user.id
        form_data = await forms.get_data(candidate_search_demand_form_name)
        new_search_demand_attributes = dict(())
        new_search_demand_attributes[user_id_attribute_name] = user_id
        new_search_demand_attributes[collect_kw] = False
        new_search_demand_attributes[transmit_kw] = False
        for field_name, field_data in form_data.items():
            if not field_data == VOID_SYMBOL:
                particular = \
                    next((particular for particular in DemandParticular if particular.name.lower() == field_name), None)
                if particular in INTERACTION_VARIANTS[InteractionVariant.Clickable.SELECTABLE]:
                    if particular in INTERACTION_VARIANTS[InteractionVariant.Clickable.Extension.PREDICTABLE]:
                        all_particular_choices = CHOICES[particular]
                        field_data_choices_numbers = \
                            get_choices_numbers(choices=field_data, all_particular_choices=all_particular_choices)
                    else:
                        field_data_choices_numbers = get_choices_numbers(choices=field_data, particular=particular)
                    field_data_choices_numbers_json = dumps(field_data_choices_numbers)
                    new_search_demand_attributes[field_name] = field_data_choices_numbers_json
                elif particular in INTERACTION_VARIANTS[InteractionVariant.Clickable.TOGGLEABLE]:
                    field_data_boolean = get_choice_boolean(field_data)
                    new_search_demand_attributes[field_name] = field_data_boolean
                else:
                    new_search_demand_attributes[field_name] = field_data

        new_search_demand = SearchDemand(**new_search_demand_attributes)
        await session.merge(new_search_demand)
        await session.commit()
        await message.answer(search_demand_registration_success_chat_message)
