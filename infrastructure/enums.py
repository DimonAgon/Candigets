
from enum import Enum, auto
from aenum import Enum as AEnum


class Particular(Enum):...

class DemandParticular(Particular):
    JOB_TITLE = auto()
    SKILLS = auto()
    PHOTO_REQUIREMENT = auto()
    AGE_MINIMUM = auto()
    AGE_MAXIMUM = auto()
    GENDER = auto()
    SALARY_MINIMUM = auto()
    SALARY_MAXIMUM = auto()
    SALARY_STATEMENT_REQUIREMENT = auto()
    RUBRICS = auto()
    YEARS_OF_EXPERIENCE = auto()
    STUDENTSHIP_REQUIREMENT = auto()
    LANGUAGES = auto()
    EMPLOYMENT_TYPES = auto()
    FIELDS = auto()
    EDUCATIONS = auto()
    CURRICULUM_VITAE = auto()

class AdParticular(Enum):
    SOURCE = auto()
    PROFESSION = auto()
    NAME = auto()
    LOCATION = auto()
    AGE = auto()
    SALARY = auto()
    JOBS_EXPERIENCES = auto()
    CV_FULLNESS = auto()
    UPDATE = auto()
    CONNECTION_STATUS = auto()
    PICTURE = auto()


class ReadingVariant(AEnum):

    class Text(AEnum):
        UNARY_TEXT = auto()
        PARALLEL_TEXT = auto()

    class Path(AEnum):
        HYPER_REFERENCE = auto()
        SOURCE = auto()


class InteractionVariant(AEnum):

    class Writable(AEnum):

        class Extension(AEnum):
            SEARCHABLE = auto()

    class Clickable(AEnum):
        SELECTABLE = auto()
        TOGGLEABLE = auto()

        class Extension(AEnum):
            MULTICHOICE = auto()
            PREDICTABLE = auto()