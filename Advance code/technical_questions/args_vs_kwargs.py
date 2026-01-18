# *args: Takes multiple non-keyword arguments as a tuple
def add_numbers(*args):
    total = 0
    for num in args:
        total += num
    return total

# **kwargs: Takes multiple keyword arguments as a dictionary
def print_info(**kwargs):
    for key, value in kwargs.items():
        print(f"{key}: {value}")

# Using *args
print(add_numbers(1, 2, 3))  # Output: 6
print(add_numbers(10, 20, 30, 40))  # Output: 100

# Using **kwargs
print_info(name="Rahul", age=20)  # Output: name: Rahul
                                  #         age: 20

# Combining both
def combine(*args, **kwargs):
    print("Numbers:", args)  # Tuple of numbers
    print("Info:", kwargs)   # Dictionary of named arguments

combine(1, 2, 3, name="Amit", city="Delhi")
# Output: Numbers: (1, 2, 3)
#         Info: {'name': 'Amit', 'city': 'Delhi'}
