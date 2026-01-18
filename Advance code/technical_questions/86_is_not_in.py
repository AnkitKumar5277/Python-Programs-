a = 10
b = 10
print(a is b)  # Output: True (because small integers share the same memory in Python)

x = [1, 2, 3]
y = [1, 2, 3]
print(x is y)  # Output: False (lists are different objects in memory)

is_sunny = False
print(not is_sunny)  # Output: True (not False = True)

if not is_sunny:
    print("It is raining!")  # Output: It is raining!

fruits = ["apple", "banana", "orange"]
print("apple" in fruits)  # Output: True
print("grape" in fruits)  # Output: False

name = "Hello"
print("H" in name)  # Output: True
