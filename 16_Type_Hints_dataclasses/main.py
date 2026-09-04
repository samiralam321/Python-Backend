# Type Hints 

def add(a:int, b:int):
    return a+b

# You can also write : 

age:int = 21
name:str = "Samir"
price:float = 99.5
is_logged_in:bool = True


# Type hints for Functions 

def add(a:int, b:int) -> int:  # function expected to return an int
    return a+b

def greet(name:str) ->str:
    return "Hello" + name



# List with Type Hints

numbers: list[int] = [10,20,30,40]

names: list[str] = ["Samir", "Rahul", "Aman"]


# Dictionary : 

student = {
    "name" : "Samir",
    "age" : 21
}


student: dict[str,int]



# Type aliases

# All Correct

user_id : int
UserID = int
user_id : UserID = 101


# What type of Hints Matter in Backend ?

# Imagine you are building an API
# A function might look like : 

def create_user(name:str, age:int) -> dict:
    ....

# Immediately, another developer understand : 

# name -> string
# age -> integer
# return -> dictoinary 

# without reading the entire function.
# this becomes extremly useful when your project has hundreds of functions



############### Dataclasses #################

storing a user:
can use dictionary 

user = {
    "name" : "Samir",
    "age" : 21,
    "email" : "sam@gmail.com"
}

what you have 50 user object?
use classes

class User:

    def __init__(self, name, age, email):
        self.name = name
        self.age = age
        self.email = email


user = User("Samir", 21, "sam@gmail.com")


But Python gives us a shortcut called a Dataclass



################### Dataclass #############

from dataclasses import dataclass

@dataclass
class User:
    name:str
    age:int
    email:str

user = User("Samir", 21, "sam@gmail.com")

print(user.name)
print(user.age)
print(user.email)

# why this is useful : 

# without dataclass

class User:
    
    def __init__(self, name, age, emial):
        self.name = name
        self.age = age
        self.email = email


# with dataclass

@dataclass

class User:
    name:str
    age:int
    email:str

#python automatically generates useful things such as initializer

# do not need to repeatedly write : 

# self.name = name
# self.age = age
# self.email = email


## Dataclass with default values 

@dataclass

class User:
    name: str
    age: int = 18


# Datclass + Methods 
# A dataclass can still have methods

# -----------------------------------------------------

from dataclasses import dataclass

@dataclass

class User:
    name:str
    age: int

    def greet(self):
        print("hello", self.name)

user = User("Samir", 21)
user.greet()  # Hello Samir

# So, dataclass reduces boilerplat for data-heavy classes























