## List 

## Lists are Mutable 
## List can store Different Data Types

users = ["samir", "aman", "rahul", "riya"]
print(users[0])
print(users[1])
print(users[-1]) ## U can access from the End

print(users[1:3]) ## Start -> Included and End -> Excluded 
print(users[:2])
print(users[2:])

## append() : Adding an item to the end of the List

users.append("Priya")
print(users)


## insert(index, value) : insert at a specific postion 

users.insert(1, "Siya")

users.remove("samir")
print(users)

## pop() : Remove and returns and element; it removes the last element

users.pop()
print(users)

## clear() : Removes everything

users.clear()
print(users)


##  Check if an item Exists or not 

if "samir" in users:
    print("User found")

if "Priya" not in users:
    print("user not found!!")


## Loop with index 

for index, user in enumerate(users):
    print(index, user)

## indexing is started from the 0 but what if we want the indexing that sholud be start with '1' ??

for index, user in enumerate(users, start=1):
    print(index, user)

##  Now the idnexing is started from the 1 

###############  sort() #############

numbers = [5,2,9,1,7]
numbers.sort()
print(numbers)

## How to sort in Descending Order ??

numbers.sort(reverse=True)
print(numbers)

##   reverse() #########

users = ["Samir", "Rahul", "Aman"]
users.reverse()

print(users)


## Nested Lists

users = [
    ["Samir", 20],
    ["Sonu", 21],
    ["Aman", 22]
]

print(users[0])


## User Management 

users = []

while True:
    print("\n1. Add User")
    print("2. Show Users")
    print("3. Exit")

    choice = input("Enter your choice : ")

    if choice == '1':
        name = input("Enter user name: ")
        users.append(name)
        print("user added successfully")
    
    elif choice == '2':
        if(len(users)) == 0:
            print("No user found")
        else:
            print("\nUsers : ")

            for index, user in enumerate(users, start=1):
                print(f"{index}. {user}")
    elif choice == "3":
        print("Goodbye")
        break
    else:
        print("Invalid Choice")













