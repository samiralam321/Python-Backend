################### Advanced File Handling ###############

# File Cursor 

file.read(5)  # it reads the first 5 characters 

# tell()  : tells you where the cursor currently is : 

with open("data.txt", "r") as file:
    print(file.tell())

# Output : 0   means the cursoe starts at position 0

with open("data.txt", "r") as file:
    print(file.tell())
    file.read(5)
    print(file.tell())


######### seek() : Moves the cursor ################

with open("data.txt", "r") as file:
    print(file.read(5))  # Hello
    file.seek(0)
    print(file.read(5))  # Hello 


######### read() vs readline() vs readlines() #########

# Suppose data.txt

# Samir
# Rahul
# Aman

# read() : It reads everything : 

with open("data.txt", "r") as file:
    data = file.read()

print(data)


# It will print all the names

# read() -> everything 


############# readline() : Reads one line 

with open("data.txt", "r") as file:
    line = file.readline()
    print(line)


# Result = Samir



with open("data.txt", "r") as file:
    print(file.readline())
    print(file.readline())

# Output : Samir 
#          Rahul


################ readlines() : Reads all the lines and give you a list #################

with open("data.txt", "r") as file:
    lines = file.readlines()

print(lines)

# Output : ["Samir\n", "Rahul\n", "Aman\n"]



######### So remember ###########

# read()
# ↓
# Whole file as string

# readline()
# ↓
# One line

# readlines()
# ↓
# All lines as list


############# Better way to write the syntax ##############

with open("data.txt", "r") as file:
    for line in file:
        print(line.strip())

# it is useful for large files 


######### Why not read() ########

# Suppsoe you have 5 GB file, then you will do data = file.read()
# Python tries to load the entire file into memory
# That is not efficient


# Instead : 

with open("large_file.txt", "r") as file:
    for line in file:
        process(line)



############## Checking Whether a File Exists ################

# instead of open a file and hoping it exists, we can check : 

import os

if os.path.exists("user.json"):
    print("File exists")

else:
    print("File does not exist")


# Modern python gives us even cleaner approach 

####################### pathlib ############################

from pathlib import Path   #Import

# Create a path:

file_path = Path("users.json")

if file_path.exists():
    print("file exists")


#######################  Check if it is File

from pathlib import Path

file_path = Path("users.json")

if file_path.is_file():
    print("it is a file")

#################### Check if it is a Folder 

from pathlib import Path

folder = Path("data")

if folder.is_dir():
    print("it is a folder")

###################### Create a Folder

from pathlib import Path

folder = Path("data")

folder.mkdir()

# If the folder might already exist :

folder.mkdir(exist_ok=True)



############### Create a File inside Folder #################

from pathlib import Path

folder = Path("data")

folder.mkdir(exist_ok=True)

file_path = folder / "users.txt"   # a nice feature of pathlib

with open(file_path, "w") as file:
    file.write("Samir")




################## Read file using pathlib

from pathlib import Path

file_path = Path("data.txt")

data = file_path.read_text()
print(data)

# And Write  : 

file_path.write_text("Hello Samir")



#################### JSON + pathlib

import json
from pathlib import Path

file_path = Path("users.json")

users = [
    {
        "name" : "Samir",
        "age" : 20,
    }
]

with open(file_path, "w") as file:
    json.dump(users, file, indent=4)


# Notice that open() accepts Path object


######## Safe JSON Loading : Suppose users.json does not exist ############

with open("users.json", "r") as file:
    users = json.load(file)   # Cause : FileNotFoundErro

#######


import json
from pathlib import Path

file_path = Path("users.json")

try:
    with open(file_path, "r") as file:
        users = json.load(file)

except FileNotFoundError:
    users = []

print(users)


# Now if file exits then Load it, else use []


########## Now suppose the file exists but it is not valid

# suppose users.json contains : This is not valid JSON
# then json.load(file) will fail with JSONDecodeError


import json

try:
    with open("users.json", "r") as file:
        users = json.load(file)

except FileNotFoundError:
    users = []

except json.JSONDecodeError:
    print("Invalid JSON File")
    users = []

# Now our application won't crush just because the JSON file is invalid


import json
from pathlib import Path

file_path = Path("data/users.json")

def load_users(){
    try:
        with open(file_path, "r") as file:
            return json.load(file)

    except FileNotFoundError:
        return []

    except json.JSONDecodeError:
        return []
}

def save_users(users):
    file_path.parent.mkdir(exist_ok = True)

    with open(file_path, "w") as file:
        json.dump(users, file, indent=4)

def create_user():
    name = input("Enter name : ")
    age = int(input("Enter age : "))
    email = input("Enter email : ")

    return{
        "name" : name,
        "age" : age,
        "email" : email
    }


users = load_users()
user = create_user()

users.append(user)

save_user(users)
print("User saved successfully")



########## Task 

# Task 1

with open("data.txt", "r") as file:
    for line in file:
        print(line.strip())


# Create Folder and   File suing Path 

from pathlib import Path

folder = Path("data")

folder.mkdir(exist_ok=True)

file_path = foler/"text.txt"

file_path.write_text("Hello Backend")



