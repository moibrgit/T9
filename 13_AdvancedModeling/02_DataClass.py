# Python  3.10 : ---> dataclasses


""" 
DataclasseS:
- dataclasses are standard library within python 3.10 (not external library)
- does not need extra __init__()
- The attributes are instance based attributes and not class based attribtes (even they are out of the methods)
- frozen=True ---> makes the object immutable --> not changeable after constructing
- repr = False --> do not display it while printing ---> not by __repr__
- init=False ---> do not allow the user to provide the value within creating the instance
- there is no data validation

"""


from dataclasses import dataclass, field
import random, string


def generate_random_id():
    return "".join(random.choices(string.ascii_lowercase, k = 8))

#@dataclass(frozen=True)
@dataclass
class Person:
    first_name:str
    last_name:str
    age:int 
    
    age_duplicated:int = field(init=False)
    
    person_id:int = field(repr = False)
    salary:int = field(repr = True, init=False)   
    
    list_of_projects: list[str] = field(default_factory = list)
    
    person_random_id: str = field(default_factory = generate_random_id, init= False )
        
    weight:int = 80 # default value
    
    
    
    # Custom __init__ after the original constructor --> POST (After) construtor
    def __post_init__(self):
        self.age_duplicated = self.age * 2 
    
    
 
    
     


# person1 = Person("Thomas", "Meier", 50, 1, 100)
# person2 = Person("Sven", "Meier", 50,2, 90)

person1 = Person(first_name="Thomas", last_name="Meier", age = 50, person_id= 1, weight=100)
person2 = Person(first_name="Sven", last_name="Meier", age = 50, person_id= 2, weight=90)
person3 = Person(first_name=1, last_name=2, age = 3, person_id= 2, weight=90)


person1.salary = 60
person2.salary = 60
person3.salary = 60


print(person1) # Person(first_name='Thomas', last_name='Meier', age=50)
#äprint(person1 == person2) # False

person1.first_name = "Thomas 1"
print(person1)
print(person2)
print(person3)