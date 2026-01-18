# Define a function to square a number
def square(num):
    return num * num

# List of numbers
numbers = [1, 2, 3, 4, 5]

# Use map() to apply square function to each number
squared_numbers = list(map(square, numbers))

# Print the result
print(squared_numbers)  # Output: [1, 4, 9, 16, 25]
