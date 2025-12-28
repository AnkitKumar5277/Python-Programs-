# 1. Class and Object
# Class is a blueprint for creating objects. Objects are instances of a class.
class Employee:
    company = "TechCorp"

    def __init__(self, name, age, salary):
        self.name = name
        self.age = age
        self.salary = salary

    def get_salary(self):
        return self.salary

    def increment(self, amount):
        self.salary += amount
        return self.salary

emp1 = Employee("Alice", 30, 50000)
emp2 = Employee("Bob", 25, 45000)

print(f"Employee 1: {emp1.name}, Age: {emp1.age}, Salary {emp1.get_salary()}, Company: {emp1.company}")
print(f"Employee 2: {emp2.name}, Age: {emp2.age}, Salary {emp2.get_salary()}, Company: {emp2.company}")

emp1.increment(5000)
print(f"Employee 1 after increment: {emp1.get_salary()}")

# 2. Class Attribute vs Instance Attribute
# Class attributes belong to the class, instance attributes belong to the object.
class Sample:
    a = "Ankit"
obj = Sample()
obj.a = "Vikky"
Sample.a = "Rohan"
print(f"Class attribute: {Sample.a}")
print(f"Instance attribute: {obj.a}")

# 3. Self Parameter
# 'self' refers to the instance calling the method. It is automatically passed.
class Cat:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def info(self):
        print(f"I am a cat My name is {self.name}. I am {self.age} years old.")

    def make_sound(self):
        print("Meow")

cat = Cat("Whiskers", 3)
cat.info()
cat.make_sound()

# 4. Static Method
# Static methods don’t require self and are decorated with @staticmethod.
class StaticExample:
    @staticmethod
    def greet():
        print("Hello, I am a static method!")

StaticExample.greet()
obj = StaticExample
obj.greet()

# 5. Constructor (__init__)
# Constructor is called automatically when an object is created.
class Programmer:
    company = "Microsoft"

    def __init__(self, name, salary, pin):
        self.name = name
        self.salary = salary
        self.pin = pin
        print(f"Programmer {self.name} intialized with salary {self.salary} and pin {self.pin}")
p = Programmer("Ankit", 120000000, 240011)
print(f"{p.name}, {p.salary}, {p.pin}, {p.company}")

r = Programmer("Rohan", 1200000, 340000)
print(f"{r.name}, {r.salary}, {r.pin}, {r.company}")



# 1. Class and Object
# Class is a blueprint for creating objects. Objects are instances of a class.
class Employee:
    # Class attribute (shared by all objects)
    company = "TechCorp"

    def show_details(self):
        print(f"Employee works at {self.company}")

emp1 = Employee()   # instance attribute
emp2 = Employee()
emp1.show_details()
emp2.show_details()

# 2. Class vs Instance Attributes
# Class attributes belong to the class, instance attributes belong to specific objects
class Sample:
    a = "Ankit" #class attribute

# creating an object
obj = Sample()
obj.a = "Vikky" #instance attribute
Sample.a = "Rohan" # changing class attribute

print(Sample.a)
print(obj.a)

# 3. Self Parameter
# Self refers to the instance calling the method
class Cat:
    def __init__(self, name, age):
        self.name = name #instance
        self.age = age #instance

    def info(self):
        print(f"i am a cat. My name is {self.name} i am {self.age} years old")

#creating object and calling method
cat1 = Cat("Whiskers", 3)
cat1.info()

# Creating object and calling method
cat1 = Cat("Whiskers", 3)
cat1.info()

# 4. static method
# Static methods don't use self and are marked with @staticmethod
class StaticExample:
    @staticmethod
    def greet():
        print("Hello from static method !")

obj = StaticExample()
obj.greet()
StaticExample.greet()

# calling static method without self
obj = StaticExample()
obj.greet()
StaticExample.greet()

# 5. Constructor (__init__)
# Constructor initializes objects when they are created
class Programmer:
    company = "Microsoft" # class attribute

    def __init__(self, name, salary, pin):
        self.name = name
        self.salary = salary
        self.pin = pin

    def show_info(self):
        print(f"name : {self.name}, salary: {self.salary}, pin : {self.pin}, company : {self.company}")

p1 = Programmer("Ankit", 12000000, 23424)
p2 = Programmer("Hayy", 12000403, 34242)
p1.show_info()
p2.show_info()

# 6. Modelling a Problem in OOP
# Nouns -> Class (e.g., Car)
# Adjectives -> Attributes (e.g., color, speed)
# Verbs -> Methods (e.g., drive, stop)
class Car:
    def __init__(self, color, speed):
        self.color = color
        self.speed = speed

    def drive(self):
        print(f"the {self.color} car is driving at {self.speed} km/n")

    def stop(self):
        print(f"the {self.color} car has stopped")

    #creating object and using methods
car1 = Car("Red", 120)
car1.drive()
car1.stop()

