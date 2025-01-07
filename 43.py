# Python Program to Count the Number of Each Vowel
# Program to count the number of each vowels
vowels = 'aeiou'
ip_str = 'Hello, have you tried our tutorial section yet?
ip_str = ip_str.casefold()
count = {}.fromkeys(vowels,0)
for char in ip_str:
   if char in
      count[char] += 1
print(count)
# output
# {'a': 2, 'e': 5, 'i': 3, 'o': 5, 'u': 3}

# Source Code: Using a list and a dictionary comprehension
ip_str = 'Hello, have you tried our tutorial section yet?'
ip_str = ip_str.casefold()
count = {x:sum([1 for char in ip_str if char == x]) for x in 'aeiou'}
print(count)
# {'a': 2, 'e': 5, 'i': 3, 'o': 5, 'u': 3}

# Write a function to return the first N vowels from a given string.
# Return the first N vowels from the string. If there are fewer than N vowels in the string, return "Not found".
# For example, for input "Hello World", the output should be 'e', 'o', 'o'.
def first_n_vowels(string, n):
    vowels = "aeiouAEIOU"
    result = [char for char in string if char in vowels]
    if len(result) >= n:
        return result[:n]
    else:
        return "Not found"
