################# Exception Handling ######################

# Differece between Error Vs Exception 

# An error means Python cannont continue normally
print(10/0)  #ZeroDivisionError

number = int("hello") #ValueError


# Suppose u r building a calculator and, if the user enters invalid numbers
# your application will be crashed, and you don't want that
# So, use try and except 

# try and except 

try:
    code_that_might_fail
except:
    code_to_handle_error




try:
    number = int(input("Enter a number : "))
    print(number)

except:
    print("Invalid Input")


# If user enters : 20, Output : 20
# If user enters : hello, Output : Invalid input

Try this code
      ↓
Did it work?
   ↙       ↘
 YES       NO
  ↓         ↓
Continue   except


# So,

try
↓
"Try this"

except
↓
"If something goes wrong, handle it"



# Do not always write except:

try:
    number = int(input("Enter number : "))

except ValueError:
    print("Please enter a valid number ")


## Multiple Exceptions 

try:
    a = int(input("Enter your number : "))
    b = int(input("Enter second number : "))

    print(a/b)

except ValueError:
    print("Please enter number only")

except ZeroDivisionError:
    print("Cannot divide by zero")


# else -> run only when no exception occurs

try:
    number = int(input("Enter number : "))

except ValueError:
    print("Invalid number")

else:
    print(f"You entered {number}")


## So remeber,

# try    → Try the code
# except → Handle error
# else   → Run if everything succeeded


## finally

# finally always execute

try:
    number = int(input("Enter number : "))

except ValueError:
    print("Invalid Number")

finally:
    print("Program finished")


# If input is valid:

# You entered 10
# Program finished

# If input is invalid:

# Invalid number
# Program finished

# The finally block runs in both cases.


# Real database connection exmaple where fianlly keyword is useful 

try:
    connect_to_database()
    perform_operations()

finally:
    close_database_connections()


################# raise ##############

# Sometimes you want to create an exception yourself 

age = 15

if age < 18:
    raise ValueError("Age must be 18 or above")


############## Handling a Raised Exception ##############
# Combining raise with try/except

def register_user(age):
    if age < 18:
        raise ValueError("Age must be 18 or older")
    return "Registration Successfully"


try:
    result = register_user(15)
    print(result)

except ValueError as error:
    print(error)


##

try:
    number = int("hello")

except ValueError as error:
    print(error)

# you might see : invalid literal for int() with base 10: 'hello'


################### Common Python Exceptions ############

ValueError
TypeError
ZeroDivisionError
IndexError
KeyError
NameError
FileNotFoundError



##### Avoid using Bare except #########

try:
    something()

except:
    print("Error")

# it can hide bugs so aboi avoid it

## Prefer 

try : 
    something()

except ValueError:
    print("Invalid value")


# Or, when appropriate 

except Exception as error:
    print(error)

# Specific exceptions are better because they tell you what went wrong



################# Nested try/except ########################

def register_user(name, age, email):
    if name == "":
        raise ValueError ("Name cannot be empty")

    if age < 18:
        raise ValueError("Age must be 18 or above")
    
    if "@" not in email:
        raise ValueError("Invalid email")

    return {
        "name" : name,
        "age" : age,
        "email" : email
    }

try:
    name = input("Enter name : ")
    age = int(input("Enter age : "))
    email = input("Enter email : ")

    user = register_user(name, age, email)
    print(user)

except ValueError as error:
    print(f"Registration failed : {error}")




## Backend Example : Safe Division Function 

def deivde(a,b):
    if b == 0:
        raise ValueError("Cannot divide by zero")
    return a/b

try:
    result = deivde(10,0)
    print(result)

except ValueError as error:
    print("f"Error : {error})

# Output : Cannot divide by zero



######## Exception Handling with User Input ###############

while True:
    try:
        age = int(input("Enter your age : "))
        break

    except ValueError:
        print("Plase enter a valid number ")

print(f"Your age is {age}")



######## Complete Examples #############

def create_user(name, age, email):
    if not name:
        raise ValueError("Name cannot be empty")
    if age < 18:
        raise ValueError("Age must be 18 or above")
    if "@" not in email:
        raise ValueError("Invalid email")

    return{
        "name" : name,
        "age" : age,
        "email" : email
    }

try:
    name = input("Enter your name : ").strip()
    age = int(input("Enter your age : "))
    email = input("Enter your email: ").strip()

    user = create_user(name, age, email)

except ValueError as error:
    print(f"Error : {error}")

else:
    print("User created succesfully")
finally:
    print("Process Compelted")

