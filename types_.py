
from infrastructure.enums import *

from dataclasses import dataclass

from typing import List, Any


class CandidateAdData:
    def __init__(
            self,
            external_id: str=None,
            source: str=None,
            profession: str=None,
            name: str=None,
            location: str=None,
            age: str=None,
            salary: str=None,
            jobs_experiences: list[List[str]]=(),
            cv_fullness: str=None,
            update: str=None,
            connection_status: str=None,
            picture: str = None,
    ):
        self.external_id = external_id
        self.source = source
        self.profession = profession
        self.name = name
        self.location = location
        self.age = age
        self.salary = salary
        self.jobs_experiences = jobs_experiences
        self.cv_fullness = cv_fullness
        self.update = update
        self.connection_status = connection_status
        self.picture = picture


@dataclass
class ParticularFieldData:
    particular: Particular
    value: Any