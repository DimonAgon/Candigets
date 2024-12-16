
body_xpath = (
    '/html/'
    'body/'
)

job_title_and_skills_input_xpath = (
    f'{body_xpath}'
    'div[1]/'
    'div[2]/'
    'div/'
    'div/'
    'alliance-employer-cvdb-header-filters/'
    'section/'
    'div/'
    'alliance-employer-cvdb-desktop-filter-keyword/'
    'santa-suggest-input/'
    'santa-drop-down/'
    'div/'
    'div[1]/'
    'santa-input/'
    'div/'
    'input'
)
#TODO: add location-related path

page_xpath = (
    'app-root/'
    'div/'
    'alliance-cv-list-page/'
    'main/'
    'article/'
)

requirements_section_xpath = (
    f'{body_xpath}'
    f'{page_xpath}'
    'div[2]/'
    'alliance-employer-cvdb-vertical-filters-sidebar/'
    'div/'
    'alliance-employer-cvdb-vertical-filters-panel/'
    'div/'
)

photo_requirement_toggler_xpath = (
    f'{requirements_section_xpath}'
    'div[1]/'
    'santa-toggler/'
    'label/'
    'span'
)

age_minimum_input_xpath = (
    f'{requirements_section_xpath}'
    'div[2]/'
    'alliance-employer-cvdb-simple-age/'
    'lib-input-range/'
    'div/'
    'div[1]/'
    'santa-input/'
    'div/'
    'input'
)

age_maximum_input_xpath = (
    f'{requirements_section_xpath}'
    'div[2]/'
    'alliance-employer-cvdb-simple-age/'
    'lib-input-range/'
    'div/'
    'div[2]/'
    'santa-input/'
    'div/'
    'input'
)

salary_minimum_input_xpath = (
    f'{requirements_section_xpath}'
    'div[4]/'
    'alliance-employer-cvdb-simple-salary/'
    'lib-input-range/'
    'div/'
    'div[1]/'
    'santa-input/'
    'div/'
    'input'
)

salary_maximum_input_xpath = (
    f'{requirements_section_xpath}'
    'div[4]/'
    'alliance-employer-cvdb-simple-salary/'
    'lib-input-range/'
    'div/'
    'div[2]/'
    'santa-input/'
    'div/'
    'input'
)

gender_switcher_pattern_xpath = (
    f'{requirements_section_xpath}'
    'div[3]/'
    'alliance-employer-cvdb-simple-gender/'
    'santa-switcher-group/'
    'div/'
    f'santa-switcher[{"{number}"}]/'
    'label'
)

salary_statement_requirement_toggler_xpath = (
    f'{requirements_section_xpath}'
    'div[4]/'
    'lib-without-salary/'
    'santa-toggler/'
    'label/'
    'span'
)

rubric_menu_maximizer_button_xpath = (
    f'{requirements_section_xpath}'
    'div[5]/'
    'alliance-employer-cvdb-simple-rubric/'
    'santa-button/'
    'button'
)

rubric_label_xpath_pattern = (
    f'{requirements_section_xpath}'
    'div[5]/'
    'alliance-employer-cvdb-simple-rubric/'
    'alliance-shared-checkbox-recursive-list/'
    f'div[{"{number}"}]/'
    'div/'
    'div/'
    'div[1]/'
    'div/'
    'p'
)

rubric_checkbox_xpath_pattern = (
    f'{requirements_section_xpath}'
    'div[5]/'
    'alliance-employer-cvdb-simple-rubric/'
    'alliance-shared-checkbox-recursive-list/'
    f'div[{"{number}"}]/' # first div is empty, rubrics starting from second one #TODO: consider
    'santa-checkbox/'
    'div/'
    'label'
)

years_of_experience_category_label_xpath_pattern = (
    f'{requirements_section_xpath}'
    'div[6]/'
    'alliance-employer-cvdb-simple-experience/'
    'alliance-shared-checkbox-recursive-list/'
    f'div[{"{number}"}]/'
    'div/'
    'div/'
    'div/'
    'div/'
    'p'
)

years_of_experience_category_checkbox_xpath_pattern = (
    f'{requirements_section_xpath}'
    'div[6]/'
    'alliance-employer-cvdb-simple-experience/'
    'alliance-shared-checkbox-recursive-list/'
    f'div[{"{number}"}]/'
    'santa-checkbox/'
    'div/'
    'label'
)

studentship_requirement_toggler_xpath = (
    f'{requirements_section_xpath}'
    'div[6]/'
    'div/'
    'santa-toggler/'
    'label/'
    'span'
)

language_menu_maximizer_button_xpath = (
    f'{requirements_section_xpath}'
    'div[7]/'
    'alliance-employer-cvdb-simple-language/'
    'santa-button/'
    'button'
)

language_label_xpath_pattern = (
    f'{requirements_section_xpath}'
    'div[7]/'
    'alliance-employer-cvdb-simple-language/'
    'alliance-shared-checkbox-recursive-list/'
    f'div[{"{number}"}]/'
    'div/'
    'div/'
    'div[1]/'
    'div/'
    'p'
)

language_checkbox_xpath_pattern = (
    f'{requirements_section_xpath}'
    'div[7]/'
    'alliance-employer-cvdb-simple-language/'
    'alliance-shared-checkbox-recursive-list[2]/'
    f'div[{"{number}"}]/'
    'santa-checkbox/'
    'div/'
    'label'
)

employment_type_label_xpath_pattern = (
    f'{requirements_section_xpath}'
    'div[8]/'
    'alliance-employer-cvdb-schedule-simple/'
    'alliance-shared-checkbox-recursive-list/'
    f'div[{"{number}"}]/'
    'div/'
    'div/'
    'div/'
    'div/'
    'p'
)

employment_type_checkbox_xpath_pattern = (
    f'{requirements_section_xpath}'
    'div[8]/'
    'alliance-employer-cvdb-schedule-simple/'
    'alliance-shared-checkbox-recursive-list/'
    f'div[{"{number}"}]/'
    f'santa-checkbox/'
    f'div/'
    'label'
)

field_menu_maximizer_button_xpath = (
    f'{requirements_section_xpath}'
    'div[9]/'
    'alliance-employer-cvdb-branches-simple/'
    'santa-button/'
    'button'
)

field_label_xpath_pattern = (
    f'{requirements_section_xpath}'
    'div[9]/'
    'alliance-employer-cvdb-branches-simple/'
    'alliance-shared-checkbox-recursive-list/'
    f'div[{"{number}"}]/'
    'div/'
    'div/'
    'div/'
    'div/'
    'p'
)

field_checkbox_xpath_pattern = (
    f'{requirements_section_xpath}'
    'div[8]/'
    'alliance-employer-cvdb-schedule-simple/'
    'alliance-shared-checkbox-recursive-list/'
    f'div[{"{number}"}]/'
    'santa-checkbox/'
    'div/'
    'label'
)

education_label_xpath_pattern = (
    f'{requirements_section_xpath}'
    'div[10]/'
    'alliance-employer-cvdb-education-simple/'
    'alliance-shared-checkbox-recursive-list/'
    f'div[{"{number}"}]/'
    'div/'
    'div/'
    'div/'
    'div/'
    'p'
)

education_checkbox_xpath_pattern = (
    f'{requirements_section_xpath}'
    'div[10]/'
    'alliance-employer-cvdb-education-simple/'
    'alliance-shared-checkbox-recursive-list/'
    f'div[{"{number}"}]/'
    'santa-checkbox/'
    'div/'
    'label'
)

curriculum_vitae_label_xpath_pattern = (
    f'{requirements_section_xpath}'
    'div[11]/'
    'alliance-employer-cvdb-resume-filling-simple/'
    'alliance-shared-checkbox-recursive-list/'
    f'div[{"{number}"}]/'
    'div/'
    'div/'
    'div/'
    'div/'
    'p'
)

curriculum_vitae_checkbox_xpath_pattern = (
    f'{requirements_section_xpath}'
    'div[11]/'
    'alliance-employer-cvdb-resume-filling-simple/'
    'alliance-shared-checkbox-recursive-list/'
    f'div[{"{ad_number}"}]/'
    'santa-checkbox/'
    'div/'
    'label'
)
candidate_ad_source_anchor_xpath_pattern = (
    f'{body_xpath}'
    'app-root/'
    'div/'
    'alliance-cv-list-page/'
    'main/'
    'article/'
    'div[1]/'
    'div/'
    'alliance-employer-cvdb-cv-list/'
    'div/'
    'div/'
    f'alliance-employer-cvdb-cv-list-card[{"{ad_number}"}]/'
    'section/'
    'div/'
    'alliance-shared-link-wrapping/'
    'a'
)

candidate_ad_content_xpath_pattern = (
    f'{candidate_ad_source_anchor_xpath_pattern}/'
    'alliance-shared-ui-media-adaptive-container/'
    'alliance-employer-cvdb-card-content-desktop/'
    'div/'
)

candidate_ad_profession_paragraph_xpath_pattern = (
    f'{candidate_ad_content_xpath_pattern}'
    'div[2]/'
    'p[1]'
)

candidate_ad_name_paragraph_xpath_pattern = (
    f'{candidate_ad_content_xpath_pattern}'
    'div[2]/'
    'div[1]/'
    'p'
)

candidate_ad_location_paragraph_xpath_pattern = (
    f'{candidate_ad_content_xpath_pattern}'
    'div[2]/'
    'div[1]/'
    'div[1]/'
    'p'
)

candidate_ad_age_paragraph_xpath_pattern = (
    f'{candidate_ad_content_xpath_pattern}'
    'div[2]/'
    'div[1]/'
    'div[2]/'
    'p'
)

candidate_ad_salary_paragraph_xpath_pattern = (
    f'{candidate_ad_content_xpath_pattern}'
    'div[2]/'
    'div[1]/'
    'div[3]/'
    'p'
)

candidate_ad_job_experience_paragraph_xpath_pattern = (
    f'{candidate_ad_content_xpath_pattern}'
    'div[2]/'
    f'p[{"{paragraph_number}"}]'
)

candidate_ad_cv_fullness_paragraph_pattern = (
    f'{candidate_ad_content_xpath_pattern}'
    'div[3]/'
    'alliance-fillable-resume/'
    'div'
)

candidate_ad_update_paragraph_pattern = (
    f'{candidate_ad_content_xpath_pattern}'
    'div[2]/'
    'div[2]/'
    'p[1]'
)

candidate_ad_connection_status_paragraph_xpath_pattern = (
    f'{candidate_ad_content_xpath_pattern}'
    'div[2]/'
    'div[2]/'
    'p[2]'
)

candidate_ad_image_xpath_pattern = (
    f'{candidate_ad_content_xpath_pattern}'
    'div[1]/'
    'alliance-employer-resume-circle-photo/'
    'div/'
    'img'
)










