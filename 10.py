# Python Program to Print the Fibonacci sequence
# Program to display the Fibonacci sequence up to n-th term
nterms = int(input("How many terms? "))
# first two terms
n1, n2 = 0, 1
count = 0
# check if the number of terms is valid
if nterms <= 0:
   print("Please enter a positive integer")
# if there is only one term, return n1
elif nterms == 1:
   print("Fibonacci sequence upto",nterms,":")
   print(n1)
# generate fibonacci sequence
else:
   print("Fibonacci sequence:")
   while count < nterms:
       print(n1)
       nth = n1 + n2
       # update values
       n1 = n2
       n2 = nth
       count += 1
# #output 
# How many terms? 7
# Fibonacci sequence:
# 0
# 1
# 1
# 2
# 3
# 5
# 8

#challenge
def fibonacci_less_than(n):
    # Start with the first two Fibonacci numbers
    sequence = [0, 1]
    # Keep adding numbers to the list until the next one is too big
    while True:
        next_number = sequence[-1] + sequence[-2]  # Add the last two numbers
        if next_number >= n:  # Stop if the next number is too big
            break
        sequence.append(next_number)  # Add the next number to the list
    return sequence


# Python Program to Display Powers of 2 Using Anonymous Function
# Display the powers of 2 using anonymous function
# terms = 10
# Uncomment code below to take input from the user
terms = int(input("How many terms? "))
# use anonymous function
result = list(map(lambda x: 2 ** x, range(terms)))
print("The total terms are:",terms)
for i in range(terms):
   print("2 raised to power",i,"is",result[i])
# # output
# The total terms are: 10
# 2 raised to power 0 is 1
# 2 raised to power 1 is 2
# 2 raised to power 2 is 4
# 2 raised to power 3 is 8
# 2 raised to power 4 is 16
# 2 raised to power 5 is 32
# 2 raised to power 6 is 64
# 2 raised to power 7 is 128
# 2 raised to power 8 is 256
# 2 raised to power 9 is 512
