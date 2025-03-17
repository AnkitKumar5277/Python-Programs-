# Python Program to Find the Sum of Natural Numbers
# Sum of natural numbers up to num
num = 16
if num < 0:
   print("Enter a positive number")
else:
   sum = 0
   # use while loop to iterate until zero
   while(num > 0):
       sum += num
       num -= 1
   print("The sum is", sum)
   # The sum is 136

# Write a function to find the sum of first N natural numbers.
# Hint: The formula for the sum of the first N natural numbers is N*(N+1)/2.
# For example, for input 5, the outout should be 15.
def sum_of_natural_numbers(n):
    if n < 1:
        return "Input must be a positive integer."
    return n * (n + 1) // 2  # Using integer division for an exact result
number = 5
result = sum_of_natural_numbers(number)
print(f"The sum of the first {number} natural numbers is {result}.")
# or
def sum_of_natural_numbers(n):
    return n * (n + 1) // 2  # // is for whole number division
print(sum_of_natural_numbers(5))  # Output will be 15

rows = int(input("Enter number of rows: "))
k = 0
count=0
count1=0
for i in range(1, rows+1):
    for space in range(1, (rows-i)+1):
        print("  ", end="")
        count+=1
    while k!=((2*i)-1):
        if count<=rows-1:
            print(i+k, end=" ")
            count+=1
        else:
            count1+=1
            print(i+k-(2*count1), end=" ")
        k += 1
    count1 = count = k = 0
    print()


