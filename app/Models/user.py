from typing import Optional
from .base import SchoolBaseModel


class User(SchoolBaseModel):
    users_id: Optional[int] = None
    user_name: str
    user_password: str
    user_email: str
    administrator: Optional[bool] = None
