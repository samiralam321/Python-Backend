# Complete GET One User Code

@app.get("/users/{user_id}")
def get_user(
    user_id: int,
    db = Depends(get_db)
):
    user = db.query(User).filter(User.id == user_id).first()
    if user is None:
        raise HTTPSException(
            status_code = 404,
            # status_code=status.HTTP_404_NOT_FOUND,  => It is more redable
            detail = "User not Found"
        )
    return user

#Complete POST Endpoint with Error Handling : 

@app.post(
    "/users",
    status_code=status.HTTP_201_CREATED
)

def create_user(
    user : UserCreate,
    db = Depends(get_db)
):

    new_user = User(
        name = user.name,
        age = user.age,
        email = user.email
    )

    db.add(new_user)
    db.commit()
    db.refresh(new_user)

    return new_user


# PUT Endpoint

@app.put("/users/{user_id}")
def update_user(
    user_id: int,
    updated_user: UserUpdate,
    db = Depends(get_db)
):

    user = db.query(User).filter(User.id == user_id).first()

    if user is None:
        raise HTTPException(
            status_code=404,
            detail="User not found"
        )

    user.name = updated_user.name
    user.age = updated_user.age
    user.email = updated_user.email

    db.commit()

    db.refresh(user)

    return user


# PATCH Endpoint 

@app.patch("/users/{user_id}")
def patch_user(
    user_id: int,
    updated_data: UserPatch,
    db = Depends(get_db)
):

    user = db.query(User).filter(User.id == user_id).first()

    if user is None:
        raise HTTPException(
            status_code=404,
            detail="User not found"
        )

    if updated_data.name is not None:
        user.name = updated_data.name

    if updated_data.age is not None:
        user.age = updated_data.age

    if updated_data.email is not None:
        user.email = updated_data.email

    db.commit()

    db.refresh(user)

    return user


#DELETE Endpoint 

@app.delete("/users/{user_id}")
def delete_user(
    user_id: int,
    db = Depends(get_db)
):

    user = db.query(User).filter(User.id == user_id).first()

    if user is None:
        raise HTTPException(
            status_code=404,
            detail="User not found"
        )

    db.delete(user)
    db.commit()

    return {
        "message": "User deleted successfully"
    }


# Almost every operation follows this pattern : 

Receive Request
      ↓
Get Path / Request Data
      ↓
Get Database Session
      ↓
Find User
      ↓
Does User Exist?
   ↙          ↘
 YES          NO
 ↓            ↓
Perform       404
Operation
 ↓
Commit if database changes
 ↓
Return Response


# Adding 201 to POST

@app.post(
    "/users",
    status_code=status.HTTP_201_CREATED
)
def create_user(
    user: UserCreate,
    db = Depends(get_db)
):

    new_user = User(
        name=user.name,
        age=user.age,
        email=user.email
    )

    db.add(new_user)
    db.commit()
    db.refresh(new_user)
    return new_user


# Adding 204 to DELETE

@app.delete(
    "/users/{user_id}",
    status_code=status.HTTP_204_NO_CONTENT
)
def delete_user(
    user_id: int,
    db = Depends(get_db)
):

    user = db.query(User).filter(User.id == user_id).first()

    if user is None:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="User not found"
        )

    db.delete(user)
    db.commit()


############ Complete Architecture ###################

CLIENT
   │
   │ HTTP Request
   ▼
FASTAPI ENDPOINT
   │
   │ Validates input
   ▼
PYDANTIC MODEL
   │
   │ Validated data
   ▼
SQLALCHEMY
   │
   │ Database operation
   ▼
SQLITE DATABASE
   │
   │ Result
   ▼
SQLALCHEMY
   │
   ▼
FASTAPI
   │
   │ JSON Response + Status Code
   ▼
CLIENT


##

from fastapi import FastAPI, Depends, HTTPException, status
from pydantic import BaseModel, ConfigDict
from typing import Optional

from sqlalchemy import create_engine, Column, Integer, String
from sqlalchemy.orm import sessionmaker, declarative_base, Session


app = FastAPI()


# --------------------------------
# DATABASE CONFIGURATION
# --------------------------------

DATABASE_URL = "sqlite:///./users.db"


engine = create_engine(
    DATABASE_URL,
    connect_args={
        "check_same_thread": False
    }
)


SessionLocal = sessionmaker(
    autocommit=False,
    autoflush=False,
    bind=engine
)


Base = declarative_base()


# --------------------------------
# DATABASE MODEL
# --------------------------------

class User(Base):
    __tablename__ = "users"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String)
    age = Column(Integer)
    email = Column(String, unique=True)


# Create database table

Base.metadata.create_all(bind=engine)


# --------------------------------
# DATABASE SESSION
# --------------------------------

def get_db():

    db = SessionLocal()

    try:
        yield db

    finally:
        db.close()


# --------------------------------
# PYDANTIC MODELS
# --------------------------------

class UserCreate(BaseModel):
    name: str
    age: int
    email: str


class UserUpdate(BaseModel):
    name: str
    age: int
    email: str


class UserPatch(BaseModel):
    name: Optional[str] = None
    age: Optional[int] = None
    email: Optional[str] = None


class UserResponse(BaseModel):
    id: int
    name: str
    age: int
    email: str

    model_config = ConfigDict(from_attributes=True)


# --------------------------------
# CREATE USER
# --------------------------------

@app.post(
    "/users",
    response_model=UserResponse,
    status_code=status.HTTP_201_CREATED
)
def create_user(
    user: UserCreate,
    db: Session = Depends(get_db)
):

    new_user = User(
        name=user.name,
        age=user.age,
        email=user.email
    )

    db.add(new_user)
    db.commit()
    db.refresh(new_user)

    return new_user


# --------------------------------
# GET ALL USERS
# --------------------------------

@app.get(
    "/users",
    response_model=list[UserResponse]
)
def get_users(
    db: Session = Depends(get_db)
):

    users = db.query(User).all()
    return users


# --------------------------------
# GET ONE USER
# --------------------------------

@app.get(
    "/users/{user_id}",
    response_model=UserResponse
)
def get_user(
    user_id: int,
    db: Session = Depends(get_db)
):

    user = db.query(User).filter(
        User.id == user_id
    ).first()

    if user is None:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="User not found"
        )

    return user


# --------------------------------
# PUT - COMPLETE UPDATE
# --------------------------------

@app.put(
    "/users/{user_id}",
    response_model=UserResponse
)
def update_user(
    user_id: int,
    updated_user: UserUpdate,
    db: Session = Depends(get_db)
):

    user = db.query(User).filter(
        User.id == user_id
    ).first()

    if user is None:

        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="User not found"
        )

    user.name = updated_user.name
    user.age = updated_user.age
    user.email = updated_user.email

    db.commit()

    db.refresh(user)

    return user


# --------------------------------
# PATCH - PARTIAL UPDATE
# --------------------------------

@app.patch(
    "/users/{user_id}",
    response_model=UserResponse
)
def patch_user(
    user_id: int,
    updated_data: UserPatch,
    db: Session = Depends(get_db)
):

    user = db.query(User).filter(
        User.id == user_id
    ).first()

    if user is None:

        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="User not found"
        )

    update_data = updated_data.model_dump(
        exclude_unset=True
    )

    for key,value in update_data.items():

        setattr(user,key,value)

    db.commit()

    db.refresh(user)

    return user


# --------------------------------
# DELETE USER
# --------------------------------

@app.delete(
    "/users/{user_id}",
    status_code=status.HTTP_204_NO_CONTENT
)
def delete_user(
    user_id: int,
    db: Session = Depends(get_db)
):

    user = db.query(User).filter(
        User.id == user_id
    ).first()

    if user is None:

        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="User not found"
        )

    db.delete(user)

    db.commit()