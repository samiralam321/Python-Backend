############# File Handling ####################

# The basic idea about this module : 

# Python Program
#       ↓
# Open File
#       ↓
# Read / Write / Append
#       ↓
# Close File


## IMP Note  

# Variable
# → Temporary data in memory

# File
# → Persistent data on storage


############### open() ##########

# file = open("data.txt", "w")   # ''w' means write

# data.txt = File name
# "w" = Mode

# If the file does not exist, Python creates it.

# Write to a File

file = open("data.txt", "w")
file.write("hello Samir")

file.close()

# open() -> Use file -> close()

############# Better way using with() ##############

with open("data.txt", "w") as file:
    file.write("Hello")

# Python automatically closes the file

with open(.....) as file:


## File Modes 


# | Mode  | Meaning         |
# | ----- | --------------- |
# | `"r"` | Read            |
# | `"w"` | Write           |
# | `"a"` | Append          |
# | `"x"` | Create new file |
# | `"b"` | Binary mode     |


with open("data.txt", "r") as file:
    content = file.read()

print(content)


# 'r' is default 

with open("data.txt") as file:
    content = file.read()

# is equivalent to : 

with open("data.txt", "r") as file:

# python assumes read mode if you don't specift a mode


##################  Read line by line ##############

readline()

with open("data.txt", "r") as file:
    line = file.readline()
    print(line)


## Read all lines 

with open("data.txt", "r") as file:
    liens = file.readlines()

print(lines)

######### Loop through a File ###########

with open("data.txt", "r") as file:
    for line in file:
        print(line.strip())


########## 'w' Overwrites ################

Suppose the file content

Rahul
Samir
Aman

with open("data.txt", "w") as file:
    file.write("Priya")

# The old content is gone

# File become "Priya"

# 'w' -> Write from scratch 


####################### Append Mode "a" ################

with open("data.txt", "a") as file:
    file.write("\nPriya")

# w-> Replace
# a -> Add to end


## Create a New File with "x"

with open("new_file.txt", "x") as file:
    file.write("hello")

# "x" means create the file


############# FileNotFound Error #########

with open("abc.txt", "r") as file:
    content = file.read()

# but abc.text does not exits 

# Python raise : FileNotFoundError

# We can handle it 

try:
    with open("abc.txt", "r") as file:
        content = file.read()

except FileNotFoundError:
    print("File not Found")



################ Writing User Data to a File ############

name = input("Enter your name : ")
age = int(input('Enter your age : '))

with open("users.txt", "a") as file:
    file.write(f"Name : {name}, Age : {age}\n")

print("User saved successfully")


############### Reading User Data

with open("users.txt", "r") as file:
    data = file.read()
print(data)


### You can also specift folders

with open("data/users.txt", "r") as file:
    content = file.read()



############### Python Dictionary -> JSON File

user = {
    "name" : "Samir",
    "age" : 20,
    "skills" : ["Python, "C++]
}


# Write it

import json

user = {
    "name" : "Samir",
    "age" : 20,
    "skills" : ["Python", "C++"]
}

with open("user.json", "w") as file:
    json.dump(user, file, indent=4)


#### What is dump() Vs load() #################

dump()
   ↓
Python → JSON


load()
   ↓
JSON → Python


#### JSON String Vs JSON File ########

json.dumps()
json.loads()

dump  → file
dumps → string

load  → file
loads → string

##########################################

import json

user = {
    "name" : "Samir",
    "age" : 20
}

data = json.dumps(user)

print(data)
print(type(data))

# Output : 

{"name": "Samir", "age": 20}
<class 'str'>


## So, dumps() => Dictionary -> JSON string



############# Mini Project : User Storage ############

import json

def load_users():
    try:
        with open("users.json", "r") as file:
            return json.load(file)

    except FileNotFoundError:
        return []


def save_users(users):
    with open("users.json", "w") as file:
        json.dump(users, file, indent=4)

users = load_users()

name = input("Enter name : ")
age = int(input("Enter age : "))

user = {
    "name" : name,
    "age" : age
}

users.append(user)

save_user(users)

print("User saved sucessfully")



################## Again Revsion ###########

with open("data.txt", "r") as file:
    data = file.read()

# 'r' means get Data from th file

with open("data.txt", "r") as file:
    data = file.read()


with open("data.txt", "w") as file:
    file.write("Hello")


# Create notes.txt and write Something 

with open("notes.txt", "w") as file:
    file.write("Learning Python")


# Read a File 

with open("notes.txt", "r") as file:
    data = file.read()
print(data)


####### User Storage #####

import json

name = input("Enter name : ")
age = int(input("Enter age : "))
email = input("Enter email : ")

user = {
    "name" : name,
    "age" : age,
    "email" : email
}

with open("user.json", "w") as file:
    json.dump(user, file, indent=4)

print("User saved successfully")








