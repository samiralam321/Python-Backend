## There are two loops : for and while

for variable in something:
    code

for i in range (5):
    print(i)   ## 0 1 2 3 4 

for i in range(1,6):
    print(i) # 1 2 3 4 5  ; ending value is excluded 


# range(start, end, step)

for i in range(1,11,2):
    print(i)

# 1 3 5 7 9

# Print 1 to 10

for i in range(1,11):
    print(i)

# Print 10 to 1

for i in range(10,0,-1)   # -1 means move backwards

for i in range(1,6):
    print("Current Number : ", i)

## Multiplication Table

number = int(input("Enter a number : "))

for i in range(1,11):
    print(number, "x", i, "=", number*i)


# using an f-string

number = int(input("Enter a number : "))
for i in range(1,11):
    print(f"{number} x {i} = {number*i}")




## While loop

i = 1

while i<=5 :
    print(i)
    i += 1


## Break

for i in range(1,11):
    if i == 6:
        break
    print(i)


# Real Backend Examples

users = ["Samir", "Rahul", "Aman", "Admin"]

for user in users:
    if user == "Admin":
        print("Admin found")
        break
    print(user)



# continue

for i in range(1,6):
    if i == 3:
        continue
    print(i)



# Nested Loops

for i in range(1,4):
    for j in range(1,4):
        print(i,j)


for user_id in range(1,6):
    print(f"Processing user {user_id}")


## 

n = int(input("Enter a number : "))
total = 0

for i in range(1,n+1):
    total += i


print("Sum : ", total)





## Login Attempts 

correct_password = "1234"
attempt = 0

while attempt  < 3:
    password = input("Enter password : ")

    if password == correct_password:
        print("Login Successful")
        break
    
    print("Wrong Passowrd")
    attempt += 1

















