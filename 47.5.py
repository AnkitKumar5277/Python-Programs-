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
  
    
