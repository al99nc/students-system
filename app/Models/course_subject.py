from typing import Optional
from .base import SchoolBaseModel


class CoursesSubjects(SchoolBaseModel):
    courses_subjects_id: Optional[int] = None
    courses_id: int
    subjects_id: int