
from db.models import *

from copy import deepcopy

from typing import Dict, Any


def get_db_object_fields_data(object_: Base) -> Dict[str, Any]: #TODO: reannotate object class
    object_copy = deepcopy(object_)
    object_copy_attributes = vars(object_copy); del object_copy_attributes['_sa_instance_state'] #TODO: consider using keys()
    return object_copy_attributes
