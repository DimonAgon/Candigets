
from typing import Any, Iterable


def is_in_by_attribute_or_none(searched: Any, in_what: Iterable, attribute: str) -> bool:
    return bool(next((in_one for in_one in in_what if searched == in_one.__getattribute__(attribute)), None))