
from infrastructure.enums import *
from scrapper.paths import *


DEMAND_PARTICULARS_TO_INPUT_PATHS = {
    DemandParticular.JOB_TITLE: job_title_and_skills_input_xpath,
    DemandParticular.SKILLS: job_title_and_skills_input_xpath,
    DemandParticular.PHOTO_REQUIREMENT: photo_requirement_toggler_xpath,
    DemandParticular.AGE_MAXIMUM: age_maximum_input_xpath,
    DemandParticular.AGE_MINIMUM: age_minimum_input_xpath,
    DemandParticular.GENDER: gender_switcher_pattern_xpath,
    DemandParticular.SALARY_MINIMUM: salary_minimum_input_xpath,
    DemandParticular.SALARY_MAXIMUM: salary_maximum_input_xpath,
    DemandParticular.SALARY_STATEMENT_REQUIREMENT: salary_statement_requirement_toggler_xpath,
    DemandParticular.RUBRICS: rubric_checkbox_xpath_pattern,
    DemandParticular.YEARS_OF_EXPERIENCE: years_of_experience_category_checkbox_xpath_pattern,
    DemandParticular.STUDENTSHIP_REQUIREMENT: studentship_requirement_toggler_xpath,
    DemandParticular.LANGUAGES: language_checkbox_xpath_pattern,
    DemandParticular.EMPLOYMENT_TYPES: employment_type_checkbox_xpath_pattern,
    DemandParticular.FIELDS: field_checkbox_xpath_pattern,
    DemandParticular.EDUCATIONS: education_checkbox_xpath_pattern,
    DemandParticular.CURRICULUM_VITAE: curriculum_vitae_checkbox_xpath_pattern
}

DEMAND_PARTICULARS_TO_MENU_MAXIMIZERS_PATHS = {
    DemandParticular.RUBRICS: rubric_menu_maximizer_button_xpath,
    DemandParticular.LANGUAGES: language_menu_maximizer_button_xpath,
    DemandParticular.FIELDS: field_menu_maximizer_button_xpath
}

DEMAND_PARTICULARS_TO_LABELS_PATHS = {
    DemandParticular.RUBRICS: rubric_label_xpath_pattern,
    DemandParticular.YEARS_OF_EXPERIENCE: years_of_experience_category_label_xpath_pattern,
    DemandParticular.LANGUAGES: language_label_xpath_pattern,
    DemandParticular.EMPLOYMENT_TYPES: employment_type_label_xpath_pattern,
    DemandParticular.FIELDS: field_label_xpath_pattern,
    DemandParticular.EDUCATIONS: education_label_xpath_pattern,
    DemandParticular.CURRICULUM_VITAE: curriculum_vitae_label_xpath_pattern
}

AD_PARTICULARS_TO_PARAGRAPH_PATHS = {
    AdParticular.PROFESSION: candidate_ad_profession_paragraph_xpath_pattern,
    AdParticular.NAME: candidate_ad_name_paragraph_xpath_pattern,
    AdParticular.LOCATION: candidate_ad_location_paragraph_xpath_pattern,
    AdParticular.AGE: candidate_ad_age_paragraph_xpath_pattern,
    AdParticular.SALARY: candidate_ad_salary_paragraph_xpath_pattern,
    AdParticular.JOBS_EXPERIENCES: candidate_ad_job_experience_paragraph_xpath_pattern,
    AdParticular.CV_FULLNESS: candidate_ad_cv_fullness_paragraph_pattern,
    AdParticular.UPDATE: candidate_ad_update_paragraph_pattern,
    AdParticular.CONNECTION_STATUS: candidate_ad_connection_status_paragraph_xpath_pattern,
    AdParticular.PICTURE: candidate_ad_image_xpath_pattern
}

DEMAND_PARTICULARS_TO_SHIFTS = {
    DemandParticular.GENDER: 0,
    DemandParticular.RUBRICS: 1,
    DemandParticular.YEARS_OF_EXPERIENCE: 0,
    DemandParticular.LANGUAGES: 0,
    DemandParticular.EMPLOYMENT_TYPES: 0,
    DemandParticular.FIELDS: 1,
    DemandParticular.EDUCATIONS: 1,
    DemandParticular.CURRICULUM_VITAE: 0
}

AD_PARTICULARS_TO_SHIFTS = {
    AdParticular.JOBS_EXPERIENCES: 1,
}