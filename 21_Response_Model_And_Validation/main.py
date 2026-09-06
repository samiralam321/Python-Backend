# until now, we focused on : 

Client sends data
        ↓
Pydantic Model validates it
        ↓
Backend receives data

# this called Request Validation 

# but there ie another side : 

Backend sends data
        ↓
What data should the client receive?

# That is where Response Models come in the picture

############# Difference between Reqest Model vs Response Model ##############

# Request Model : Fronted -> Backend
# Response Model : Backend -> Fronted

#example : 

class UserCreate(BaseMode):
    name: str
    email: str
    password: str

# so the fronted must send : 

{
    "name": "Samir",
    "email": "samir@gmail.com",
    "password": "mypassword123"
}


# Response Model

# Backend -> Fronted

class UserResponse(BaseModel):
    name: str
    email: str

# notice : password is not here


# So the complete Flow is : 

                REQUEST

Frontend
    │
    │ name
    │ email
    │ password
    ▼
UserCreate Model
    │
    ▼
Backend Logic


                RESPONSE

Backend Data
    │
    │ name
    │ email
    │ password
    ▼
UserResponse Model
    │
    │ Remove password
    ▼
Frontend


############## First Response Model ################

from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()

class UserCreate(BaseModel):
    name: str
    email: str
    password: str


class UserResponse(BaseModel):
    name: str
    email: str


# Now create the endpoint : 

@app.post("/users", response_model=UserResponse)

def create_user(user: UserCreate):
    return user

# Input -> user: UserCreate
# Output -> reponse_model = UserResponse


#########

from fastapi import FastAPI, status
from pydantic import BaseModel

app = FastAPI()

class UserCreate(BaseModel):
    name:str
    email: str
    password: str


class UserResponse(BaseModel):
    id: int
    name: str
    email: str

@app.post(
    "/users",
    status_code=status.HTTP_201_CREATED 
    response_model = UserResponse
)

def create_user(user: UserCreate):
    new_user = {
        "id" : 1,
        "name" : user.name
        "email" : user.email
        "password" : user.password
    }

    return new_user


# Final Response :

{
    "id" : 1,
    "name" : "Samir",
    "email" : "sam@gmail.com"
}

# this is reponse filtering


# Reponse Model don't only hide fields
# they also validate the data returned by your backend


################# Complete Example ##############

from fastapi import FastAPI,status
from pydantic import BaseModel

app = FastAPI()


# Request Model
class UserCreate(BaseModel):
    name: str
    email: str
    password: str


# Response Model
class UserResponse(BaseModel):
    id: int
    name: str
    email: str


# Temporary Data
users = [
    {
        "id": 1,
        "name": "Samir",
        "email": "samir@gmail.com",
        "password": "secret123"
    },
    {
        "id": 2,
        "name": "Rahul",
        "email": "rahul@gmail.com",
        "password": "secret456"
    }
]


# GET ALL USERS
@app.get(
    "/users",
    response_model=list[UserResponse]
)
def get_users():
    return users


# GET ONE USER
@app.get(
    "/users/{user_id}",
    response_model=UserResponse
)
def get_user(user_id: int):

    for user in users:
        if user["id"] == user_id:
            return user

    return {
        "id": 0,
        "name": "Not Found",
        "email": "Not Found"
    }


# CREATE USER
@app.post(
    "/users",
    status_code=status.HTTP_201_CREATED,
    response_model=UserResponse
)
def create_user(user: UserCreate):

    new_user = {
        "id": len(users) + 1,
        "name": user.name,
        "email": user.email,
        "password": user.password
    }

    users.append(new_user)

    return new_user


























