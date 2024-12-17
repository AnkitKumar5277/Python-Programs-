# Python Program to Find Numbers Divisible by Another Number
# Take a list of numbers
my_list = [12, 65, 54, 39, 102, 339, 221,]
# use anonymous function to filter
result = list(filter(lambda x: (x % 13 == 0), my_list))
# display the result
print("Numbers divisible by 13 are",result)
# output
# Numbers divisible by 13 are [65, 39, 221]


# challenge
# Write a function to check if a number is divisible by five.
# Return True if the number is divisible by 5. Otherwise, return False.
def is_divisible_by_five(number):
    return number % 5 == 0
# Example usage
print(is_divisible_by_five(10))  # True
print(is_divisible_by_five(12))  # False
print(is_divisible_by_five(0))   # True
print(is_divisible_by_five(-15)) # True

