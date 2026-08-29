## Strings are immutable

name = "samir"

print(type(name)) # <class 'str>
print(name[0])
print(name[1])
print(name[2])

# Python can also access from the end, it is called Negative Indexing

name = "samir"
print(name[-1])
print(name[-2])


## Slicing 

name = "samir"
print(name[0:3])  ## Sam


## More Exmapl

name = "Samir"
print(name[1:4])

print(name[:3])   # from start
print(name[0:3])

# Untill the end

print(name[2:])   # mir


## String step

string[start:end:step]

text = "python"
print(text[::2])  ## Output : Pto

## Reverse a string

name = "samir"

print(name[::-1])


## upper()

name = "samir"
print(name.upper())

## lower()

name = "SAMIR"
print(name.lower())


## Useful logic to handle the login and email handling

email = input("Enter email : ")
email = email.lower()

print(email)


## title()

name = "samir alam"
print(name.title())  # Output : Samir Alam


## capitalize()

name = "samir alam"
print(name.capitalize())

## Samir alam : only the first charcter become upper case


## strip()  => Remove the space from the beginning and end

name = "   samir   "
print(name.stripe())



## U do not want to stroe unnecessary spaces 

username = input("Enter username : ").stripe()


## find()   Used to find the postion of something 

email = "samir@gmail.com"
print(email.find("@"))   ## 5


## 'in'  Keywords  : To check whether something exists or not 

email = "samir@gmail.com"
print("@" in email)  ## True



## Exmaples Validation : 

email = input("Entr email : ")

if "@" in email:
    print("Valid email")
else:
    print("invalid email ")


## startswith() and endswith()

## check how a string starts or ends : 

email = "samir@gmail.com"
print(email.startswith("samir"))  ## Output is True
print(email.endswith(".com")) ## True

## Real backend example

filename = "photo.jpg"

if filename.endswith(".jpg"):
    print("Valid image")


## count()

text = "banana"
print(text.count("a")) ## 3


## String concatention using '+' 

first_name = "Samir"
last_name = "Alam"

full_name = first_name + " " + last_name

## F-Strings 

name = "samir"
age = 20

print(f"My name is {name} and i am {age} years old")
print(f"My nam is {name} and i will be {age+1} next years ")


## Real backedn example

username = "samir"
user_id = 101

message = f"User {username} with ID {user_id} created successfully"
print(message)



## Loop thorugh a string

name = "Samir"
for ch in name :
    print(ch)


## count vowels 

name = "samir"
count = 0

for ch in name:
    if ch.lower() in "aeiou":
        count += 1

print("Vowels : ", count)


## Email Validation 

email = input("Enter your email : ").stripe().lower()

if email == "" :
    print(Cannot empty)
elif "@" not in email:
    print("Invalid email")

elif not email.endswith(".com"):
    print("Email must end with .com")

else:
    print("Email is Valid!!")















