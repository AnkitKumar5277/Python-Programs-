# Programs to print full pyramids
# Example 6: Program to print full pyramid using *
#         *
#       * * *
#     * * * * *
#   * * * * * * *
# * * * * * * * * *
rows = int(input("enter: "))
k = 0
for i in range(1, rows+1):
  for space in range(1, (rows-1) + 1):
    print(end = "  ")
  while k!=(2*i-1):
    print("* ", end = "")
    k+=1
  k = 0
  print()

# Example 8: Inverted full pyramid of *
# * * * * * * * * *
#   * * * * * * *
#     * * * * *
#       * * *
#         *
rows = int(input("Enter number of rows: "))
for i in range(rows, 1, -1):
    for space in range(0, rows-i):
        print("  ", end="")
    for j in range(i, 2*i-1):
        print("* ", end="")
    for j in range(1, i-1):
        print("* ", end="")
    print()

 #           1
 #         1   1
 #       1   2   1
 #     1   3   3    1
 #   1  4    6   4   1
 # 1  5   10   10  5   1

rows = int(input("enter :")
coef = 1
for i in range(1, rows+1):
 for space in range(1, rows-i+1):
  print(" ", end = "")
 for j in range(0, i):
  if j == 0 or i ==0:
   coef = 1
  else:
   coef = coef * (i - j)//j
  print(coef, end = " ")
 print()
 
# Example 2: Using the ** Operator
d1 = {1: 'a', 2: 'b'}
d2 = {2: 'c', 4: 'd'}
print({**d1, **d2})
# {1: 'a', 2: 'c', 4: 'd'}
    

# Write a function to merge two dictionaries.
# Return the merged dictionary.
# For example, for inputs {'a': 1, 'b': 2} and {'c': 3, 'd': 4}, the output should be {'a': 1, 'b': 2, 'c': 3, 'd': 4}.
def merge_dictionaries(dict1, dict2):
    merged_dict = dict1.copy()
    merged_dict.update(dict2)
    return merged_dict
dict1 = {'a': 1, 'b': 2}
dict2 = {'c': 3, 'd': 4}
merged = merge_dictionaries(dict1, dict2)
print(merged)  # Output: {'a': 1, 'b': 2, 'c': 3, 'd': 4}

# Example 5: Inverted half pyramid using numbers
# 1 2 3 4 5
# 1 2 3 4
# 1 2 3
# 1 2
# 1
rows = int(input("enter number of rows:"))
for i in range(rows, 0, -1):
  for j in range(1, i+1):
    print(j, end=" ")

  print()
  

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
