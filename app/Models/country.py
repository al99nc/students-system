from typing import Optional
from .base import SchoolBaseModel


class Country(SchoolBaseModel):
    countries_id: Optional[int] = None
    iso: str
    country_name: str
    phone_code: int
    iso3: str
