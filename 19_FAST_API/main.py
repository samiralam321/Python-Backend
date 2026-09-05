# FastAPI is a Python framework used to build 

REST APIs
Backend Applications 
Web Services

# with fastapi we can create something like :

@app.get("/")

def home():
    return {"message" : "Hello world!"}

# and your backend creates an API endpoint

# when somwone vists :  /
# they recives : 

{
    "message " : "hello world "
}


# The complete architecture 

Frontend
    ↓
HTTP Request
    ↓
FastAPI
    ↓
Python Logic
    ↓
Database
    ↓
FastAPI
    ↓
JSON Response
    ↓
Frontend

#fastapi sits between the fronted and your python backend logic


# what is Uvicorn ? 

FastAPI = Backend framework
Uvicorn = Server that runs it

# your first fastapi program 

from fastapi import FastAPI

app = FastAPI()  # creates a fastapi application object



# creating endpoint
from fastapi import FastAPI

app = FastAPI()

@app.get("/")
def home():
    return {"message" : "Hello Samir"}

# means : when someone makes a get request to "/" run the function below

"/" => represent a path or route, it represent the root endpoint

so when someone visits : /
fastapi runs : def home():

# fasapi automatically converts the python dictionary into json


# Multiple Endpoints : 

from fastapi import FastAPI

app = FastAPI()

@app.get("/")
def home():
    return {
        "message" : "welcome to my backend"
    }

@app.get("/about")
def about():
    return {
        "message" : "this is the about page"
    }


@app.get("/users")
def get_users():
    return {
        "users" : [
            "Samir",
            "Rahul",
            "me"
        ]
    }


# how the above code is working : 

Client
   │
   │ GET /users
   ▼
FastAPI
   │
   ▼
get_users()
   │
   ▼
Python executes
   │
   ▼
return dictionary
   │
   ▼
FastAPI converts to JSON
   │
   ▼
Client receives response


# So 

FastAPI
   ↓
Creates backend APIs

app = FastAPI()
   ↓
Creates your backend application

@app.get("/")
   ↓
Creates a GET endpoint

def function()
   ↓
Runs when the request arrives

return dictionary
   ↓
FastAPI sends JSON response

uvicorn main:app --reload
   ↓
Runs your backend server


# so above we are creating fixed endpoints 

# now we will create dynamic enpoints 

################## FastAPI : path Paramters and Query Paramters ###################

# what is the problem with the fixed URL's
# suppose i have 1000 users and every user has an ID 

# you want an API to get a specific users 
# so u could write like this :

@app.get("/users/1")
def uder_one():
    return {"name" : "Samir"}

@app.get("/users/2")
def user_two():
    return {"name" : "Rahul"}

# obv we can't do this for 1000 users, instead we do, 

/users/{user_id} #called dynamic route

# so {user_id} is a path paramters

# First path paramters

from fastapi import FastAPI

app = FastAPI()

@app.get("/users/{user_id}")
def get_user(user_id):
    return {
        "user_id" : user_id
    }


# it will return string type of user_id like "101"

# so we will :Path Paramters With Type Hints

@app.get("/users/{user_id}")
def get_user(user_id: int):
    return {
        "user_id" : user_id
    }


# now the user_id must be an integer




######### Multiple Path Parameters ############

@app.get("/users/{user_id}/posts/{post_id}")

def get_post(user_id: int, post_id:int):
    return {
        "user_id" : user_id,
        "post_id" : post_id
    }


#Note that : URL Paramters should be same as Function paramters name


# now visit : /users/10/posts/10
you may get :

user_id = 10
post_id = 25


# Exmple : 

@app.get("/products/{product_id}")
def get_product(product_id: int)


########### Query Paramters ###############

/products?category=laptop

#mean : give me products where category is laptop

# this url has two parts : /products and second is ?category=laptop


Query paramters are often used for : 

Searching
Filtering
Sorting
Pagination 


# query paramters examples : 

@app.get("/products")
def get_products(catagory):   # here category is a query paramter
    return {
        "category" : category
    }


# query paramters with type hint

@app.get("/products")
def get_products(category: str):
    return {
        "category" : category
    }

############# Multiple Query Paramters #########

@app.get("/products")

def get_products(
    category: str,
    min_roce: int
):
    return{
        "category" : category,
        "min_price" : min_price
    }


# REPONSE : 

{
    "category" : "laptop",
    "min_price": 50000
}



############### Required vs Optional Query Paramters ################

def get_products(catagory: str = None):

#Noe : /products works and also 
/products?category=laptop also works

@app.get("/products")
def get_products(category:str = None):
    return {
        "category" : category
    }



# Optional Type Hints : The Better Way

# you can explicity say that a value can either be:

str or None

# in Modern Python 

@app.get("/products")

def get_products(category:str | None = None):
    return {
        "category" : category
    }

# this means : category can be string or None


########### Path and Query Paramters ###########

Path paramters : /users/101   or /users/{user_id}
Query Parameter : /users?age=21

############ Combining Path and Query Paramters ############

@app.get("/users/{user_id}/posts")

def get_posts(
    user_id : int,
    published: bool = True
):

    return{
        "user_id" : user_id,
        "published" : published
    }


@app.get("/users/{user_id}/posts")

def get_posts(
    user_id:int,
    published: bool = True
):
    return {
        "user_id" : user_id,
        "published" : published
    }


/users/101/posts?published=false
       ↑              ↑
       │              │
 Path Parameter    Query Parameter



@app.get("/products/{product_id}")
def get_product(
    product_id: int,
    include_reviews: bool = False
):

   return {
       "product_id" : product_id,
       "include_reviews" : include_reviews
   }


/products/10

returns : 

{
    "product_id" : 10,
    "include_reviews" : false
}

   
   ########### Default Values #########


@app.get("/products")
def get_products(
    limit: int = 10
):
    return {
        "limit" : limit
    }


# if the user visited : /products
# the result is : 

{
    "limit" : 10
}



############## Pagination ###############

i have 10k products 
and i do not want send all 10k at once

so instead : 

/products?page=1&limit=10

meaning : Page = 1 and limit = 10


@app.get("/products")
def get_products (
    page: int = 1,
    limit: int = 10
):
   
    return {
        "page" : page,
        "limit" : limit
    }


############# Complete Code ########

from fastapi import FastAPI

app = FastAPI()

@app.get("/")
def home():
    return {
        "message" : "Welcome to my API"
    }


# Path Paramters 

@app.get("users/{user_id}")

def get_users(user_id:int):
    return {
        "user_id" : user_id
    }

# Multiple Path Paramters 

@app.get("/users/{user_id}/posts/{post_id}")
def get_post(user_id:int, post_id:int):
    return {
        "user_id" : user_id,
        "post_id" : post_id
    }


# Required Path Paramters

@app.get("/search")
def search_products(keyword: str):
    return {
        "keyword" : keyword
    }


# Optional Query Paramters

@app.get("/products")
def get_products(
    category:str | None = None,
    limit:int = 10
):
    return {
        "category" : category,
        "limit" : limit
    }


#Path + Query Paramters

@app.get("/products/{product_id}")
def get_product(
    product_id:int,
    include_reviews: bool = False
):

    return {
        "product_id" : product_id,
        "include_reviews" : include_reviews
    }


# one imp thing to Remeber #######

@app.get("/users/{user_id}")
def get_user(user_id: int):

FastAPI Knows:

user_id -> Path Parameter

because it exists in : 

/users/{user_id}

but look at : 

@app.get("/products")
def get_products(category: str | None = None):

category does not exist inside the path : 
So, FastAPI treats it as : Query Paramter

So,

Inside URL path {}
       ↓
Path Parameter


Inside function but not in path
       ↓
Query Parameter



######################## POST Requests and Request Body ################

# POST is mainly used to send new data to the backend

Frontend
    │
    │ POST /users
    │
    │ {user data}
    ▼
Backend
    │
    ▼
Create user


# POST usually sends the data inside the Request Body

POST /users

Request Body:
{
    "name" : "Samir",
    "age" : 21
}


# so now we have three places where data can come from 

1. PATH

/users/101
       ↓
user_id


2. QUERY

/users?age=21
           ↓
          age


3. BODY

{
    "name": "Samir",
    "age": 21
}


############# POST Request ##########

from fastapi import FastAPI

app = FastAPI()

@app.post("/users")
def create_user():
    return {
        "message" : "User created!"
    }


######## Same URL can haee Different Methods ########

@app.get("/users")
def get_users():
    return {
        "message" : "All users"
    }


@app.post("/users")
def create_user():
    return {
        "message" : "User Created"
    }


########### Pydantic #################

# suppose someone sends :

What fields do we expect?
What type should each field have?
Which fields are required?
Which fields are optional?

# so pydantic helps us to define the structure of our data 

Expected User Data
        │
        ▼
┌─────────────────────┐
│ name  → string      │
│ age   → integer     │
│ email → string      │
└─────────────────────┘

######### Creating a Pydantic Model ########

from pydantic import BaseModel

class User(BaseModel):  # Create a data model called User
    name : str  #name must be string
    age : int   # age must be integer
    email : str  # email must be string



######## using this model in a Post request 


from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()

class User(BaseModel):
    name: str
    age:int
    email:str

@app.post("/users")
def create_user(user : User):
    return {
        "message" : "User Created sucessfully",
        "user" : user
    }


# this line : def create_user(user : User):

# it means : 

FastAPI:
Receive the request body
        ↓
Convert it into User data
        ↓
Store it inside variable user


# Optional Fields 

# Suppose we want bio to be optional

class User(BaseModel):
    name : str
    age: int
    email: str
    bio: str | None = None  # Bio can be string OR None


### Creating a Product 

class Product(BaseModel):
    name: str
    price: float
    quantity: int

# now create an endpoint

@app.post("/products")
def create_products(product: Product):
    return {
        "message" : "Product Created",
        "product_name" : product.name,
        "price" : product.price,
        "quantity" : product.quantity
    }


######### Get and Post Together ############

from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()

class User(BaseModel):
    name: str
    age: int
    email: str

@app.get("/users")
def get_users():
    return{
        "message"  : "Here are all users"
    }


@app.post("/users")
def create_user(user: User):
    return {
        "message" : "User Created",
        "user" : user
    }


Frontend
    │
    │ POST Request
    ▼
FastAPI
    │
    │ Reads JSON Body
    ▼
User Model
    │
    │ Validates data
    ▼
create_user()
    │
    │ Python Logic
    ▼
Response
    │
    ▼
Frontend







