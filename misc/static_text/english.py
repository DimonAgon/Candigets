#keywords
from misc.static_text.ukrainian import salary_kw, fullness_kw

#particles
    #p̶a̶r̶t̶i̶c̶l̶e̶s̶

    #nouns
candidate_kw = "candidate"
candidates_kw = f"{candidate_kw}s"
ad_kw = "ad"
ads_kw = f"{ad_kw}s"
source_kw = "source"
profession_kw = "profession"
name_kw = "name"
location_kw = "location"
age_kw = "age"
salary_kw = "salary"
job_kw = "job"
jobs_kw = f"{job_kw}s"
experience_kw = "experience"
experiences_kw = f"{experience_kw}s"
cv_kw = "cv"
fullness_kw = "fullness"
update_kw = "update"
connection_kw = "connection"
status_kw = "status"
picture_kw = "picture"
search_kw = "search"
demand_kw = "demand"
id_kw = "id"
form_kw = "form"
user_kw = "user"
administrator_kw = "administrator"
creator_kw = "creator"
page_kw = "page"
html_kw = "html"
href_kw = "href"
src_kw = "src"
    #n̶o̶u̶n̶s̶

    #verbs
collect_kw = "collect"
transmit_kw = "transmit"
    #v̶e̶r̶b̶s̶

    #adjectives
inner_kw = "inner"
external_kw = "external"
    #a̶d̶j̶e̶c̶t̶i̶v̶e̶s̶

    #adverbs
    #a̶d̶v̶e̶r̶b̶s

#k̶e̶y̶w̶o̶r̶d̶s̶

#keyword combinations
#k̶e̶y̶w̶o̶r̶d̶ c̶o̶m̶b̶i̶n̶a̶t̶i̶o̶n̶s̶

#phrase parts

    #fields
    #f̶i̶e̶l̶d̶s̶

    #notice
    #n̶o̶t̶i̶c̶e

    #success
    #s̶u̶c̶c̶e̶s̶s̶

    #fail
    #f̶a̶i̶l̶

#p̶h̶r̶a̶s̶e̶ p̶a̶r̶t̶s̶

#phrases

    #fields
    #f̶i̶e̶l̶d̶s̶

    #fail
    #f̶a̶i̶l̶

    #notice
    #n̶o̶t̶i̶c̶e

    #success
    #s̶u̶c̶c̶e̶s̶s̶

#p̶h̶r̶a̶s̶e̶s

#texts
#t̶e̶x̶t̶s̶

#misc

    #table names
candidate_ad_table_name = f"{candidate_kw}_{ad_kw}"
search_demand_table_name = f"{search_kw}_{demand_kw}"
candidates_ads_table_name = f"{candidates_kw}_{ads_kw}"
job_experience_table_name = f"{job_kw}_{experience_kw}"
jobs_experiences_table_name = f"{jobs_kw}_{experiences_kw}"
    #t̶a̶b̶l̶e̶̶ ̶n̶a̶m̶e̶s̶

    #form names
candidate_search_demand_form_name = f"{candidate_kw}-{search_kw}-{demand_kw}"
    #f̶o̶r̶m̶ ̶n̶a̶m̶e̶s̶
id_field_reference_pattern = f"{'{form_name}'}.{id_kw}"
    #field references
candidate_ad_id_field_reference = id_field_reference_pattern.format(form_name=candidate_ad_table_name)
search_demand_id_field_reference = id_field_reference_pattern.format(form_name=search_demand_table_name)
    #f̶i̶e̶l̶d̶ ̶r̶e̶f̶e̶r̶e̶n̶c̶e̶s̶
    #field names
cv_fullness_field_name = f"{cv_kw}_{fullness_kw}"
connection_status_field_name = f"{connection_kw}_{status_kw}"
external_id_field_name = f"{external_kw}_{id_kw}"
search_demand_id_field_name = f"{search_kw}_{demand_kw}_{id_kw}"
    #f̶i̶e̶l̶d̶ ̶n̶a̶m̶e̶s̶

    #attribute names
user_id_attribute_name = f"{user_kw}_{id_kw}"
inner_HTML_attribute_name = f"{inner_kw}{html_kw.capitalize()}"
    #a̶t̶t̶r̶i̶b̶u̶t̶e̶ ̶n̶a̶m̶e̶s̶

    #choices
    #c̶h̶o̶i̶c̶e̶s̶

#m̶i̶s̶c̶
