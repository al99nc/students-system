from typing import Optional
from .base import SchoolBaseModel


class Subject(SchoolBaseModel):
    subject_id: Optional[int] = None
    subject_name: str
    subject_description: str
