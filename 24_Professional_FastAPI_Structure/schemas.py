# a schema define : 

# What data should come into our API?         ↓
# What fields are required?            ↓
# What data type should each field have?

from pydantic import BaseModel, Emailstr

class UserCreate(BaseModel): # it is used when we create a User
    name: str
    age:int
    email: EmailStr
    password: str


class UserUpdate(BaseModel): # it is used when we update an existing user
    name: str
    age: int
    email: EmailStr



# our final flow 

# Client Request
#       ↓
# routers/users.py
#       ↓
# Pydantic Schema Validation
#       ↓
# Database Query
#       ↓
# SQLite Database
#       ↓
# Response






















