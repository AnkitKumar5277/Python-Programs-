# Python program to check if the input number is odd or even.
# A number is even if division by 2 gives a remainder of 0.
# If the remainder is 1, it is an odd number.
num = int(input("Enter a number: "))
if (num % 2) == 0:
   print("{0} is Even".format(num))
else:
   print("{0} is Odd".format(num))

# Enter a number: 43
# 43 is Odd
# Enter a number: 18
# 18 is Even

# Challenge:
# Write a function to check if the entered integer is odd or even.
def check_odd_or_even(number):
    """
    Determines if a given number is odd or even.
    
    Args:
        number (int): The number to be checked.
    
    Returns:
        str: "Odd" if the number is odd, "Even" if the number is even.
    """
    if number % 2 == 0:
        return "Even"
    else:
        return "Odd"

# Example usage:
print(check_odd_or_even(4))  # Output: Even
print(check_odd_or_even(7))  # Output: Odd



