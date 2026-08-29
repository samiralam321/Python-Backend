## Tuples 

## Tuples are Immutable
## List is Mutable 


## A tuple stores multiple values, similar to a list 

## List : 

users = ["Samir", "Rahul"]

## Tuple : 

users = ("Samir", "Rahul")
print(users[0])
print(users[-1])

users[0] = "Aman" ## ERROR, U can't change the tuple elements

## Tuple is Fixed Data
## Lists are Changable Data 

################## Single Element Tuple ##################

number = (10)  # This is not tuple, Python treats it as: int

## Correct : 

number = (10,) ## The comma is necessary

--------------------------------------------------

numbers = (1,2,3,2,2)
print(numbers.count(2))

users = ("samir", "rahul", "aman")
print(users.inde("Rahul"))
users.add("Amamnn")
users.remove("samir")


## Set -> Store unique elements 

users = ["samir", "rahul", "samir", "aman"]
unique_users = set(users)

print(unique_users)  ## Order is not guranteed


---------------------------------------------------------

## discard()

users = {"Samir", "Rahul"}
users.discard("Priya")

print(users)


# Remember : 

# remove() -> Error if not found
# discard() -> No error if not found


## pop()

users = {"samir", "Rahul", "Aman"}
users.pop()   # it removes arbitary item
print(users)



## Set Operations 

python_user = {"samir", "rahul", "aman"}
java_user = {"rahul", "aman", "priya"}


# union

print(python_user | java_user)

python_user.union(java_user)


################### Dictionaries #####################

# it store data as Key -> Value

user = {
    "name" : "samir",
    "age" : 20,
    "city" : "japan"
}

print(user["name"])

# Add new data

user["city"] = "Singhai"
print(user)

# Update data

user["age"] = 21
print(user)

# Remove Data 

user.pop("age")

# del ; delete the key

del user["age"]

# get()

# Instead of : print(user["email"])
# if email does not exist, Python gives an error

print(user.get("email")) ## Output : None

# Or u can add a default value : 

print(user.get("email", "Email not found"))


=============================================================

## Check if a key Exists or Not

user = {
    "name" : "Samir",
    "age" : 20
}

if "email" in user:
    print("email exist")
else:
    print("Email not exist")



## Dictionary Methods

user = {
    "name" : "Samir",
    "age" : 20
}

print(user.keys())   

## name
## age

print(user.values())

# Samir
# 20

print(user.items())

## Return both keys and values


## Loop through Dictionary

## Key

for key in user :
    print(key)

## Values : 

for value in user.values():
    print(value)



### Now print Key + Value

for key,value in user.items():
    print(key, ":", value)

# name : Samir
# age : 20


## Nested Dictionary

user = {
    "name" : "Samir",
    "address" : {
        "city" : "kapurthala",
        "state" : "Punjab"
    }
}


print(user["address"]["city"])


################# (IMP) List of Dictionaries ######################

users = [
    {
        "name" : "Samir",
        "age" : 20
    },

    {
        "name" : "Rahul",
        "age" : 21
    },

    {
        "name" : "Aman",
        "age" : 22
    }
]

for user in users :
    print(user["name"])




############### Backend Examples #################

users = []

while True:
    print("\n1. Add User")
    print("2. Show Users")
    print("3. Exit")

    choice = input("Enter choice: ")

    if choice == "1":
        name = input("Enter name: ")
        age = int(input("Enter age: "))

        user = {
            "name": name,
            "age": age
        }

        users.append(user)

        print("User added successfully")

    elif choice == "2":
        if len(users) == 0:
            print("No users found")

        else:
            for user in users:
                print(f"Name: {user['name']}")
                print(f"Age: {user['age']}")
                print()

    elif choice == "3":
        print("Goodbye")
        break

    else:
        print("Invalid choice")






















