# Python Program to Check Whether a String is Palindrome or Not
my_str='aIbohPhoBiA'
my_str = my_str.casefold()
rev_str = reversed(my_str)
if list(my_str) == list(rev_str):
  print("the string is a palindrom.")
else:
  print("the string is not a palindrome")
# The string is a palindrome.


# Example 10: Floyd's Triangle
# 1
# 2 3
# 4 5 6
# 7 8 9 10
rows = int(input("enter: ")
number = 1
for i in range(1, rows+1):
  for j in range(1, i+1):
    print(number, end= " ")
    number += 1
  print()
