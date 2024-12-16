
from misc.static_text.ukrainian import gender_kw_choices, yes_no_kw_choices, yes_kw, no_kw
from infrastructure.enums import *
from scrapper.scrapper_ import CandidateRobotaScrapper


GENDER_CHOICES = gender_kw_choices
YES_NO_CHOICES = yes_no_kw_choices
YES_CHOICE = yes_kw
NO_CHOICE = no_kw
ALL_UNPREDICTABLE_PARTICULARS_CHOICES = CandidateRobotaScrapper.scrap_all_unpredictable_choices()
CHOICES = {
    DemandParticular.PHOTO_REQUIREMENT: YES_NO_CHOICES,
    DemandParticular.GENDER: GENDER_CHOICES,
    DemandParticular.RUBRICS: ALL_UNPREDICTABLE_PARTICULARS_CHOICES[DemandParticular.RUBRICS],
    DemandParticular.YEARS_OF_EXPERIENCE: ALL_UNPREDICTABLE_PARTICULARS_CHOICES[DemandParticular.YEARS_OF_EXPERIENCE],
    DemandParticular.STUDENTSHIP_REQUIREMENT: YES_NO_CHOICES,
    DemandParticular.LANGUAGES: ALL_UNPREDICTABLE_PARTICULARS_CHOICES[DemandParticular.LANGUAGES],
    DemandParticular.EMPLOYMENT_TYPES: ALL_UNPREDICTABLE_PARTICULARS_CHOICES[DemandParticular.EMPLOYMENT_TYPES],
    DemandParticular.FIELDS: ALL_UNPREDICTABLE_PARTICULARS_CHOICES[DemandParticular.FIELDS],
    DemandParticular.EDUCATIONS: ALL_UNPREDICTABLE_PARTICULARS_CHOICES[DemandParticular.EDUCATIONS],
    DemandParticular.CURRICULUM_VITAE: ALL_UNPREDICTABLE_PARTICULARS_CHOICES[DemandParticular.CURRICULUM_VITAE]
}