# Database : A database stores information even after your program stops 

# SQL Strcutured Query Language) : It is language to communicate with relational database

# Example : 

SELECT * FROM users; # give me all users 
SELECT * FROM users WHERE age > 20;


Python Backend
      ↓
     SQL
      ↓
Database



# What is Relational Database ? 

# The most common beginner-friendly way to understand it is:
# A relational database stores data in tables.
# Imagine an Excel spreadsheet : 

users

+----+--------+-------------------+-----+
| id | name   | email             | age |
+----+--------+-------------------+-----+
| 1  | Samir  | samir@gmail.com   | 21  |
| 2  | Rahul  | rahul@gmail.com   | 22  |
| 3  | Aman   | aman@gmail.com    | 20  |
+----+--------+-------------------+-----+

# a databse contain many tables 


################## Your First SQL Table #############

# Suppose we want a users table

CREATE TABLE users (
    id INTEGER,
    name VARCHAR(100),
    age INTEGER,
    email VARCHAR(255)
);

# Datatypes : 

INTEGER
→ whole numbers

VARCHAR
→ text with a length limit

TEXT
→ text

BOOLEAN
→ true/false

DECIMAL
→ precise decimal numbers

DATE
→ date

TIMESTAMP
→ date + time



age INTEGER
age VARCHAR(100)
price DECIMAL(10,2)
is_active BOOLEAN 

## INSERT 

# WE HAVE A TABLE 

CREATE TABLE users (
    id INTEGR,
    name VARCHAR(100),
    age INTEGER,
    email VARCHAR(255)
);

# This creates four columns 

users
│
├── id
├── name
├── age
└── email

######### INSERT : Adding data

CREATE TABLE users (
    id INTEGER,
    name VARCHAR(100),
    age INTEGER
);

# we can add a user : 

INSERT INTO users(id, name, age)
VALUES (1, 'Samir', 21);


# Now : 

id | name  | age
---|-------|----
1  | Samir | 21
2  | Rahul | 22


########### SELECT : retriving data ###########

# To retrive everyting : 

SELECT * from users;   #  * means : all columns

# you can request only specifc columns : 

SELECT name,age FROM users; 

Result : 

Samir | 21
Rahul | 22

So, SELECT means : Retrive data 

## WHERE Filtering : 

SELECT * FROM users
WHERE name = "Samir"; 

SELECT * FROM users
WHERE age > 20; 

# Mental Mode : 

SELECT
   ↓
Get data

WHERE
   ↓
Filter it


SELECT * FROM users
WHERE age >= 21; 

# means: Give me suers whose age is at least 21


######## Combining Conditions 

# you can use AND : 

SELECT * FROM users
WHERE age > 20
AND name = 'Samir'; 

# Both conditions must be true 

## OR => Either condition can be true : 

SELECT * FROM users
WHERE age = 20
OR age = 21; 


# UPDATE 

UPDATE users
SET age = 22
WHERE id = 1; 


# Note : 

UPDATE users
SET age = 22; # It can update every users


######## DELETE 

# To delete user 1 : 

DELETE FROM users
WHERE id = 1; 

# Careful : 
DELETE FROM users;   # Can delete all rows


############## CRUD Connection ###########

CREATE  -> INSERT
READ    -> SELECT
UPDATE  -> UPDATE
DELETE  -> DELETE


# Connect that to HTTP:

API                  SQL

POST    →            INSERT
GET     →            SELECT
PUT     →            UPDATE
DELETE  →            DELETE




######## Primary Key : 

# Consider : 

id | name
---|------
1  | Samir
2  | Rahul
3  | Aman

# The id uniquely identifies each user : 
# this is a primary key.

# we can define it like this : 

CREATE TABLE users (
    id INTEGER PRIMARY KEY,
    name VARCHAR(100),
    age INTEGER
); 

# id -> unique identifier for a row
# without a unique identifer, it becomes difficult to reliably distinguish records


# We can automatically gernerates the IDs

# For PostgreSQL, one common approach is: 

CREATE TABLE users (
    id INTEGER GENERATED ALWAYS AS IDENTIFY PRIMARY KEY,
    name VARCHAR (100) NOT NULL,  # means every user must have name 
    age INTEGER
)

INSERT INTO users (name, age)
VALUES ('Samir', 21); 

# And the database generates the ID


######### NOT NULL

# Suppose every user must have a name 

name VARCHAR (100) NOT NULL


####### UNIQUE

# every email should be unique


########### Constraints #########

Things like : 

Primary Key
Foregin Key
Not NULL
Unique 

are called constraints 

# their job is to help keep invalid or inconsistent data out of the database



############## Foreign Keys ############

users

id | name
---|------
1  | Samir
2  | Rahul


# and another table : 

orders

id | user_id | product
---|---------|---------
1  | 1       | Laptop
2  | 1       | Mouse
3  | 2       | Keyboard


# Here 

orders.user_id   refers to users.id
# that is foreign key : 

# we can define it like : 

CREATE TABLE orders (
    id INTEGER PRIMARY KEY,
    user_id INTEGER,
    prodcut VARCHAR(100),

    FOREIGN KEY (user_id)
    REFERENCE users(id)
)

# now the database knows that the order belongs to a user : 


########## one to Many relationship

# a vary common realtionship in one to many :

# one user can place many orders 

Samir
 ├── Order 1
 ├── Order 2
 └── Order 3

The database represntation is : 

users -> orders 

one user -> many orders


one to one 
one to many
many to many 

# but one to many is espeicially important to understand first


########### JOIN #########

# suppose we have 

users

id   name
1    Samir
2    Rahul

and 

orders

id | user_id | product
---|---------|---------
1  | 1       | Laptop
2  | 1       | Mouse
3  | 2       | Keyboard


# now we want : 

Samir -> Laptop
Samir -> Keyboard
Rahul -> Keyboard 

this info is split between two tables, so we use JOIN

SELECT users.name, orders.product
FROM users
JOIN orders
ON user.id = orders.user_id; 

# Result:

name  | product
------|--------
Samir | Laptop
Samir | Mouse
Rahul | Keyboard


############# Normalization ############

For now, understand its main purpose : 

> Avoid unnecessary duplicate data.
> Keep information organized.
> Represent relationships properly.

for example, instead of repetedly storing : 

Samir | samir@gmail.com | Laptop
Samir | samir@gmail.com | Mouse
Samir | samir@gmail.com | Keyboard


# we can store user informstion in users and order information in orders, and then connect them 

##################### Indexes ###############

# suppose database contains 10M users
# nd u frequently search : 

SELECT * FROM users
WHERE email = 'sam@gmai.com'; 


# an index can help the databse find the matching data faster


##

Without index

10 million rows
      ↓
Search many rows
      ↓
Potentially slower


With index

Index
  ↓
Locate matching data efficiently
  ↓
Retrieve row


# For Examples :

CREATE INDEX idx_users_email
ON users(email)

# but indexes are not free, they consume storage and also add overhead to writes,
# so you don't simply index every column



# Connect SQL with Python 

Python Backend
      ↓
   SQL Query
      ↓
   Database
      ↓
   Query Result
      ↓
     Python


# python might construct / executre a query such as : 

query = """
SELECT * FROM users
WHERE age > 20; 
"""


######## SQLite with Python ###########

import sqlite3

# create a database

import sqlite3
connection = sqlite3.connect("users.db")
cursor = connection.cursor()



# Creating a table through Python 

import sqlite3

connection = sqlite3.connect("users.db")
cursor = connection.cursor()

cursor.execute("""
CREATE TABLE IF NOT EXISTS users (
    id INTEGER PRIMARY KEY,
    name TEXT NOT NULL,
    age INTEGER
""")

connection.commit()  # runs SQL
connection.close()  # save database changes


######### Reading data from Python #######

cursor.execute("SELECT * FROM users")
users = cursor.fetchall()  # retrived all returned rows
print(users)

# For a single row use : cursor.fetchone()


########## Mini Program ########

import sqlite3

connection = sqlite3.connect("users.db")
cursor = connection.cursor()

cursore.execute ("""
CREATE TABLE IF NOT EXISTS users (
    id INTEGER PRIMARY KEY,
    name TEXT NOT NULL,
    age INTEGER
)
""")

connection.commit()
cursor.execute("SELECT * FROM users")

users = cursor.fetchall()


for user in users :
    print(user)

connection.close()

# the database remains after your program ends 






























































































