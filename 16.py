# Python Program to Find the Factorial of a Number
# Python program to find the factorial of a number provided by the user.
# change the value for a different result
# num = 7
# To take input from the user
num = int(input("Enter a number: "))
factorial = 1
# check if the number is negative, positive or zero
if num < 0:
   print("Sorry, factorial does not exist for negative numbers")
elif num == 0:
   print("The factorial of 0 is 1")
else:
   for i in range(1,num + 1):
       factorial = factorial*i
   print("The factorial of",num,"is",factorial)
   # The factorial of 7 is 5040

# iteration	factorial*i (returned value)
# i = 1	1 * 1 = 1
# i = 2	1 * 2 = 2
# i = 3	2 * 3 = 6
# i = 4	6 * 4 = 24
# i = 5	24 * 5 = 120
# i = 6	120 * 6 = 720
# i = 7	720 * 7 = 5040

# Python program to find the factorial of a number provided by the user
# using recursion
def factorial(x):
    """This is a recursive function
    to find the factorial of an integer"""
    if x == 1 or x == 0:
        return 1
    else:
        # recursive call to the function
        return (x * factorial(x-1))
# change the value for a different result
num = 7
# to take input from the user
num = int(input("Enter a number: "))
# call the factorial function
result = factorial(num)
print("The factorial of", num, "is", result)

Write a function to calculate the factorial of a number.

# The factorial of a non-negative integer n is the product of all positive integers less than or equal to n.
# For example, for input5, the output should be 120
def factorial(n):
    if n < 0:
        raise ValueError("Factorial is not defined for negative numbers.")
    result = 1
    for i in range(1, n + 1):
        result *= i
    return result
# Example usage
number = 5
print(f"The factorial of {number} is {factorial(number)}")



