# so we already know how to interact with the SQLite using raw SQL

cursor.execute("""
INSERT INTO users(name,age,email)
VALUES(?,?,?)
""",
(
    user.name,
    user.age,
    user.email
))

# To get users : 

cursor.execute("""
SELECT * FROM users
""")

users = cursor.fetchall()

# To update : 

cursor.execute("""
UPDATE users
SET name=?, age=?, email=?
WHERE id=?
""")

# this approach is called : Raw SQL





############ ORM (Object Realational Mapping) ####################

# Object, in Python 

user = User(
    name="Samir",
    age=22,
    email="sam@gmail.com"
)


# Realtional Database
# SQLite is realtional database
# it stores data in tables 

############ Mapping #################

# ORM creates a connection between : 

Python Object -> Database Table 

# The IMP Definition :

# ORM allows us to work with database data
# using programming language objects instead of writing SQL 
# queries manually


######### Without ORM #######

cursor.execute("""
INSERT INTO users(name,age,email)
VALUES(?,?,?)
""",
(
    "Samir",
    22,
    "samir@example.com"
))

# we directly tell the database : INSERT this data into the users table 

############ With ORM ###########

user = User(
    name="Samir",
    age=22,
    email="sam@gmail.com"
)

db.add(user)
db.commit()

# so the architecture becomes : 


Your Python Code
       ↓
Python Object
       ↓
SQLAlchemy ORM
       ↓
SQL Query generated automatically
       ↓
SQLite Database


# note that : SQLAlchemy internally generates SQL

for example, when you write : 

db.add(user)
db.commit()

SQLAlchemy may internally execute something conceptually like : 

ISNERT INTO users(name,age,email)
VALUES('Samir', 22, 'sam@gmail.com')

# so ORM acts like a translator : 

Python
   ↓
SQLAlchemy
   ↓
  SQL
   ↓
Database


########### what is SQLAlchemy ##########

> python library
> help python application to communicate with database


########## The Biggest Difference ###########

# Raw SQL

think in terms of : 

Tables
Columns
SQL Queries
Rows


# ORM 

think in terms of : 

Python Classes
Python Objects
Attributes
Methods


########### with SQLAlchemy : you can define a class that represents a database table ###############

class User(Base):
    id = Column(Integer)
    name = Column(String)
    age = Column(Integer)
    email = Column(String)



# Remember : 

Python Class
       ↓
Database Table


Python Object
       ↓
Database Row


Python Attribute
       ↓
Database Column


# The ORM mapping Table : 

| Python    | Database |
| --------- | -------- |
| Class     | Table    |
| Object    | Row      |
| Attribute | Column   |


##############################################################################################

from sqlalchemy import create_engine
from sqlalchemy.orm import declarative_base

DATABASE_URL = "sqlite:///users.db"
# the above line means : I want to use SQLite and my database file is users.db

engine = create_engine(DATABASE_URL)
print("Database engine creates sucessfully")

# so engine is the bridge between Python and SQLite

Python
   │
   ▼
engine
   │
   ▼
SQLite

# so engine communicate with the database


####################################################################

from sqlalchemy import create_engine
from sqlalchemy.orm import declarative_base
from sqlalchemy import create_engine, Column, Integer, String

DATABASE_URL = "sqlite:///users.db"

engine = create_engine(DATABASE_URL)
Base = declarative_base()

print("Database engine created successfully")


class User(Base):
    __table_name__ =  "users"
    id = Column(Integer, primary_key=True)  #create a database column, Column data type is Integer
    name = Column(String) # create the name Column
    age = Column(Integer)
    email = Column(String)

Base.metadata.create_all(bind=engine)



# means : 

Column name → id
Type        → INTEGER
Primary Key → Yes


#### Base : Creates the parent/base for our ORM models 



Base.metadate.create_all()  # create_all() means : If table does not exits -> Create it,    If the table already exists -> Do nothing

# looks at all models connected to Base
# check theire datable defintions
# create the tables if they do not exists


################## SQLAlchemy Sesssion #############################

# so we have creates a Python object, now questions is how will this Python object reach  to the atabase

# Create object
# Add object to session
# Commit session 

from sqlalchemy.orm import declarative_base, sessionmaker
from sqlalchemy import create_engine,Column,Integer,String
from sqlalchemy.orm import declarative_base,sessionmaker

# so sessionmaker -> Creates database sessions 

SessionLocal = sessionmaker(bind=engine)

db = SessionLocal()  # it creates a new session


############ Our Code So Far ####################

from sqlalchemy import create_engine,Column,Integer,String
from sqlalchemy.orm import declarative_base,sessionmaker


DATABASE_URL = "sqlite:///users.db"
engine = create_engine(DATABASE_URL)
Base = declarative_base()


class User(Base):
    __tablename__ = "users"

    id = Column(Integer,primary_key=True)
    name = Column(String)
    age = Column(Integer)
    email = Column(String)


Base.metadata.create_all(bind=engine)

SessionLocal = sessionmaker(bind=engine)  #mening : Creates a session factory

db = SessionLocal()  # create an actual database session













