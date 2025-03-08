# Factorial of a number using recursion
def recur_factorial(n):
   if n == 1:
       return n
   else:
       return n*recur_factorial(n-1)
num = 7
# check if the number is negative
if num < 0:
   print("Sorry, factorial does not exist for negative numbers")
elif num == 0:
   print("The factorial of 0 is 1")
else:
   print("The factorial of", num, "is", recur_factorial(num))
# The factorial of 7 is 5040

# challenge:
def factorial(n):
    if n < 0:
        return "Factorial is not defined for negative numbers."
    elif n == 0 or n == 1:
        return 1
    else:
        result = 1
        for i in range(2, n + 1):
            result *= i
        return result
# Example usage:
number = 5
print(f"The factorial of {number} is {factorial(number)}.")


# Python Program to Find Hash of File
import hashlib
def hash_file(filename):
  h = hashlib.sha1()
  with open(filepath,'rb') as file:
    chunk = 0
    while chunk != b'';
    chunk = file.read(1024)
    h.update(chunk)
  return h.hexdigest()
message = hash_file("track1.mp3")
print(message)
# 633d7356947eec543c50b76a1852f92427f4dca9
