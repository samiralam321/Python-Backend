print("Hello, Samir!")

####   Varaible 

name = "Samir"
print(name)

age = 20
print(age)

# Python automatically understand the types

# C++
string name = "Samir";
int age = 20;

# Python

name = "Samir"
age= 20 


# Variable Naming Rule : Variable cannot start with a number

name = "Samir"
student_age = 20
totalMarks = 90

age = 20
price = 33.33
name = "samie"
is_student = True
data = None

print(type(name)) //string
print(type(age)) // <class 'int'>

print(type("Hello"))
print(type(10))
print(type(10.4))
print(type(10.5))
print(type(True))


### String

name = "samir"
city = "Kapurthala"
city = 'Kapurthala' # is also valid

a  = 10
b = 20

sum = a + b
print(sum)

## Boolean

is_logged_in = True
is_admin = False

# Examples : 

is_authenticated = True

if is_authenticated:
    print("Welcome User")


## None : Means there is currently no value

user = None

# User exits as a variable but currently has no value

user = None # might mean User not found

database_connection = None

# Later the variable might receive a real value


#### Taking Input #########################

name = input("Enter your name")
print(name)

##

name = input("Enter your name : ")
print("Hello", name)

## Or use f-string

name = input("Enter your name : ")
print(f"Hello {name}")

################### Input always Returns String #######################

age = input("Enter your age : ")
print(type(age))

# If u enter 20, the type will be 'str' so we need type conversation



############## Type Conversion ##################

age = int(input("Enter your age : "))
print(age)

price = float(input("Enter price : "))


############## Convert Number to string ############

age = 20
age_text = str(age)


############### Example #################

name = input("Enter your name : ")
email = input("Enter your email : ")
age = int(input("Enter your age : "))

print("------------ User Details ------------")
print(f"Name : {name}")
print(f"Email : {email}")
print(f"Age : {age}")