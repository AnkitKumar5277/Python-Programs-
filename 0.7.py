# Program to check if a number is prime or not
num = int(input("Enter a number: "))
flag = False
if num == 0 or num == 1:
    print(num, "is not a prime number")
elif num > 1:
    for i in range(2, num):
        if (num % i) == 0:
            flag = True
            # break out of loop
            break
    # check if flag is True
    if flag:
        print(num, "is not a prime number")
    else:
        print(num, "is a prime number")

num = int(input("Enter a number: "))
if num == 0 or num == 1:
    print(num, "is not a prime number")
elif num > 1:
   # check for factors
   for i in range(2,num):
       if (num % i) == 0:
           print(num,"is not a prime number")
           print(i,"times",num//i,"is",num)
           break
   else:
       print(num,"is a prime number")
# if input number is less than
# or equal to 1, it is not prime
else:
   print(num,"is not a prime number")
# Write a function to check whether a number is prime or not.
# For example, for input 7, the output should be True.

def is_prime(number):
    """
    Check if a number is a prime number.
    Args:
    number (int): The number to check.
    Returns:
    bool: True if the number is prime, False otherwise.
    """
    if number <= 1:  # Numbers less than or equal to 1 are not prime
        return False
    if number <= 3:  # 2 and 3 are prime
        return True
    if number % 2 == 0 or number % 3 == 0:  # Eliminate multiples of 2 and 3
        return False
    # Check divisors from 5 to √number
    i = 5
    while i * i <= number:
        if number % i == 0 or number % (i + 2) == 0:
            return False
        i += 6
    return True
# Example usage
print(is_prime(7))  # Output: True

# Python program to display all the prime numbers within an interval
lower = 900
upper = 1000
print("Prime numbers between", lower, "and", upper, "are:")
for num in range(lower, upper + 1):
   # all prime numbers are greater than 1
   if num > 1:
       for i in range(2, num):
           if (num % i) == 0:
               break
       else:
           print(num)
# Prime numbers between 900 and 1000 are:
# 907
# 911
# 919
# 929
# 937
# 941
# 947
# 953
# 967
# 971
# 977
# 983
# 991
# 997

def is_prime_in_range(number, start, end):
    if number <= 1:
        return False  # 0 and 1 are not prime numbers
    # Check divisors in the specified range
    for divisor in range(start, end + 1):
        if divisor > 1 and divisor < number and number % divisor == 0:
            return False  # Divisible within range; not prime
    return True
# Example usage
result = is_prime_in_range(49, 2, 6)
print(result) 
# Output: True
