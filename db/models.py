
import sqlalchemy
from sqlalchemy.orm import DeclarativeBase
from sqlalchemy.orm import Mapped, mapped_column, relationship

from .db_infrastructure.data_types import *
from db.constants import *
from misc.static_text.english import *

from typing import List


class Base(DeclarativeBase):
    ...

class CandidateAd(Base):
    __tablename__ = candidate_ad_table_name

    id: Mapped[int] = mapped_column(primary_key=True)
    external_id: Mapped[int] = mapped_column(unique=True)
    search_demand_id: Mapped[int] = mapped_column(sqlalchemy.ForeignKey(search_demand_id_field_reference))
    search_demand: Mapped['SearchDemand'] = relationship(back_populates=candidates_ads_table_name)
    source: Mapped[str] = mapped_column(sqlalchemy.CHAR(MAX_URL_LENGTH))
    picture: Mapped[str] = mapped_column(sqlalchemy.CHAR(MAX_URL_LENGTH), nullable=True)
    profession: Mapped[str] = mapped_column(nullable=True)
    name: Mapped[str] = mapped_column(nullable=True)
    location: Mapped[str] = mapped_column(nullable=True)
    age: Mapped[str] = mapped_column(nullable=True)
    salary: Mapped[str] = mapped_column(nullable=True)
    jobs_experiences: Mapped[int] = mapped_column(nullable=True)
    cv_fullness: Mapped[str] = mapped_column(nullable=True)
    update: Mapped[str] = mapped_column(nullable=True)
    connection_status: Mapped[str] = mapped_column(nullable=True)

class SearchDemand(Base):
    __tablename__ = search_demand_table_name

    id: Mapped[int] = mapped_column(primary_key=True)
    user_id: Mapped[int] = mapped_column(unique=True)
    universal_particular_field_data = {'nullable': True}
    for particular in DemandParticular:
        field_name = particular.name.lower()
        field_data_type = DATA_TYPES[particular]
        locals()[field_name] = mapped_column(field_data_type, **universal_particular_field_data)
    candidates_ads: Mapped[List['CandidateAd']] = relationship(back_populates=search_demand_table_name)
    collect: Mapped[bool]
    transmit: Mapped[bool]
