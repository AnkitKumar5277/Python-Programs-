while True:
  n1 = int(input("enter: "))
  n2 = int(input("enter: "))
  print(n1 + n2)

# Python Program to Display the multiplication Table
num = int(input("Display multiplication table of? "))
for i in range(1, 11):
   print(num, 'x', i, '=', num*i)
# output
# 12 x 1 = 12
# 12 x 2 = 24
# 12 x 3 = 36
# 12 x 4 = 48
# 12 x 5 = 60
# 12 x 6 = 72
# 12 x 7 = 84
# 12 x 8 = 96
# 12 x 9 = 108
# 12 x 10 = 120

# Python Program to Find HCF or GCD
def compute_hcf(x,y):
  if x>y:
    smaller = y
  else:
    smaller = x
  for i in range(1, smaller+1):
    if((x%i==0) and (y%i==0)):
      hcf = i
      return hcf
num1 = 54
num2 = 24
print("the h.c.f. is", compute_hcf(num1, num2))
# output
# The H.C.F. is 6

# Source Code: Using the Euclidean Algorithm
def compute_hcf(x,y):
  while(y):
    x,y = x&y
  return x
hcf = compute_hcf(300, 400)
print("the hcf is", hcf)
# The HCF is 100
