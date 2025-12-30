from typing import Optional
from datetime import datetime
from .base import SchoolBaseModel


class Student(SchoolBaseModel):
    students_id: Optional[int] = None
    first_name: str
    last_name: Optional[str] = None
    email: Optional[str] = None
    gender: Optional[str] = None
    date_of_birth: Optional[datetime] = None
    address: Optional[str] = None
    countries_id: Optional[int] = None
