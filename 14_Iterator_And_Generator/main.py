# Iterable : Something you can go through one item at a time

# Iterate means :Go through items one by one 

# Iterator : An interator is an object that remembers where it currently is 

Iterable
   ↓
Can be iterated

Iterator
   ↓
Actually remembers the current position


# iter() : Convertes iterable into an iterator 

numbers = [10,20,30]

iterator = iter(numbers)
print(next(iterator))  #10
print(next(iterator))  #20
print(next(iterator))  #30


# a string is alos iterable

name = "samir"

iterator = iter(name)

print(next(iterator))  # s
print(next(iterator))  # a
print(next(iterator))  # m

# what are __iter__() and __next__()

# __iter__() : Returns the iterator
# __next__() : Returns the next value

# When there are no values : raise StopIteration


####### Generator Vs List

numbers = [1,2,3,4,5,6]

# the entire list of stored in memory
# for a huge datset : 1,000,000 numbers the list stores all of them

# But


def number():
    for i in range(1,1000001):
        yield i

# does not create all one million numbers at once
# it produces them one at a time 

# it will save the memory 


############### Importsnt Difference #############

# list

numbers = [i for i in range(1000000000)]

# Generator

numbers = (i for i in range(10000000000))

# Create one
# ↓
# Use it
# ↓
# Create next
# ↓
# Use it

###### when should we use the Generator ???

# Large data
# Large files
# Streaming data
# Database results
# Logs
# API responses
# Data processing

# suppose i have a large file 
# so instead of 

with open("large.txt") as file:
    data = file.read()

# which loads everything into memory, you can process it line by line : 

with open("large.txt") as file:
    for line in file:
        process(line)
    

############### Backend Example #############


# Suppose our backend has 1 M users 

# and i do not want to load every user into at once
# Conceptually , you can proces them in a streaming/lazy way :

def get_users():
    for user in database:
        yield user

for user in get_users():
    process(user)




############### Infinite Generator 

# generators can produce values forever : 

def numbers():

    i = 1
    while True:
        yield i
        i += 1

generator = numbers()

print(next(generator))
print(next(generator))
print(next(generator))


################ Generator Function and Normal Function ######

## Normal Function 

def get_numbers():
    return [1,2,3,4,5]   # Returns the List

## Generator Function 

def get_numbers():
    yield 1
    yield 2
    yield 3
    yield 4
    yield 5

# It returns : Generator 

# Main Difference : 

return -> Function ends
yield -> Function pauses -> Can continue later 



############## Important Example ##############

# Consider : 

def test():

    print("A")

    yield 1

    print("B")

    yield 2

    print("C")

generator = test()  # nothing prints

print(next(generator))

# Output : 
# A
# 1

print(next(generator))

#Output : 
# B
# 2



def count_numbers(limit):
    for i in range(1, limit+1):
        yield i

numbers = count_numbers(5)

print(next(numbers))
print(next(numbers))
print(next(numbers))

print("Using for loop : ")

for number in numbers:
    print(number)




