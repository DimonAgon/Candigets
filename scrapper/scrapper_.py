
from selenium.webdriver.chrome.webdriver import WebDriver
from selenium.webdriver.common.by import By
from selenium.common import exceptions as seleniumexceptions
from selenium.webdriver.common.keys import Keys

from .driver import driver
from db.utils import *
from infrastructure.enums import *
from infrastructure.interactions import *
from scrapper.scrapper_infrastructure.reading import *
from scrapper.scrapper_infrastructure.paths import *
from .constants import *
from types_ import *
from misc.re_patterns import *

import json

import time

from typing import Dict, List


class CandidateRobotaScrapper:

    @classmethod
    def scrap_choices(cls, selectable_particular: DemandParticular) -> List[str]:
        choices = []
        driver.get(ROBOTA_CANDIDATES_URL)
        driver.maximize_window()
        if selectable_particular in DEMAND_PARTICULARS_TO_MENU_MAXIMIZERS_PATHS:
            particular_menu_maximizer_xpath = DEMAND_PARTICULARS_TO_MENU_MAXIMIZERS_PATHS[selectable_particular]
            particular_menu_maximizer = driver.find_element(By.XPATH, particular_menu_maximizer_xpath)
            particular_menu_maximizer.click()
        particular_label_number = 1
        particular_label_xpath_pattern = DEMAND_PARTICULARS_TO_LABELS_PATHS[selectable_particular]
        particular_label_xpath_shift = DEMAND_PARTICULARS_TO_SHIFTS[selectable_particular]
        while True:
            try:
                particular_label_number_shifted = particular_label_number + particular_label_xpath_shift
                particular_label_xpath = particular_label_xpath_pattern.format(number=particular_label_number_shifted)
                particular_label = driver.find_element(By.XPATH, particular_label_xpath)
                particular_label_text: str = particular_label.text
                particular_label_text_stripped = particular_label_text.strip()
                choices.append(particular_label_text_stripped)
                particular_label_number += 1
            except seleniumexceptions.NoSuchElementException:
                break
        return choices

    @classmethod
    def scrap_all_unpredictable_choices(cls) -> Dict[DemandParticular, List[str]]:
        all_choices = dict(())
        selectable_particulars = INTERACTION_VARIANTS[InteractionVariant.Clickable.SELECTABLE]
        predictable_particulars = INTERACTION_VARIANTS[InteractionVariant.Clickable.Extension.PREDICTABLE]
        selectable_particulars_except_predictable = selectable_particulars - predictable_particulars
        for particular in selectable_particulars_except_predictable:
            particular_choices = cls.scrap_choices(particular)
            all_choices[particular] = particular_choices
        return all_choices


    @classmethod
    def prepare_demand_field_datas(cls, demand: Base) -> List[ParticularFieldData]:
        demand_fields_data = get_db_object_fields_data(demand)
        del demand_fields_data[id_kw]
        del demand_fields_data[user_id_attribute_name]
        del demand_fields_data[collect_kw]
        del demand_fields_data[transmit_kw]
        demand_field_datas = [
            ParticularFieldData(
                next((particular for particular in DemandParticular if particular.name.lower() == field_name), None),
                field_value
            )
            for field_name, field_value
            in demand_fields_data.items()
        ]
        demand_field_datas.sort(key=lambda field: field.particular.value)
        return demand_field_datas

    @classmethod
    def search_ads(cls, demand: SearchDemand, driver_: WebDriver=driver) -> None:
        driver_.get(ROBOTA_CANDIDATES_URL)
        driver_.maximize_window()
        demand_field_datas = cls.prepare_demand_field_datas(demand)
        put_in_statuses: Dict[DemandParticular, bool] = dict(())
        for field_data in demand_field_datas:
            if field_data.particular in INTERACTION_VARIANTS[InteractionVariant.Writable.Extension.SEARCHABLE]:
                if not field_data.value is None:
                    put_in_statuses[field_data.particular] = False
        searched = False
        for field_data in demand_field_datas:
            if field_data.value:
                try:
                    particular_input_xpath = DEMAND_PARTICULARS_TO_INPUT_PATHS[field_data.particular]
                    if field_data.particular in INTERACTION_VARIANTS[InteractionVariant.Writable]:
                        particular_input_ = driver_.find_element(By.XPATH, particular_input_xpath)
                        particular_input_value = particular_input_.get_attribute('value')
                        if particular_input_value: particular_input_.send_keys(" ")
                        particular_input_.send_keys(field_data.value)
                        if not searched:
                            if field_data.particular in put_in_statuses:
                                put_in_statuses[field_data.particular] = True
                            if not False in put_in_statuses.values():
                                searched = True
                                particular_input_.send_keys(Keys.ENTER)
                    elif field_data.particular in INTERACTION_VARIANTS[InteractionVariant.Clickable.SELECTABLE]:
                        particular_input_number_shift = DEMAND_PARTICULARS_TO_SHIFTS[field_data.particular]
                        deserialized_value = json.loads(field_data.value)
                        if field_data.particular in DEMAND_PARTICULARS_TO_MENU_MAXIMIZERS_PATHS:  # TODO: configure unnecessary maximization
                            particular_menu_maximizer_xpath = \
                                DEMAND_PARTICULARS_TO_MENU_MAXIMIZERS_PATHS[field_data.particular]
                            particular_menu_maximizer = driver_.find_element(By.XPATH, particular_menu_maximizer_xpath)
                            particular_menu_maximizer.click()
                            time.sleep(0.1)  # sleep is required to wait for element maximizing #TODO: configure sleep time
                        if field_data.particular in INTERACTION_VARIANTS[InteractionVariant.Clickable.Extension.MULTICHOICE]:
                            for particular_input_number in deserialized_value:
                                particular_input_number_shifted = particular_input_number + particular_input_number_shift
                                particular_input_ = \
                                    driver_.find_element(
                                        By.XPATH,
                                        particular_input_xpath.format(number=particular_input_number_shifted)
                                    )
                                particular_input_.click()
                            continue
                        particular_input_number = deserialized_value[0]
                        particular_input_number_shifted = particular_input_number + particular_input_number_shift
                        particular_input_ = driver_.find_element(
                            By.XPATH,
                            particular_input_xpath.format(number=particular_input_number_shifted)
                        )
                        particular_input_.click()
                    elif field_data.particular in INTERACTION_VARIANTS[InteractionVariant.Clickable.TOGGLEABLE]:
                        if field_data.value:
                            particular_input_ = driver_.find_element(By.XPATH, particular_input_xpath)
                            particular_input_.click()
                except (
                        seleniumexceptions.NoSuchElementException,
                        seleniumexceptions.ElementClickInterceptedException,
                        seleniumexceptions.ElementNotInteractableException,
                        seleniumexceptions.InvalidSelectorException
                ):
                    continue

    @classmethod
    def scrap_ad_data(cls, ad_number: int, driver_: WebDriver=driver) -> CandidateAdData:
        ad_data_dictionary = dict(())
        ad_source_anchor_xpath = candidate_ad_source_anchor_xpath_pattern.format(ad_number=ad_number)
        ad_source_anchor = \
            driver_.find_element(By.XPATH, ad_source_anchor_xpath)
        ad_source = ad_source_anchor.get_attribute(href_kw)
        ad_data_dictionary[source_kw] = ad_source
        ad_external_id = robota_candidate_external_id_repattern.findall(ad_source)[0]
        ad_data_dictionary[external_id_field_name] = ad_external_id
        for particular, particular_element_xpath_pattern in AD_PARTICULARS_TO_PARAGRAPH_PATHS.items():
            try:
                particular_field_name = particular.name.lower()
                if particular in READING_VARIANTS[ReadingVariant.Text]:
                    if particular in READING_VARIANTS[ReadingVariant.Text.UNARY_TEXT]:
                        particular_paragraph_xpath = particular_element_xpath_pattern.format(ad_number=ad_number)
                        particular_paragraph = \
                            driver_.find_element(By.XPATH, particular_paragraph_xpath)
                        particular_paragraph_text = particular_paragraph.text
                        ad_data_dictionary[particular_field_name] = particular_paragraph_text
                    elif particular in READING_VARIANTS[ReadingVariant.Text.PARALLEL_TEXT]:
                        ad_data_dictionary[particular_field_name] = []
                        particular_paragraph_number = 1
                        particular_paragraph_number_shift = AD_PARTICULARS_TO_SHIFTS[particular]
                        while True:
                            try:
                                particular_paragraph_number_shifted = \
                                    particular_paragraph_number + particular_paragraph_number_shift
                                particular_paragraph_xpath = particular_element_xpath_pattern.format(
                                    ad_number=ad_number,
                                    paragraph_number=particular_paragraph_number_shifted
                                )
                                particular_paragraph = driver_.find_element(By.XPATH, particular_paragraph_xpath)
                                particular_paragraph_text = particular_paragraph.text
                                ad_data_dictionary[particular_field_name].append(particular_paragraph_text)
                                particular_paragraph_number += 1
                            except seleniumexceptions.NoSuchElementException:
                                break
                elif particular in READING_VARIANTS[ReadingVariant.Path]:
                    particular_element_xpath = particular_element_xpath_pattern.format(ad_number=ad_number)
                    particular_element = driver_.find_element(By.XPATH, particular_element_xpath)
                    if particular in READING_VARIANTS[ReadingVariant.Path.HYPER_REFERENCE]:
                        particular_element_point_to__path = particular_element.get_attribute(href_kw)
                    elif particular in READING_VARIANTS[ReadingVariant.Path.SOURCE]:
                        particular_element_point_to__path = particular_element.get_attribute(src_kw)
                    ad_data_dictionary[particular_field_name] = particular_element_point_to__path
            except seleniumexceptions.NoSuchElementException:
                continue
        ad_data = CandidateAdData(**ad_data_dictionary)
        return ad_data

    @classmethod
    def scrap_ads_datas(cls, demand: SearchDemand, driver_: WebDriver=driver) -> List[CandidateAdData]:
        ads_datas = []
        cls.search_ads(demand, driver_)
        current_url = driver_.current_url
        page = 1
        while page == 1 or (page != 1 and driver_.current_url != current_url):
            next_page_url = f"{current_url}&{page_kw}={page}"
            driver_.get(next_page_url)
            current_url = driver_.current_url
            ad_number = 1
            while True:
                try:
                    ad_data = cls.scrap_ad_data(ad_number, driver_)
                    ads_datas.append(ad_data)
                    ad_number += 1
                except seleniumexceptions.NoSuchElementException:
                    break
            page += 1
        return ads_datas