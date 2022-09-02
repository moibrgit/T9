import pydantic

from pydantic import BaseModel
from typing import Optional


class Person(BaseModel):
    
    first_name:str 
    last_name:str 
    age: Optional[int]
    
    
    @pydantic.validator("age")
    @classmethod
    def validate_age(cls, value):
        if value < 18:
            raise ValueError("The age must be equal or over 18") 
        
        return value
    
            



person1 = Person(first_name="Thomas", last_name="Meier", age = 17)
print(person1)