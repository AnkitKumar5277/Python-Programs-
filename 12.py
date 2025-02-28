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
