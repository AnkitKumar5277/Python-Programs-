# Python Program to Find LCM
# Python Program to find the L.C.M. of two input number
def compute_lcm(x, y):
   # choose the greater number
   if x > y:
       greater = x
   else:
       greater = y
   while(True):
       if((greater % x == 0) and (greater % y == 0)):
           lcm = greater
           break
       greater += 1
   return lcm
num1 = 54
num2 = 24
print("The L.C.M. is", compute_lcm(num1, num2))
# The L.C.M. is 216
# Number1 * Number2 = L.C.M. * G.C.D.
# Program to Compute LCM Using GCD
# Python program to find the L.C.M. of two input number

# This function computes GCD 
def compute_gcd(x, y):
   while(y):
       x, y = y, x % y
   return x
# This function computes LCM
def compute_lcm(x, y):
   lcm = (x*y)//compute_gcd(x,y)
   return lcm
num1 = 54
num2 = 24 
print("The L.C.M. is", compute_lcm(num1, num2))

Write a function to calculate the lowest common multiple (LCM) of two numbers.

# The formula to calculate LCM is lcm(a, b) = abs(a*b) // gcd(a, b), where gcd() is the greatest common divisor of a and b.
# For example, with inputs 12 and 15, the output should be 60.
import math
def lcm(a, b):
    # Find the greatest common divisor (GCD) of a and b
    gcd = math.gcd(a, b)
    # Use the formula to calculate LCM
    return abs(a * b) // gcd
# Example usage
print(lcm(12, 15))  # Output: 60


