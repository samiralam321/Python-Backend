# Look at this endpoint : 


@app.get("/users/{user_id}")
def get_user(user_id: int):
    return {
        "message": "User found",
        "user_id": user_id
    }


# Even if we request : /users/99999
# Our API still says: 

{
    "message": "User found",
    "user_id": 999999
}

# but what if user 9999 does not exists?\

# Whenever a client sends a request : 

Client
   │
   │ Request
   ▼
Backend
   │
   │ Response
   ▼
Client

# The backend does not only send data, it also sends a status code

# For example : 

GET /users/101
Status Code : 200   # meaning - Request was sucessful


GET /users/999  
Status Code: 404   # meaning resource was not found


# So a reponse conceptually contains : 

Response
│
├── Status Code
├── Headers
└── Response Body


############### Cleaner way of using Status

#import : 

from fastapi import FastAPI, status 

@app.post("/users", status_code=status.HTTP_201_CREATED)

def create_user(user: User):
    return {
        "message" : "User created sucessfully",
        "user" : user
    }



### waht if data does not Exist : 

# suppose you temporarily store users in a dictionary 

users = {
    1: {
        "name": "Samir",
        "age": 21
    },

    2: {
        "name": "Rahul",
        "age": 22
    }
}


@app.get("/users/{user_id}")
def get_user(user_id : int):
    if user_id not in users:
        return {
            "message" : "user not found"
        }

    return users[user_id]


################## Using HTTPExecution ##################

#FastAPI gives us : HTTPExection

from fastapi import FastAPI, HTTPExecution

@app.get("/users/{user_id}")
def get_user(user_id: int):

    if user_id not in users:
        raise HTTPExecution(
            status_code=404,
            datail="User not Found"
        )

    return users[user_id]




############# GET + 404 ##################

from fastapi import FastAPI, HTTPException, status 

app = FastAPI()

users = {
    1:{
        "name" : "Samir",
        "age" : 21
    },
    2: {
        "name" : "Me",
        "age" : 22
    }
}

@app.get("/users/{user_id}")
def get_user(user_id: int):
    if user_id not in users:
        raise HTTPException(
            status_code = status.HTTP_404_NOT_FOUND
            detail="User not found"
        )

    return {
        "message" : "User found",
        "user" : users[user_id]
    }


################## POST Example with 201 ####################

from fastapi import FastAPI, status
from pydantic import BaseModel

app = FastAPI()

class Usr(BaseModel):
    name: str
    age: int
    email: str

@app.post("/users", status_cod=status.HTTP_201_CREATED)

def create_user(user : User):
    return {
        "message" : "User Created",
        "user" : user
    }


############## Real CRUD with Temporary Data ############


from fastapi import FastAPI,HTTPException,status
from pydantic import BaseModel

app = FastAPI()


class User(BaseModel):
    name: str
    age: int
    email: str


users = {
    1: {
        "name": "Samir",
        "age": 21,
        "email": "samir@gmail.com"
    },

    2: {
        "name": "Rahul",
        "age": 22,
        "email": "rahul@gmail.com"
    }
}


# READ ALL USERS
@app.get("/users")
def get_users():
    return users


# READ ONE USER
@app.get("/users/{user_id}")
def get_user(user_id: int):

    if user_id not in users:

        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="User not found"
        )

    return users[user_id]


# CREATE USER
@app.post(
    "/users/{user_id}",
    status_code=status.HTTP_201_CREATED
)
def create_user(user_id: int,user: User):

    if user_id in users:

        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail="User already exists"
        )

    users[user_id] = user.model_dump()

    return {
        "message": "User created successfully",
        "user": users[user_id]
    }


# DELETE USER
@app.delete(
    "/users/{user_id}",
    status_code=status.HTTP_204_NO_CONTENT
)
def delete_user(user_id: int):

    if user_id not in users:

        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="User not found"
        )

    del users[user_id]



# this line : users[user_id] = user.model_dump()

# as user is a Pydantic object 
# Example : 

User object

name = Samir
age = 21
email = samir@gmail.com

# but our dictionary stores normal Python dictionaries 

user.model_dump()
# converts the pydantic model into a dictionary






