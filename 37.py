# Matrix Transpose using Nested Loop
# Program to transpose a matrix using a nested loop
X = [[12,7],
    [4 ,5],
    [3 ,8]]
result = [[0,0,0],
         [0,0,0]]
# iterate through rows
for i in range(len(X)):
   # iterate through columns
   for j in range(len(X[0])):
       result[j][i] = X[i][j]
for r in result:
   print(r)
# [12, 4, 3]
# [7, 5, 8]

''' Program to transpose a matrix using list comprehension'''
X = [[12,7],
    [4 ,5],
    [3 ,8]]
result = [[X[j][i] for j in range(len(X))] for i in range(len(X[0]))]
for r in result:
   print(r)
