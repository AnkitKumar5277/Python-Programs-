filter(function, iterable)

num = [1,2,3,4,5,6,7,8,9,10]
even_numbers = list(filter(lambda x: x % 2 == 0, num))
print(even_numbers)

words = ["apple", "banana", "cherry", "kiwi", "grape"]
long_words = list(filter(lambda word: len(word) > 5, words))
print(long_words)

strings = ["hello","", "world", " ", "python", ""]
empty = list(filter(lambda s: s.strip() != "", strings))
print(empty)

num = [-10, -5, 0, 5, 10, 15, -3, 8, -1]
pos = list(filter(lambda x: x>=0, num))
print(pos)
