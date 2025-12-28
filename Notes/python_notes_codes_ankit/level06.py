# 1. Basic If Statement
# Checks if a condition is True and executes a block of code
age = 18
if age >= 18:
    print("You are eligible to vote!")

# 2. If-Else Statement
# Executes one block if condition is True, another if False
temperature = 25
if temperature > 30:
    print("It's a hot day!")
else:
    print("It's a pleasant day!")

# 3. If-Elif-Else Statement
# Checks multiple conditions in sequence
marks = 85
if marks >= 90:
    print("Grade: A+")
elif marks >= 80:
    print("Grade: A")
elif marks >= 70:
    print("Grade: B")
else:
    print("Grade: C or below")

# 4. Relational Operators
# Used to compare values in conditions
number = 10
if number == 10:  # Equal to
    print("Number is exactly 10")
if number != 5:   # Not equal to
    print("Number is not 5")
if number > 5:    # Greater than
    print("Number is greater than 5")
if number <= 10:  # Less than or equal to
    print("Number is less than or equal to 10")

# 5. Logical Operators
# Combine multiple conditions
age = 20
has_id = True
if age >= 18 and has_id:  # Both conditions must be True
    print("You can enter the club!")
if age >= 18 or has_id:   # At least one condition must be True
    print("You meet at least one requirement!")
if not has_id:            # Reverses the condition
    print("This won't print because has_id is True")

# 6. 'is' Operator
# Checks if two variables point to the same object
a = [1, 2, 3]
b = a
c = [1, 2, 3]
if a is b:  # True, because a and b point to the same list
    print("a and b are the same object")
if a is not c:  # True, because a and c are different objects
    print("a and c are different objects, even if they have the same values")

# 7. 'in' Operator
# Checks if a value exists in a sequence (list, string, etc.)
fruits = ["apple", "banana", "orange"]
if "banana" in fruits:  # Checks if "banana" is in the list
    print("Banana is in the fruits list!")
if "grape" not in fruits:  # Checks if "grape" is not in the list
    print("Grape is not in the fruits list!")

