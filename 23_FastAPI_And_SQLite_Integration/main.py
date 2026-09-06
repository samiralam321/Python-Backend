# The Problem With Our Previous API

# Earlier, we had something like:

# users = []

# or:

# products = []

# When you restart the server:

# Server Stops
#      ↓
# Python variables disappear
#      ↓
# Data lost ❌


# Now:

# Client
#    ↓
# FastAPI
#    ↓
# SQLite Database
#    ↓
# Data Stored Permanently ✅



###### FastAPI + Database

from fastapi import FastAPI
import sqlite3

app = FastAPI()

connection = sqlite3.connect("users.db")
cursor = connection.cursor()

cursor.execute("""
CREATE TABLE IF NOT EXISTS users(
    id INTEGER PRIMARY KEY,
    name TEXT,
    age INTEGER,
    email TEXT
)
""")

connection.commit()

@app.get("/")
def hhome():
    return {
        "message" : "FastAPI + SQLite is working" 
    }


############# First POST Endpoint #####################

@app.post("/users")
def create_user(user: UserCreate):
    cursor.execute(
        """
        INSERT INTO users(name,age,email)
        VALUES(?,?,?)
        """,

        (
            user.name,
            user.age,
            user.email
        )
    )
    connection.commit()

    return {
        "message" : "User Created"
    }


# complete code

from fastapi import FastAPI
from pydantic import BaseModel, Emailstr
import sqlite3

app = FastAPI()

connection = sqlite3.connect("user.db")
cursor = connection.cursor()

cursor.execute("""
CREATE TABLE IF NOT EXISTS users(
    id INTEGER PRIMARY KEY,
    name TEXT,
    age INTEGER,
    email TEXT
)
""")

connection.commit()

class UserCreate(BaseModel):
    name: str
    age: int
    email: EmailStr

@app.get("/")
def home():
    return {
        "message" : "FastAPI + SQLite is working"
    }

@app.post("/users")
def create_user(user: UserCreate):
    cursor.execute(
        """
        INSERT INTO users(name,age,email)
        VALUES(?,?,?)
        """,
        (
            user.name,
            user.age,
            user.email
        )
    )

    connection.commit()   # permanently saves it.

    return {
        "message" : "user create succesfully"
    }
    

################## Reading Data from the Database ##################

# We will learn 

GET /users
    ↓
SELECT * FROM users
    ↓
fetchall()
    ↓
Convert database data
    ↓
Return JSON


# 

@app.get("/users")
def get_users():

    cursor.execute("""
    SELECT * FROM users
    """)

    users = cursor.fetchall()  # get all rows 
    return users


# Converting Rows into Dictionaries 

@app.get("/users")
def get_users():
    cursor.execute("""
    SELECT * FROM users
    """)

    rows = cursor.fetchall()

    users = []

    for row in rows:
        user = {
            "id" : row[0],
            "name" : row[1],
            "age" : row[2],
            "email" : row[3]
        }

        users.append(user)
    
    return users


############ SQLite Row Factory ############

connection = sqlite3.connect("users.db")

connection.row_factory = sqlite3.Row

cursor = connection.cursor()


# Get all users using ROW

@app.get("/users")
def get_users():

    cursor.execute("""
    SELECT * FROM users
    """)

    rows = cursor.fetchall()

    users = []

    for row in rows:

        users.append(
            dict(row)
        )

    return users


######### Complete Code #######

from fastapi import FastAPI
from pydantic import BaseModel,EmailStr
import sqlite3


app = FastAPI()


connection = sqlite3.connect("users.db")

connection.row_factory = sqlite3.Row

cursor = connection.cursor()


cursor.execute("""
CREATE TABLE IF NOT EXISTS users(
    id INTEGER PRIMARY KEY,
    name TEXT,
    age INTEGER,
    email TEXT
)
""")


connection.commit()


class UserCreate(BaseModel):
    name: str
    age: int
    email: EmailStr


@app.get("/")
def home():

    return {
        "message": "FastAPI + SQLite is working"
    }


@app.post("/users")
def create_user(user: UserCreate):

    cursor.execute(
        """
        INSERT INTO users(name,age,email)
        VALUES(?,?,?)
        """,
        (
            user.name,
            user.age,
            user.email
        )
    )

    connection.commit()

    return {
        "message": "User created successfully"
    }


@app.get("/users")
def get_users():

    cursor.execute("""
    SELECT * FROM users
    """)

    rows = cursor.fetchall()

    users = []

    for row in rows:

        users.append(
            dict(row)
        )

    return users



############## Updating Users ################

@app.put("/users/{user_id}")
def update_user(user_id: int,user: UserUpdate):

    cursor.execute(
        """
        UPDATE users
        SET name=?,age=?,email=?
        WHERE id=?
        """,
        (
            user.name,
            user.age,
            user.email,
            user_id
        )
    )

    connection.commit()

    return {
        "message": "User updated successfully"
    }


# what if user not exist  ? 

@app.put("/users/{user_id}")
def update_user(user_id: int,user: UserUpdate):

    cursor.execute(
        """
        SELECT * FROM users
        WHERE id=?
        """,
        (user_id,)
    )

    existing_user = cursor.fetchone()


    if existing_user is None:

        raise HTTPException(
            status_code=404,
            detail="User not found"
        )


    cursor.execute(
        """
        UPDATE users
        SET name=?,age=?,email=?
        WHERE id=?
        """,
        (
            user.name,
            user.age,
            user.email,
            user_id
        )
    )


    connection.commit()


    return {
        "message": "User updated successfully"
    }


# Full Updated Code 

from fastapi import FastAPI,HTTPException
from pydantic import BaseModel,EmailStr
import sqlite3


app = FastAPI()


connection = sqlite3.connect("users.db")

connection.row_factory = sqlite3.Row

cursor = connection.cursor()


cursor.execute("""
CREATE TABLE IF NOT EXISTS users(
    id INTEGER PRIMARY KEY,
    name TEXT,
    age INTEGER,
    email TEXT
)
""")


connection.commit()


class UserCreate(BaseModel):
    name: str
    age: int
    email: EmailStr


class UserUpdate(BaseModel):
    name: str
    age: int
    email: EmailStr


@app.get("/")
def home():

    return {
        "message": "FastAPI + SQLite is working"
    }


@app.post("/users")
def create_user(user: UserCreate):

    cursor.execute(
        """
        INSERT INTO users(name,age,email)
        VALUES(?,?,?)
        """,
        (
            user.name,
            user.age,
            user.email
        )
    )

    connection.commit()

    return {
        "message": "User created successfully"
    }


@app.get("/users")
def get_users():

    cursor.execute("""
    SELECT * FROM users
    """)

    rows = cursor.fetchall()

    users = []

    for row in rows:

        users.append(
            dict(row)
        )

    return users


@app.get("/users/{user_id}")
def get_user(user_id: int):

    cursor.execute(
        """
        SELECT * FROM users
        WHERE id=?
        """,
        (user_id,)
    )

    user = cursor.fetchone()

    if user is None:

        raise HTTPException(
            status_code=404,
            detail="User not found"
        )

    return dict(user)


@app.put("/users/{user_id}")
def update_user(user_id: int,user: UserUpdate):

    cursor.execute(
        """
        SELECT * FROM users
        WHERE id=?
        """,
        (user_id,)
    )

    existing_user = cursor.fetchone()


    if existing_user is None:

        raise HTTPException(
            status_code=404,
            detail="User not found"
        )


    cursor.execute(
        """
        UPDATE users
        SET name=?,age=?,email=?
        WHERE id=?
        """,
        (
            user.name,
            user.age,
            user.email,
            user_id
        )
    )


    connection.commit()


    cursor.execute(
        """
        SELECT * FROM users
        WHERE id=?
        """,
        (user_id,)
    )


    updated_user = cursor.fetchone()


    return {
        "message": "User updated successfully",
        "user": dict(updated_user)
    }


############ Delete ENdpint ########

@app.delete("/users/{user_id}")
def delete_user(user_id: int):  # fastapi extracts the ID

    cursor.execute(   #Step 2 : Check the database
        """
        SELECT * FROM users
        WHERE id=?
        """,
        (user_id,)
    )

    user = cursor.fetchone()


    if user is None:  # Step 3 : Check if the user exists

        raise HTTPException(
            status_code=404,
            detail="User not found"
        )


    cursor.execute(  #Step 4 : Delete the user
        """
        DELETE FROM users
        WHERE id=?
        """,
        (user_id,)
    )


    connection.commit()  # Step 5 : Commit -> The deletion is permanently saved


    return {
        "message": "User deleted successfully"
    }



############## Final CURD Code ##########

from fastapi import FastAPI,HTTPException
from pydantic import BaseModel,EmailStr
import sqlite3


app = FastAPI()


connection = sqlite3.connect("users.db")

connection.row_factory = sqlite3.Row

cursor = connection.cursor()


cursor.execute("""
CREATE TABLE IF NOT EXISTS users(
    id INTEGER PRIMARY KEY,
    name TEXT,
    age INTEGER,
    email TEXT
)
""")


connection.commit()


class UserCreate(BaseModel):
    name: str
    age: int
    email: EmailStr


class UserUpdate(BaseModel):
    name: str
    age: int
    email: EmailStr


@app.get("/")
def home():

    return {
        "message": "FastAPI + SQLite is working"
    }


@app.post("/users")
def create_user(user: UserCreate):

    cursor.execute(
        """
        INSERT INTO users(name,age,email)
        VALUES(?,?,?)
        """,
        (
            user.name,
            user.age,
            user.email
        )
    )

    connection.commit()

    return {
        "message": "User created successfully"
    }


@app.get("/users")
def get_users():

    cursor.execute("""
    SELECT * FROM users
    """)

    rows = cursor.fetchall()

    users = []

    for row in rows:

        users.append(dict(row))

    return users


@app.get("/users/{user_id}")
def get_user(user_id: int):

    cursor.execute(
        """
        SELECT * FROM users
        WHERE id=?
        """,
        (user_id,)
    )

    user = cursor.fetchone()

    if user is None:

        raise HTTPException(
            status_code=404,
            detail="User not found"
        )

    return dict(user)


@app.put("/users/{user_id}")
def update_user(user_id: int,user: UserUpdate):

    cursor.execute(
        """
        SELECT * FROM users
        WHERE id=?
        """,
        (user_id,)
    )

    existing_user = cursor.fetchone()

    if existing_user is None:

        raise HTTPException(
            status_code=404,
            detail="User not found"
        )

    cursor.execute(
        """
        UPDATE users
        SET name=?,age=?,email=?
        WHERE id=?
        """,
        (
            user.name,
            user.age,
            user.email,
            user_id
        )
    )

    connection.commit()

    cursor.execute(
        """
        SELECT * FROM users
        WHERE id=?
        """,
        (user_id,)
    )

    updated_user = cursor.fetchone()

    return {
        "message": "User updated successfully",
        "user": dict(updated_user)
    }


@app.delete("/users/{user_id}")
def delete_user(user_id: int):

    cursor.execute(
        """
        SELECT * FROM users
        WHERE id=?
        """,
        (user_id,)
    )

    user = cursor.fetchone()

    if user is None:

        raise HTTPException(
            status_code=404,
            detail="User not found"
        )

    cursor.execute(
        """
        DELETE FROM users
        WHERE id=?
        """,
        (user_id,)
    )

    connection.commit()

    return {
        "message": "User deleted successfully"
    }