from typing import Optional
from datetime import datetime
from .base import SchoolBaseModel


class Teacher(SchoolBaseModel):
    teachers_id: Optional[int] = None
    first_name: str
    last_name: str
    email: str
    gender: str
    date_of_birth: datetime
    address: str
