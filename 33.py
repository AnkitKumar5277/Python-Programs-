# Python Program to Find Sum of Natural Numbers Using Recursion
def sum(n):
  if n<=1:
    return n
  else
    return n + sum(n-1)
num = 16
if num < 0:
   print("Enter a positive number")
else:
   print("The sum is",recur_sum(num))
# The sum is 136
