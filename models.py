from pydantic import BaseModel, Field
from typing import List
class name_date(BaseModel):
    date: str = Field(description="dates available in text")
    name: str = Field(description="name available in email")
    location : str= Field(description="location available in text")

class list_name_date(BaseModel):
    list_name_date: List[name_date] = Field(description="list of name and date")