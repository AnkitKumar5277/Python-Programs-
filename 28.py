# Python Program to find the factors of a number
# This function computes the factor of the argument passed
def print_factors(x):
   print("The factors of",x,"are:")
   for i in range(1, x + 1):
       if x % i == 0:
           print(i)

num = 320

print_factors(num)
# The factors of 320 are:
# 1
# 2
# 4
# 5
# 8
# 10
# 16
# 20
# 32
# 40
# 64
# 80
# 160
# 320
