
from .enums import *
from .enums import DemandParticular

INTERACTION_VARIANTS = {
    InteractionVariant.Writable: {
        DemandParticular.JOB_TITLE,
        DemandParticular.SKILLS,
        DemandParticular.AGE_MINIMUM,
        DemandParticular.AGE_MAXIMUM,
        DemandParticular.SALARY_MINIMUM,
        DemandParticular.SALARY_MAXIMUM,
    },
    InteractionVariant.Writable.Extension.SEARCHABLE: {
        DemandParticular.JOB_TITLE,
        DemandParticular.SKILLS
    },
    InteractionVariant.Clickable:{
        DemandParticular.PHOTO_REQUIREMENT,
        DemandParticular.GENDER,
        DemandParticular.SALARY_STATEMENT_REQUIREMENT,
        DemandParticular.RUBRICS,
        DemandParticular.YEARS_OF_EXPERIENCE,
        DemandParticular.STUDENTSHIP_REQUIREMENT,
        DemandParticular.LANGUAGES,
        DemandParticular.EMPLOYMENT_TYPES,
        DemandParticular.FIELDS,
        DemandParticular.EDUCATIONS,
        DemandParticular.CURRICULUM_VITAE
    },
    InteractionVariant.Clickable.SELECTABLE: {
        DemandParticular.GENDER,
        DemandParticular.RUBRICS,
        DemandParticular.YEARS_OF_EXPERIENCE,
        DemandParticular.LANGUAGES,
        DemandParticular.EMPLOYMENT_TYPES,
        DemandParticular.FIELDS,
        DemandParticular.EDUCATIONS,
        DemandParticular.CURRICULUM_VITAE
    },
    InteractionVariant.Clickable.Extension.MULTICHOICE: {
        DemandParticular.RUBRICS,
        DemandParticular.YEARS_OF_EXPERIENCE,
        DemandParticular.LANGUAGES,
        DemandParticular.EMPLOYMENT_TYPES,
        DemandParticular.FIELDS,
        DemandParticular.EDUCATIONS,
        DemandParticular.CURRICULUM_VITAE
    },
    InteractionVariant.Clickable.Extension.PREDICTABLE: {
        DemandParticular.GENDER
    },
    InteractionVariant.Clickable.TOGGLEABLE: {
        DemandParticular.PHOTO_REQUIREMENT,
        DemandParticular.SALARY_STATEMENT_REQUIREMENT,
        DemandParticular.STUDENTSHIP_REQUIREMENT,
    },
}