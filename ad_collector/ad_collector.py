
import asyncio

from selenium import webdriver
from selenium.webdriver.chrome.webdriver import WebDriver

import sqlalchemy
from sqlalchemy.ext.asyncio import AsyncSession

from db.session_delivery import session_delivery
from db.models import *
from scrapper.driver import *
from scrapper.scrapper_ import *
from utils import *

import json

import os


class AdCollector:

    @classmethod
    @session_delivery.deliver_session
    async def collect_demand_ads(cls, demand: SearchDemand, session: AsyncSession, driver_: WebDriver=driver) -> None:
        ads_datas = CandidateRobotaScrapper.scrap_ads_datas(demand, driver_)
        for ad_data in ads_datas:
            ad_data_dictionary = ad_data.__dict__
            for key, value in ad_data_dictionary.items():
                if isinstance(value, (tuple, list, set)):
                    value_json = json.dumps(value)
                    ad_data_dictionary[key] = value_json
            new_ad = CandidateAd(search_demand=demand,  **ad_data_dictionary)
            await session.merge(new_ad)
        demand.collect = True
        await session.merge(demand)
        await session.commit()
        driver_.close()

    @classmethod
    @session_delivery.deliver_session
    async def collect_all_demands_ads(cls, session: AsyncSession) -> None:
        all_demands_to_collect_query = sqlalchemy.select(SearchDemand).where(SearchDemand.collect == False)
        all_demands_to_collect = await session.scalars(all_demands_to_collect_query)
        for demand in all_demands_to_collect:
            driver_ = webdriver.Chrome()
            await cls.collect_demand_ads(demand, driver_=driver_)