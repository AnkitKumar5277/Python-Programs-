# Python Program to Illustrate Different Set Operations
# Program to perform different set operations like in mathematics
# define three sets
E = {0, 2, 4, 6, 8};
N = {1, 2, 3, 4, 5};
# set union
print("Union of E and N is",E | N)
# set intersection
print("Intersection of E and N is",E & N)
# set difference
print("Difference of E and N is",E - N)
# set symmetric difference
print("Symmetric difference of E and N is",E ^ N)
# # output
# Union of E and N is {0, 1, 2, 3, 4, 5, 6, 8}
# Intersection of E and N is {2, 4}
# Difference of E and N is {8, 0, 6}
# Symmetric difference of E and N is {0, 1, 3, 5, 6, 8}

# Python Program to Safely Create a Nested Directory
 
# Example 1: Using pathlib.Path.mkdir
from pathlib import Path
Path("/root/dirA/dirB").mkdir(parents=True, exist_ok=True)

# Example 2: Using os.makedirs
import os
os.makedirs("/root/dirA/dirB")

# Example 3: Using distutils.dir_util
import distutils.dir_util
distutils.dir_util.mkpath("/root/dirA/dirB")

# Example 4: Raising an exception if directory already exists
import os
try:
    os.makedirs("/dirA/dirB")
except FileExistsError:
    print("File already exists")

# Python Program to Remove Punctuations From a String
punctuations = '''!()-[]{};:'"\,<>./?@#$%^&*_~'''
my_str = "Hello!!!, he said ---and went."
no_punct = ""
for char in my_str:
  if char not in punctuations:
    no_punct = no_punct + char
print(no_punct)
# Hello he said and went

# Python Program to Multiply Two Matrices
x = [[12,7,3],
     [4,5,6],
     [7,8,9]]
y = [5,8,1,2],
    [6,7,3,0],
    [4,5,9,1]]
result = [[0,0,0,0],
          [0,0,0,0],
          [0,0,0,0]]
for i in range(len(x)):
  for j in range(len(y[0])):
    for k in range(len(y)):
      result[i][j] += x[i][k] * y[k][j]
for r in result:
  print(r)
# output
# [114, 160, 60, 27]
# [74, 97, 73, 14]
# [119, 157, 112, 23]

# Program to multiply two matrices using list comprehension
X = [[12,7,3],
    [4 ,5,6],
    [7 ,8,9]]
Y = [[5,8,1,2],
    [6,7,3,0],
    [4,5,9,1]]
result = [[sum(a*b for a,b in zip(x_row, y_col)) for y_col in zip(*y)] for x_row in x]
for r in result:
     print(r)
     

