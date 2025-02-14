# Program to check if a number is prime or not
# num = 29
# To take input from the user
num = int(input("Enter a number: "))
# define a flag variable
flag = False
if num == 0 or num == 1:
    print(num, "is not a prime number")
elif num > 1:
    # check for factors
    for i in range(2, num):
        if (num % i) == 0:
            # if factor is found, set flag to True
            flag = True
            # break out of loop
            break
    # check if flag is True
    if flag:
        print(num, "is not a prime number")
    else:
        print(num, "is a prime number")


# num = 407
# To take input from the user
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

