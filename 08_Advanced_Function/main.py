## Recursion 

def greet():
    print("Hello")
    greet()



def countDown(number):
    if number == 0:
        print("Done!")
        return 
    
    print(number)
    countDown(number - 1)

countDown(5)





def factorial(number):
    if number == 0:
        return 1

    return number * factorial(number- 1)


## Lambda Function : It is a small anonymous Function 

# Syntax : lambda paramters : expression

add = lambda a,b : a+b

print(add(5,10))

--------------------------------

sqaure = lambda number : number*number
print(square(5))

## For larger logic : Use def
## For very small one-line logic : Use lambda function 


######################## In Python, Functions are Objects, it is treated like values #############################

def greet():
    print("Hello")

message = greet  ## means -> Store the function
message()   # Hello


############ Passing a Function to Another Function

def greet():
    return "Hello"

def execute(function):
    print(function())

execute(greet)    # Output : Hello


#### Nested Functions

def outer():
    print("Outer function")

    def inner():
        print("Inner Function")
    inner()

outer()


######################## Decorators Basics ##################


# A function that extends the behavious of another function
# w/o modifying the bas function.
# Pass the base function as an argument to the decorator

# if u want to add something before and after the function, u can use decorator

def decorator(function):
    def wrapper():
        print("Before function")
        function()
        print("After function")
    return wrapper


##### Complete Example

def decorator(function):
    def wrapper():
        print("Before function")
        function()
        print("After function")

    return wrapper

@decorator
def greet():
    print("Hello")
greet()


# Output :

# Before function
# Hello
# After function


# What is the use of decorator in Backend ??

# Suppose an API, before running a function, you might need 

# Check authentication
# Check permission
# Log requests
# Validate access
# Measure execution time

@authentication
def get_users():
    return users



######################### map() #####################

# using map()
# you want square of each number

numbers = [1,2,3,4]

result = map(lambda number : number*number, numbers)
print(list(result))

# output : [1,4,9,16]

# Syntax : map(function, iterable)



###################### filter() ##########################

numbers = [1,2,3,4,5,6]

result = []

for number in numbers:
    if number % 2 == 0:
        result.append(number)
print(result)

# Using filter

numbers = [1,2,3,4,5,6]

result = filter(
    lambda number : number % 2 == 0,
    numbers
)

print(list(result))


############# IMP Backend Examples ###########

# Find adults

users = [
    {"name": "Samir", "age": 20},
    {"name": "Rahul", "age": 17},
    {"name": "Aman", "age": 22}
]

adults = list(
    filer(
        lambda user : user["age"] >= 18,
        users
    )
)

print(adults)


















