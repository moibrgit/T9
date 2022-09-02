class Car:
    pass 

class Person:
    first_name:str
    last_name:str
    age:int 
    
    
    def __init__(self, first_name, last_name, age) :
        
        self.first_name = first_name
        self.last_name = last_name
        self.age = age 
        self.weight = 80   
        self.salary = ""      
        
    def __repr__(self):
        return f"{self.first_name} - {self.last_name}"
        
    def __eq__(self, other: object) -> bool:                
        if self.age == other.age:
            return True
            
        return False

 

# Create Instances
person1 = Person("Thomas", "Meier", 45)
person2 = Person("Sven", "Meier", 45)

print(person1)
print(person2)


print(person1 == person2)
 
# Problem
person1.salar = 50

print(person1.__dict__)
print(person2.__dict__)