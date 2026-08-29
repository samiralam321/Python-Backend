def greet():
    print("Hello Samir")

greet() # Function Call

# def functin_name():
#     code


def greet(name):
    print(f"Hello {name}")

greet("Samir")
greet("Rahul")
greet("Aman")


def user_info(name, age):
    print(f"Name : {name}")
    print(f"Age : {age}")

user_info("Sami", 20)




def add(a,b):
    print(a+b)

result = add(4,10)
print(result)


## 

def total(price, quatity):
    return price * quantity

ans = total(100,3)

print(f"Total : {total}")



def get_user():
    return {
        "Name" : "Samir",
        "age" : 20
    }



## Default Paramters 

def greet(name="Guest"):
    print(f"Hello {name}")

greet()


## Keywords Arguments 

def user_info(name, age, city):
    print(name)
    print(age)
    print(city)

user_info("Samir", 20, "Kapurthala")   # it is postional keywords and order is matter , same order like the parameters

## We can also pass the arguments in another way

## keyword Arguments : In this arguemen,s the order is not matter

user_info(
    "name" = "Samir",
    age = 20,
    city = "kaputhala"
)


## *args : use it when u have no idea like how many arguments will comes?


def add(*numbers):   # *numbers collected arguments into a tuple
    total = 0;

    for number in numbers:
        total += number
    return total

print(add(10,20))
print(add(10,20,30))
print(add(10,20,30,40,50))


## **kwargs   : Used when u do not how many keywords arguments will come

def user_info(**data):
    print(data)

user_info(
    name = "Samir",
    age = 20,
    city = "Japan"
)

## **kwargs collects the data into a dictionary


def user_info(**data):
    for key,value in data.items():
        print(f"{key} : {value}")

user_info(
    name = "Samir",
    age = 20,
    city = "Kapurthala"
)



# *args
# ↓
# Multiple positional arguments
# ↓
# Tuple


# **kwargs
# ↓
# Multiple keyword arguments
# ↓
# Dictionary


def test(*args, **kwargs):
    print(args)
    print(kwargs)

test(
    10,
    20,
    name = "samir",
    age = 20
)

## Output : 

(10,20)

{
    'name' : 'samir',
    'age' : 20
}


############# Functions Calling Functions ###########

def get_name():
    return input("Enter your name : ")

def greet(name):
    print(f"Hello {name}")

name = get_name()
greet(name)


########### Backend Style Example ###################

users = []

def create_user(name,age):
    user = {
        "name" : name,
        "age" : age
    }

    users.append(user)
    return user

new_user = create_user("Samir", 20)
print(new_user)


## Output : 

# {
#     "name" : "Samir",
#     "age" : 20
# }



### Simple Calculator using functions


def add(a, b):
    return a+b

def subtract(a, b):
    return a - b

def multiply(a, b):
    return a * b

def divide(a, b):
    if b == 0:
        return "Cannot divide by zero"

    return a / b


while True:
    print("\n1. Add")
    print("2. Subtract")
    print("3. Multiply")
    print("4. Divide")
    print("5. Exit")

    choice = input("Enter choice: ")

    if choice == "5":
        print("Goodbye")
        break

    a = float(input("Enter first number: "))
    b = float(input("Enter second number: "))

    if choice == "1":
        print(add(a, b))

    elif choice == "2":
        print(subtract(a, b))

    elif choice == "3":
        print(multiply(a, b))

    elif choice == "4":
        print(divide(a, b))

    else:
        print("Invalid choice")

