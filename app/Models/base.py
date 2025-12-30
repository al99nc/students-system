from pydantic import BaseModel, ConfigDict


class SchoolBaseModel(BaseModel):
    model_config = ConfigDict(from_attributes=True)
