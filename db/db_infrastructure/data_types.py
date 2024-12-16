
from infrastructure.enums import *

import sqlalchemy


DATA_TYPES = {
    DemandParticular.JOB_TITLE: sqlalchemy.CHAR(300),
    DemandParticular.SKILLS: sqlalchemy.VARCHAR,
    DemandParticular.PHOTO_REQUIREMENT: sqlalchemy.BOOLEAN,
    DemandParticular.AGE_MINIMUM: sqlalchemy.INTEGER,
    DemandParticular.AGE_MAXIMUM: sqlalchemy.INTEGER,
    DemandParticular.GENDER: sqlalchemy.INTEGER,
    DemandParticular.SALARY_MINIMUM: sqlalchemy.INTEGER,
    DemandParticular.SALARY_MAXIMUM: sqlalchemy.INTEGER,
    DemandParticular.SALARY_STATEMENT_REQUIREMENT: sqlalchemy.BOOLEAN,
    DemandParticular.RUBRICS: sqlalchemy.VARCHAR,
    DemandParticular.YEARS_OF_EXPERIENCE: sqlalchemy.VARCHAR,
    DemandParticular.STUDENTSHIP_REQUIREMENT: sqlalchemy.BOOLEAN,
    DemandParticular.LANGUAGES: sqlalchemy.VARCHAR,
    DemandParticular.EMPLOYMENT_TYPES: sqlalchemy.VARCHAR,
    DemandParticular.FIELDS: sqlalchemy.VARCHAR,
    DemandParticular.EDUCATIONS: sqlalchemy.VARCHAR,
    DemandParticular.CURRICULUM_VITAE: sqlalchemy.VARCHAR
}