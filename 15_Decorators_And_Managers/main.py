## Decorators & Context Managers

## IMP

def greet():
    print("Hello Samir")

greet() # Hello Samir

# Now we want to add something before and after every function 

# If you want to add something before and after every function : 

# manually : 

def greet():
    print("Before function")
    print("Hello Samir")
    print("After function")


## Decorator : A decorator allows us to add extra behavior to an 
## existing function without changing its original code.


# IMP Note : Functions are Object in Python 
# we can store the function in a varaible

def greet():
    print("Hello")

x = greet

x()


# As functions are objects, so we can pass them as arguments 

def greet():
    print("Hello")

def execute(func):
    func()

execute(greet)   # Hello


# A function can also return another function 

def outer():
    def inner():
        print("Hello")
    
    return inner

x = outer()
x()

# outer() -> Returns inner

################## Simple Decorator ##################

def decorator(func):

    def wrapper():
        print("Before function")

        func()

        print("After function")

    return wrapper


# actual function 

def greet():
    print("hello samir")

greet = decorator(greet)

greet()

# Output : 

Before function
Hello Samir
After function

####### Another way to write this , cleaner code

instead of 

def greet():
    print("hello Samir")

greet = decorator(greet)

####### We can write : 

@decorator
def greet():
    print("Hello Samir")
greet()



# why do we call it wrapper : 

def decorator(func):

    def wrapper():
        print("Before")

        func()

        print("After")

    return wrapper


# wrapper() wraps around the original function 



        wrapper
   ┌─────────────────┐
   │                 │
   │    Before       │
   │                 │
   │   original      │
   │   function      │
   │                 │
   │    After        │
   │                 │
   └─────────────────┘



############## Decorators with Arguments ############

def decorator(func):

    def wrapper(*args, **kwargs):
        print("Before")

        func(*args, **kwargs)

        print("After")

    return wrapper


@decorator

def greet(name):
    print("Hello", name)

greet("Samir")



# *args handles positional arguments
func(10,20)

# **kwargs handles keyword arguments 
func(a=10, b=20)


#another examples 

def decorator(func):

    def wrapper(*args, **kwargs):
        return func(*args, **kwargs)

@decorator

def add(a,b):
    return a+b


# Authentication Examples 

def login_required(func):

    def wrapper(*args, **kwargs):
        logged_in = True

        if logged_in:
            return func(*args, **kwargs)
        print("Please Login")

    return wrapper

@login_requires
def dashboard():
    print("Welcome to dashboard")
dashboard()

# the decorator checcks authntication beore allowing the function to execute


