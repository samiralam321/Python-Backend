import calculator

result = calculator.add(10,5)
print(result)

What means of import ???

# So you r bascially saying: Find calculator.py and make it
# code avaialbe here

# Or you can import in another way 

from calculator import add

print(add(10,4))


## Import Multiple Things

from calculator import add, subtract

print(add(10,5))
print(subtract(10,5))


## Import Everything : This import Everything

from calculator import *

#But avoid using this in real project, coz it becomes
# difficult to know where names come from 


## Aliases : you can give an imported module a shorter name

import calculator as calc

print(calc.add(10,5))



# Python built in module 

# import math

print(math.sqrt(25))


# import random

import random

number = random.randint(1,10)
print(number)


# Another 

import datetime

print(datetime.datetime.now())


######################################################

# there are 3 type of module in Python

# Built-in / standard Library
# your own modules       like auth.py / database.py   / users.py
# third party module     like FastAPI, Django, requests, SQLAlchemy Pydantic


##################### What is pip #########################

# so pip is Python's package installer
# suppose you want to install : requests
# you can run : pip install requests
# then python can use it : import requests


##################### Package ? ######################

# A Package is a collection of Python modules organized together

# shopping/
# │
# ├── __init__.py
# ├── products.py
# ├── cart.py
# └── payment.py


################## Module vs Package ############

# calculator.py -> Module

# While : 

# shopping/
# │
# ├── __init__.py
# ├── products.py
# ├── cart.py
# └── payment.py

# is a package

# so, Module is Python file and package is collection of Python modules 


################ what is __init__.py ###############

# it is useful for package initialization and compatibility


######### it matters for Backend

## Imagine a real backend

backend/
│
├── main.py
│
├── users/
│   ├── __init__.py
│   ├── routes.py
│   └── service.py
│
├── auth/
│   ├── __init__.py
│   ├── routes.py
│   └── service.py
│
└── database/
    ├── __init__.py
    └── connection.py



## Use of pip

# as FastAPI is not part of Python standard library

# but we can install it using 

pip install fastapi

# then 

from fastapi import FastAPI

# now we can use it : 


### Real Backend Worflow #########


Create Project
      ↓
Create venv
      ↓
Activate venv
      ↓
Install packages
      ↓
Write code
      ↓
Create requirements.txt
      ↓
Git / GitHub
      ↓
Deploy



### Complete Mental Model

                 PYTHON PROJECT
                       │
          ┌────────────┼────────────┐
          ↓            ↓            ↓
       main.py     users.py     auth.py
          │            │            │
          └────────────┼────────────┘
                       ↓
                    MODULES
                       ↓
                    PACKAGES
                       ↓
              External Libraries
                       ↓
                      pip
                       ↓
              Virtual Environment
                       ↓
                 Isolated Project


# short Notes

Module
→ A Python file

Package
→ Collection of modules

import
→ Bring a module into your code

from X import Y
→ Import a specific thing

pip
→ Install Python packages

venv
→ Isolated Python environment

requirements.txt
→ Project dependencies

.gitignore
→ Files Git should ignore



###


MODULE
Python file
calculator.py

PACKAGE
Folder containing Python modules

IMPORT
import calculator

SPECIFIC IMPORT
from calculator import add

ALIAS
import calculator as calc

PIP
Install external packages

pip install package_name

VIRTUAL ENVIRONMENT
Isolated Python environment

python -m venv venv

WINDOWS ACTIVATE
venv\Scripts\activate

DEACTIVATE
deactivate

DEPENDENCIES
requirements.txt

CREATE
pip freeze > requirements.txt

INSTALL
pip install -r requirements.txt

GIT
.gitignore

IGNORE
venv/











