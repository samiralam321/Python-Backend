from fastapi import APIRouter, HTTPException
from database import connection, cursor
from schemas import UserCreate, UserUpdate

#router = APIRouter()  # it represents a collection of routes

#creating a Router 

router = APIRouter(
    prefix="/users"
)


# previously we had app = FastAPI()
# the app represents the complete FastAPI application 


# previosly we had
# @app.get("/users")
# def get_users():
#     return []



# now

@router.get("/")
def get_users():
    return {
        "message" : "Users router is working"
    }


# @app
#  ↓
# Complete application


# @router
#    ↓
# Routes belonging to one group


@router.post("/")
def create_user(user: UserCreate):

    cursor.execute(
        """
        INSERT INTO users(name,age,email)
        VALUES(?,?,?)
        """,

        (
            user.name
            user.age
            user.email
        )
    )
    connection.commit()

    return {
        "message": "User created successfully"
    }


# Read All Users (GET)

@router.get("/")
def get_users():
    cursor.execute(
        """
        SELECT * FROM users
        """
    )

    rows = cursor.fetchall()

    users = []

    for row in rows:
        users.append(dict(row))

    return users



# Get one User

@router.get("/{user_id}")
def get_user(user_id: int):

    cursor.execut(
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
        

######## Update User #######

@router.put("/{user_id}")
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


####### Delete User ########

@router.delete("/{user_id}")
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



# The problems with many routes : 

#imagine your backend later has : 

/users/
/products/
/orders/
/auth/
/payments/

# swagger may show many endpoits together 


Users
    POST /users/
    GET /users/
    GET /users/{user_id}
    PUT /users/{user_id}
    DELETE /users/{user_id}


# Later : 

Products
    POST /products/
    GET /products/


# this grouping is done using : tags 


# so we have to add a tag to routers :

# currently  

router = APIRouter(
    prefix = "/users"
)

# change it to

router = APIRouter(
    prefix = "/users",
    tags=["Users"]
)

# understand the prefix : 

prefix = "/users"

# suppose you  write : 

@router.get("/")
# the final URL becomes : 
/users/

# Suppose 

@router.get("/{user_id}")

# the final URL becomes : 

/users/{user_id}



# so, tags helps organize Swagger


########### Improved Code ##########

from fastapi import APIRouter, HTTPExecution
from database import connection, curosor
from schemas import UserCreate, UserUpdate

router = APIRouter (
    prefix = "/users",
    tags=["users"]
)






