# untill now our pydantic model only checked basic data types

class UserCreate(BaseMode):
    name: str
    age: int
    email: str

# this checks : 

name  → must be string
age   → must be integer
email → must be string

# but there is a problem : suppsoe someone sends : 

{
    "name" : "",
    "age" : -40,
    "email" : "hello"
}


# technillay all the above is correct coz, name is string, age is integer, email is string
# but logically we know it is not correct 


# here comes Data Validation

Client sends data
        ↓
Backend checks rules
        ↓
Valid?
   YES      NO
    ↓        ↓
Accept    Reject



gt = greater than 0
ge = greater than equal to 0
lt = less than
le = less than equals to 

#


from fastapi import FastAPI
from pydantic import BaseModel, Field

app = FastAPI()

class Product(BaseModel):
    name: str = Field(
        min_length = 2,
        max_length = 100,
        description = "Product name"
    )

    price: float = Field(
        gt = 0,
        description = "Price must be greater than 0"
    )

    stock: int = Field(
        default = 0,
        ge = 0,
        description = "Stock cannot be megative"
    )

@app.get("/products")
def create_product(product : Product):
    return {
        "message ": "product created!",
        "product" : product
    }



####### Mutiple Validation Rules ########

class Product(BaseModel):
    name: str = Field(
        min_length = 2,
        max_length = 100
    )

    price:float = Field(
        gt = 0,
        le = 1000000
    )

    stock:int = Field(
        ge=0,
        le=100000
    )


################ Email Validation ##############

from pydantic import BaseModel, EmailStr

class User(BaseModel):
    name: str
    email: EmailStr



# Complete User Validation Exampels


from fastapi import FastAPI
from pydantic import BaseModel, Field, EmailStr

app = FastAPI()

class UserCreate(BaseMode):
    name: str = Field(
        min_length=2,
        max_length=50
    )

    age: int = Field(
        ge=1,
        le=120
    )

    email: EmailStr

    password: str = Field(
        min_length = 6
    )

@app.post("/users")
def create_user(user : UserCreate):
    return {
        "message" : "User created",
        "user" : {
            "name" : user.name,
            "age" : user.age,
            "email" : user.email
        }
    }








































































































