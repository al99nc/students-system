from typing import Optional
from .base import SchoolBaseModel


class Course(SchoolBaseModel):
    courses_id: Optional[int] = None
    courses_name: str
    courses_description: str
