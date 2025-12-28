# 1️⃣ Python — High Level Programming Language
# Simple Python code
print("Hello, Python!")   # Output: Hello, Python!

# 2️⃣ Programming Language
# High level (Python) -> Low level (Machine code)
x = 10
y = 20
print(x + y)  # Output: 30

# 3️⃣ File Extension
# Python file ka extension .py hota hai
# Example: my_first_program.py
print("This is a .py file")

# 4️⃣ Features Example
# Example of interpreted & simple syntax
for i in range(5):
    print("python")

# 5️⃣ Module
# math module ka use
import math
print(math.sqrt(16))
print(math.pi)

# 6️⃣ Custom Module
# my_module.py
def greet(name):
    return f"Hello, {name}!"

# main.py
# import my_module
# print(my_module.greet("Ankit"))

# 7️⃣ Package
# Structure:
# my_package/
#     __init__.py
#     greetings.py

# greetings.py
def say_hi():
    print("hi from package!")

# main.py
# from my_package import greetings
# greetings.say_hi()

# 8️⃣ pip (Package Manager)
# Terminal Commands
# pip install pandas
# pip list
# pip uninstall pandas
# pip install --upgrade pandas

# 9️⃣ Import Example
import random
print(random.randint(1,10))

# 🔟 Comments
# This is a single-line comment

"""
This is a
multi-line comment
"""
print("Comments help explain code")

# 11️⃣ REPL (Read Evaluate Print Loop)
# open python shell and type:
# >>> 5+3
# output: 8
# >>> exit()

# 12️⃣ Escape Sequence
print("hello\nworld")
print("this is a tab\tspace")

# 13️⃣ .listdir()
import os
print(os.listdir())

# 14️⃣ Indentation
for i in range(3):
    print("indented line")

# 15️⃣ Namespace
a = 10
b = 20
print(globals())

# 16️⃣ Case Sensitive
name = "ankit"
Name = "ANKIT"

# 17️⃣ PEP 8 (Coding Style)
def greet_user(name):
    print(f"Hello,{name}!")
def GreetUser(Name):print("Hi",Name)

# 18️⃣ Output
name = "python"
version = 3
print("i am learning",name,"version",version)
# or
print(f"i am learning{name} version {version}")
