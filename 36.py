# Python Program to Add Two Matrices
# Program to add two matrices using nested loop
X = [[12,7,3],
    [4 ,5,6],
    [7 ,8,9]]
Y = [[5,8,1],
    [6,7,3],
    [4,5,9]]
result = [[0,0,0],
         [0,0,0],
         [0,0,0]]
# iterate through rows
for i in range(len(X)):
   # iterate through columns
   for j in range(len(X[0])):
       result[i][j] = X[i][j] + Y[i][j]
for r in result:
   print(r)
# [17, 15, 4]
# [10, 12, 9]
# [11, 13, 18]

# Source Code: Matrix Addition using Nested List Comprehension
X = [[12,7,3],
    [4 ,5,6],
    [7 ,8,9]]
Y = [[5,8,1],
    [6,7,3],
    [4,5,9]]
result = [[x[i][j]+y[i][j] for j in range(len(x[0]))] for i in range(len(x))]
for r in result:
    print(r)
