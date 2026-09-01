## OOPS in Python

class User:
    def __intit__(self,name,age,email):
        self.name = name
        self.age = age
        self.email = email

    def introduce(self):
        print(f"Name : {slef.name}")
        print(f"Age : {self.age}")
        print(f"Email : {self.email}")

user1 = User(
    "Samir",
    20,
    "samir@gmail.com"
)

user2 = User(
    "Rahul",
    21,
    "rahul@gmail.com"
)

user1.introduce()
user2.introduce()


########### Methods Can Change Object's Data #######

class User:
    def __init__(self, name, age):
        self.name = name
        slef.age = age

    def birthday(self):
        self.age += 1


user = User("Samir", 20)

print(user.age)
user.birthday()
print(user.age)


## Class Atributes

# some time a value should be shared by all objects

class User:
    platform = "MyApp"

    def __init__(self, name):
        self.name = name

user1 = User("Samir")
user2 = User("Rahul")

print(user1.platform)  #myApp
print(user2.platform)  #MyApp


## Instance vs Class Atributes


# Instance Attribute
#         ↓
# Different for every object

# self.name
# self.age
# self.email


# Class Attributes : Same/Shared by the Class


############# Encapsulation ################

class BankAccount:
    def __init__(self, balance):
        self._balance = balance

    def get_balance(self):
        return self._balance

# _balance means : This is intented for internal use



### Dobule Underscore __

class BankAccount:
    def __init__(self, balance):
        self.__balance = balance

    def get_balance(self):
        return self.__balance

account = BankAccount(10000)
# you should not directly do this account._balance

# instead, provide a methdo
print(account.get_balance())  # 10000


# _balance
# → internal-use convention

# __balance
# → name mangling


################# Inheritance ################

# one class can reuse/extend another class

class User:
    def __init__(self, name, email):
        self.name = name
        self.email = email

class Student(User):
    def study(self):
        print(f"{self.name} is studying")


student = Student(
    "Samir",
    "samir@gmail.com"
)


# Use super() if the child class needs its own attribute too

class User:
    def __init__(self, name, email):
        self.name = name
        self.email = email

class Student(User):
    def __init__(self, name, email, course):
        super().__init__(name, email)  #it calls the parent class 
        self.course = course

s = Student(
    "Samir",
    "samir@gmail.com",
    "BTech-CSE"
)



################ Method Overriding ###############

# A child class can provide its own version of a parent method 

class User:
    def role(self):
        print("I am a user")

class Student(User):
    def role(self):
        print("I am a student")

user = User()
student = Student()

user.role()    # I am a user
student.role() # I am a student
#The child overrides the parent method




###################################

class User:
    def __init__(self, name, email):
        self.name = name
        self.email = email
    
    def get_profile(self):
        return{
            "name" : self.name,
            "email" : self.email
        }

user = User(
    "Samir",
    "samir@gmail.com"
)

print(user.get_profile())



################# Practice Code ###############

class User:

    platform = "MyApp"

    def __init__(self, name, age, email):
        self.name = name
        self.age = age
        self.email = email

    def introduce(self):
        print(f"Name: {self.name}")
        print(f"Age: {self.age}")
        print(f"Email: {self.email}")

    def birthday(self):
        self.age += 1


class Student(User):

    def __init__(self, name, age, email, course):
        super().__init__(name, age, email)
        self.course = course

    def study(self):
        print(f"{self.name} is studying {self.course}")


student = Student(
    "Samir",
    20,
    "samir@gmail.com",
    "B.Tech CSE"
)

student.introduce()
student.study()

print("Before birthday:", student.age)

student.birthday()

print("After birthday:", student.age)

print("Platform:", student.platform)



# Task 1 : Create a student calss with name, rollNo, course and a Method introducr()

class Student:
    def __init__(self, name, rollNo, course):
        self.name = name
        self.rollNo = rollNo
        self.course =  course

    def introduce(self):
        print(f"Name : {self.name}")
        print(f"Roll No : {self.rollNo}")
        print(f"Course : {self.course}")


s = Student(
    "Samir",
    101,
    "BTech CSE"
)

s.introduce()


#################################

class BankAccount:

    def __init__(self, owner, balance):
        self.owner = owner
        self.balance = balance

    def deposit(self, amount):
        self.balance += amount

    def withdraw(self, amount):

        if amount > self.balance:
            print("Insufficient balance")
        else:
            self.balance -= amount

    def get_balance(self):
        return self.balance


account = BankAccount("Samir", 1000)

account.deposit(500)
account.withdraw(200)

print(account.get_balance())

















































