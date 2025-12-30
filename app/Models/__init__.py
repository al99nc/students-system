from .base import SchoolBaseModel
from .country import Country
from .student import Student
from .teacher import Teacher
from .course import Course
from .subject import Subject
from .user import User

__all__ = [
    "SchoolBaseModel",
    "Country",
    "Student",
    "Teacher",
    "Course",
    "Subject",
    "User",
    "StudentsCourses",
    "TeachersCourses",
    "CoursesSubjects",
]