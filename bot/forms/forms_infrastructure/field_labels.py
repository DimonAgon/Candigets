
from infrastructure.enums import *
from misc.static_text.ukrainian import *


FIELD_CHAT_MESSAGES = {
    DemandParticular.JOB_TITLE: job_title_field_chat_message,
    DemandParticular.SKILLS: skills_field_chat_message,
    DemandParticular.PHOTO_REQUIREMENT: photo_requirement_field_chat_message,
    DemandParticular.AGE_MINIMUM: age_minimum_field_chat_message,
    DemandParticular.AGE_MAXIMUM: age_maximum_field_chat_message,
    DemandParticular.GENDER: gender_field_chat_message,
    DemandParticular.SALARY_MINIMUM: salary_minimum_field_chat_message,
    DemandParticular.SALARY_MAXIMUM: salary_maximum_field_chat_message,
    DemandParticular.SALARY_STATEMENT_REQUIREMENT: salary_statement_requirement_field_chat_message,
    DemandParticular.RUBRICS: rubrics_field_chat_message,
    DemandParticular.YEARS_OF_EXPERIENCE: years_of_experience_field_chat_message,
    DemandParticular.STUDENTSHIP_REQUIREMENT: studentship_requirement_field_chat_message,
    DemandParticular.LANGUAGES: languages_field_chat_message,
    DemandParticular.EMPLOYMENT_TYPES: employment_types_field_chat_message,
    DemandParticular.FIELDS: fields_field_chat_message,
    DemandParticular.EDUCATIONS: educations_field_chat_message,
    DemandParticular.CURRICULUM_VITAE: curriculum_vitae_field_chat_message
}