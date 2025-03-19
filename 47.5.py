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
    
