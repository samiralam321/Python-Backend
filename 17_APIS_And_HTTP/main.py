## Working with API's and HTTP

Your Website
     ↓
   API
     ↓
Backend Server


# role of API

Mobile App
     │
     │ HTTP Request
     ↓
Backend API
     │
     │ HTTP Response
     ↓
Mobile App


# Request : A client sends a request
# Response : A server sends a response


CLIENT
   │
   │ Request
   ↓
SERVER
   │
   │ Response
   ↓
CLIENT


# Who is the Client ? 

# A client is the thing making the request.

# Browser
# Mobile App
# Fronted JavaScript
# Postman
# Another Backed


# For examples, when you open: 

# example.com

# your browser acts as a client


########### Who is the Server ##########

# A server is the machine/application that receives the request 
# and sends back a response

# for a backend application:

Browser
   ↓
FastAPI server
   ↓
Python code
   ↓
Database


The server could be running somewhere on the internet 


################### URL ############

# A URL tell the clinet where to send the request 

https://example.com/users/101
   │          │          │
 protocol    host       path


################ HTTP Methods ####################

GET
POST
PUT
DELETE


| Method | Basic meaning   |
| ------ | --------------- |
| GET    | Give me data    |
| POST   | Create new data |
| PUT    | Update data     |
| DELETE | Delete data     |




############### What is an endpoint ##############

# Suppose your backend has : 

GET /users
GET /users/101
POST /users
DELETE /users/101

# Each API route is called as endpoint 

/users is an enpoint path

# A complete API endpoint ca be thought of as : 

HTTP Method + URL/Path

# For examples : GET /users



################## Request #################


# An HTTP request can contain several things :

REQUEST
│
├── Method
├── URL
├── Headers
├── Query Parameters
└── Body


# Example : 

POST /users
Content-Type: application/json

{
    "name" : "Samir",
    "age" : 20
}


####################### Headers #####################

# Header provides the additional information about the request 

# example : 

# Content-Type: application/json

# This tells the servers :

# "The data i'm sending is JSON"

# Another common header : 

# Authorization: Bearer <token>


###################### Request Body ################

# The body contains data you are sending to the server

# for examples : 

{
    "name" : "samir",
    "email" : "sam@gmail.com"
}


################## Query Paramters ##################

# Suppose you want to search users.

GET /users?name=Samir

# Here : ?name=Samir   is a query parameter


# Multiple Paramters 

GET /users?name=Samir&age=21

# so, /users is the path
# and ?name=Samir&age=21  contains query parameter


################### Path Paramters ###############

/users/101 : 101 can be a path paramters


################# Query vs Path Paramter ##############

# Path Paramters :  => you are identifying a specifc resource 

/users/101

# Query Paramter => is generally filtering and searchgin 

/users?age=21   



################ Response ##########

# A server sends a response back 

# A response generally contains : 

RESPONSE
│
├── Status Code
├── Headers
└── Body


# Ex : 

HTTP 200

{
    "name": "Samir",
    "age": 21
}


############## Python Dictionary Vs JSON ##############

# Python : 

user = {
    "name" : "Samir",
    "age" : 21
}


JSON : 

{
    "name" : "Samir",
    "age" : 21
}


## Python -> JSON

import json

user = {
    "name" : "Samir",
    "age" : 21
}

data = json.dump(user)
print(data)

# dumps() means : Python object -> JSON string



## JSON -> Python

import json

data = '{"name" : "Samir", "age" : 21}'

data = json.loads(data)
print(user)


# loads() means : JSON string -> Python object

# Remember : 

dump  → Python → JSON file
load  → JSON file → Python

dumps → Python → JSON string
loads → JSON string → Python


########## Call an API using Python ##############

# install : pip install requests 

import requests

response = requests.get("https://api.hithub.com")
#response contains information about the servers response

print(response.status_code)
print(response.json())


Python program
      ↓
  GET request
      ↓
  API server
      ↓
   Response
      ↓
    Python


############### GET with query/paramters 

# instead of manually contructing : ?name=Samir&age=21

import requests

params = {
    "name" : "Samir",
    "age" : 21
}

response = requests.get(
    "https://example.com/users",
    params=params
)


############# POST Request ############

import requests 

user = {
    "name" : "Samir",
    "age" : 21
}

response = requests.post(
    "https://example.com/users",
    json=user  # means : Send this python data as JSON
)

print(response.status_code)
print(response.json())


## PUT (Update)

response = requests.put(
    "https://example.com/users/101",

    json={
        "name" : "Samir",
        "age" : 22
    }
)


## DELETE 

response = requests.delete(
    "https://example.com/users/101"
)


############# A Complete Backend Flow ##########

# Imagine you are building a student's management application.


Frontend:

User clicks "Add Student"

Frontend sends:

POST /students

with:

{
    "name": "Samir",
    "age": 21,
    "course": "CSE"
}

Backend receives it:


POST /students
       ↓
Validate data
       ↓
Business logic
       ↓
Database
       ↓
Student created


Backend responds:

201 Created

with:

{
    "id": 101,
    "name": "Samir",
    "age": 21,
    "course": "CSE"
}

Frontend receives it and updates the UI.

That's backend development in action.


################## REST API  ######################


# REST API as a common way of designing web APIs around resources.

























