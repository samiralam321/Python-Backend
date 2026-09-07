from fastapi import FastAPI
from routers import users
from database import connection,cursor
from schemas import UserCreate,UserUpdate


app = FastAPI(
   title = "Professional FastAPI Proejct",
   description="A simple user CRUD API build using FastAPI and SQLite"
   version = "1.0.0"
)


@app.get("/")
def home():

    return {
        "message": "Professional FastAPI Project"
    }

app.include_router(users.router)



# the request travels like this : 

CLIENT
   ↓
main.py
   ↓
app.include_router()
   ↓
routers/users.py
   ↓
@router.post("/")
   ↓
UserCreate
   ↓
schemas.py
   ↓
Validation successful
   ↓
database.py
   ↓
cursor.execute()
   ↓
users.db
   ↓
connection.commit()
   ↓
Response


######## you can also descripbe what each endpoint does : 

@router.post(
   "/",
   summary="Create a new user"
)


# now Swagger will show : 

POST /users/

#Create a new user

@router.get(
   "/{user_id}",
   summary="Get a user by ID"
)


# Update : 

@router.put(
   "/{user_id}"
   summary="Update a user"
)

# Delete

@router.delete(
   "/{user_id}",
   summary="Delte a user"
)


#### Router Decorator Should look like this : 

@router.post(
   "/",
   summary="Create a new user"
)

def create_user(user : UserCreate)



@router.get(
   "/",
   summary="Get all users"
)
def get_users():

@router.get(
   "/{user_id}",
   summary="Get a user by ID"
)

def get_user(user_id : int):




# PUT

@router.delete(
   "/{user_id}",
   summary="Delete a user"
)

def delete_user(user_id : int):




















