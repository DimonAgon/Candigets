
from aiogram_forms.errors import ValidationError

from misc.static_text.ukrainian import *
from misc.re_patterns import *

import re

from typing import List


def validate_is_integer_string(value: str) -> None:
    try:
        int(value)
    except TypeError:
        raise ValidationError(is_integer_string_check_fail_chat_message, code='type')


def validate_is_sequence_string(value: str) -> None:
    if not sequence_string_repattern.fullmatch(value):
        raise ValidationError(is_sequence_string_check_fail_chat_message, code='regex')


def validate_is_single_word(value: str):
    if not single_word_repattern.fullmatch(value):
        raise ValidationError(is_single_word_check_fail_chat_message, code='regex')


class ChoicesValidator:
    def __init__(self, choices: List[str]) -> None:
        self.choices = choices

    def __call__(self, value: str) -> None:
        value_copy = value
        for choice in self.choices:
            if re.search(choice, value):
                value_copy = value_copy.replace(choice, "")
        if not emptied_sequence_string_repattern.fullmatch(value_copy):
            raise ValidationError(is_choice_check_fail_chat_message, code='regex')
