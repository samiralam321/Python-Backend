## Operators ar Symbol that performs operations 

a = 10
b = 2

print(a+b)   # + is operator

print(a+b)
print(a-b)
print(a*b)
print(a/b) # 5.0  Devision
print(a//b) # 5  Floor Division

print(10/3) # 3.333
print(10//3) # 3

print(10 % 3) # Modulus 

number = 10
print(number % 2)

###############  Power ##############

print(2 ** 3)   # 8


############### 

age = 20
has_id = True

if age >= 18 and has_id:
    print("Entry allowed")


is_admin = False
is_owner = True

print(is_admin or is_owner) # True


if (age >= 18):
    print("U can vote")

age = int(input("Enter your age : "))

if age >= 18:
    print("U can vote")
else:
    print("U cannot vote")




marks = int(input("Enter your marks : "))

if marks >= 90:
    print("A")
elif marks >= 75:
    print("B")
elif marks >= 50:
    print("C")
else:
    print("Fail")



username = input("Enter username : ")
password = input("Enter password : ")

if username == "samir" and password == "1234":
    print("Login successful")
else:
    print("Invalid username or password")


## Nested Conditions 

age = 20
has_id = True

if age >= 18:
    if has_id:
        print("Allowed")
    else:
        print("ID Required")
else:
    print("Must be 18 or older")


### Assignment Operator ###########

age = 20
age += 1

print(age)

