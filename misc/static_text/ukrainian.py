
#keywords

    #particles
only_kw = "тільки"
with_kw = "з"
from_kw = "з"
to_kw = "до"
not_kw = "не"
without_kw = "без"
in_kw = "в"
yes_kw = "так"
no_kw = "ні"
    #p̶a̶r̶t̶i̶c̶l̶e̶s̶

    #nouns
job_title_kwc = "посада"
skills_kw = "навички"
photo_kw = "фото"
age_kw = "вік"
salary_kw = "зарплатня"; salary_gen_kw = "зарплатні"
hryvnya_loc_kw = "гривні"
gender_kw = "стать"
rubric_kw = "рубрика"
experience_noun_kw = "досвід"
work_noun_gen_kw = "роботи"
students_kw = "студенти"
possession_kw = "володіння"
languages_obj_kw = "мовами"
type_kw = "тип"
occupation_gen_kw = "зайнятості"
field_kw = "галузь"
education_kw = "освіта"
fullness_kw = "заповненість"
resume_noun_kw = "резюме"
women_kw = "жінки"
men_kw = "чоловіки"
fail_noun_kw = "помилка"
integer_obj_kw = "числом"
sequence_obj_kw = "послідовністю"
choice_obj_kw = "вибором"
word_ojb_kw = "словом"
demand_kw = "вимога"; demand_acc_kw = "вимогу"
user_kw = "користувач"
administrator_kw = "адміністратор"
    #n̶o̶u̶n̶s̶

    #verbs
worked_mask_kw = "працював"
show_verb_kw = "показувати"
is_kw = "є"
exists_kw = "існує"
recommended_verb_kw = "рекомендується"
delete_kw = "видалити"; deleted_verb_kw = "видалено"
registered_verb_kw = "зареєстровано"
canceled_verb_kw = "перервано"
    #v̶e̶r̶b̶s̶

    #adjectives
which_adj_loc_fem_kw = "якій"
awaited_adj_fem_kw = "очікувана"
every_adj_fem_kw = "будь-яка"
entered_adj_neut_kw = "введене"
single_obj_mask_kw = "єдиним"
current_adj_fem_kw = "поточну"
    #a̶d̶j̶e̶c̶t̶i̶v̶e̶s̶

    #adverbs
    #a̶d̶v̶e̶r̶b̶s

#k̶e̶y̶w̶o̶r̶d̶s̶

#keyword combinations
awaited_salary_in_hryvnya_kwc = f"{awaited_adj_fem_kw} {salary_kw} {in_kw} {hryvnya_loc_kw}"
single_word_obj_kwc = f"{single_obj_mask_kw} {word_ojb_kw}"
#k̶e̶y̶w̶o̶r̶d̶ c̶o̶m̶b̶i̶n̶a̶t̶i̶o̶n̶s̶

#phrase parts

    #fields
    #f̶i̶e̶l̶d̶s̶

    #notice
on_cancelling_chat_message = canceled_verb_kw
    #n̶o̶t̶i̶c̶e

    #success
    #s̶u̶c̶c̶e̶s̶s̶

    #fail
fail_chat_message_pp = f"{fail_noun_kw}, {'{details}'}"
fail_chat_message_with_recommendation_pp = f"{fail_chat_message_pp}; {recommended_verb_kw} {'{recommendation}'}"
entered_check_fail_chat_message_pp_details = f"{entered_adj_neut_kw} {not_kw} {is_kw} {'{details}'}"
entered_check_fail_chat_message_pp = fail_chat_message_pp.format(details=entered_check_fail_chat_message_pp_details)
    #f̶a̶i̶l̶

#p̶h̶r̶a̶s̶e̶ p̶a̶r̶t̶s̶

#phrases

    #fields
job_title_field_chat_message = f"{job_title_kwc}"
skills_field_chat_message = f"{skills_kw}"
photo_requirement_field_chat_message = f"{only_kw} {with_kw} {photo_kw}"
age_minimum_field_chat_message = f"{age_kw} {from_kw}"
age_maximum_field_chat_message = f"{age_kw} {to_kw}"
gender_field_chat_message = f"{gender_kw}"
salary_minimum_field_chat_message = f"{awaited_salary_in_hryvnya_kwc} {from_kw}"
salary_maximum_field_chat_message = f"{awaited_salary_in_hryvnya_kwc} {to_kw}"
salary_statement_requirement_field_chat_message = f"{not_kw} {show_verb_kw} {without_kw} {salary_gen_kw}"
rubrics_field_chat_message = f"{rubric_kw}"
years_of_experience_field_chat_message = f"{experience_noun_kw} {work_noun_gen_kw}"
studentship_requirement_field_chat_message = f"{only_kw} {students_kw}"
languages_field_chat_message = f"{possession_kw} {languages_obj_kw}"
employment_types_field_chat_message = f"{type_kw} {occupation_gen_kw}"
fields_field_chat_message = f"{field_kw} {in_kw} {which_adj_loc_fem_kw} {worked_mask_kw}(ла)"
educations_field_chat_message = f"{education_kw}"
curriculum_vitae_field_chat_message = f"{fullness_kw} {resume_noun_kw}"
    #f̶i̶e̶l̶d̶s̶

    #fail
is_integer_string_check_fail_chat_message = \
    entered_check_fail_chat_message_pp.format(details=integer_obj_kw)
is_sequence_string_check_fail_chat_message = \
    entered_check_fail_chat_message_pp.format(details=sequence_obj_kw)
is_choice_check_fail_chat_message = \
    entered_check_fail_chat_message_pp.format(details=choice_obj_kw)
is_single_word_check_fail_chat_message = \
    entered_check_fail_chat_message_pp.format(details=single_word_obj_kwc)
is_administrator_check_fail_chat_message_details = f"{user_kw} {not_kw} {is_kw} {administrator_kw}"
is_administrator_check_fail_chat_message = fail_chat_message_pp.format(details=is_administrator_check_fail_chat_message_details)
no_user_demand_check_fail_chat_message_details = f"{demand_kw} {exists_kw}"
no_user_demand_check_fail_chat_message_recommendation = f"{delete_kw} {current_adj_fem_kw} {demand_acc_kw}"
no_user_demand_check_fail_chat_message = \
    fail_chat_message_with_recommendation_pp.format(
        details=no_user_demand_check_fail_chat_message_details,
        recommendation=no_user_demand_check_fail_chat_message_recommendation
    )
user_demand_exists_check_fail_chat_message = f"{demand_kw} {not_kw} {exists_kw}"
    #f̶a̶i̶l̶

    #notice
    #n̶o̶t̶i̶c̶e

    #success
search_demand_registration_success_chat_message = f"{demand_acc_kw} {registered_verb_kw}"
search_demand_on_deletion_success_chat_message = f"{current_adj_fem_kw} {demand_acc_kw} {deleted_verb_kw}"
    #s̶u̶c̶c̶e̶s̶s̶

#p̶h̶r̶a̶s̶e̶s

#texts
bot_instruction_text = (
    "/demand /dem /d— створити вимогу розсилки"
    "\n/clear_demand— очистити вимогу"
)
#t̶e̶x̶t̶s̶

#misc

    #choices
yes_no_kw_choices = (yes_kw, no_kw)
gender_kw_choices = (every_adj_fem_kw, women_kw, men_kw)
    #c̶h̶o̶i̶c̶e̶s̶

#m̶i̶s̶c̶
