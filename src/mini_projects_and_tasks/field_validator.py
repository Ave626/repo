from pydantic import BaseModel,field_validator

class User(BaseModel):
    name : str
    @field_validator("name")
    @classmethod
    def check(cls,value : str) -> str:
        if value == "" or  not value.replace(" ", "").isalpha():
            raise ValueError("Name must contain only letters and spaces")
        return value