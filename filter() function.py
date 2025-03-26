

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

# lambda arguments: expression
# square = lambda x: x**2
# print(square(2))

add = lambda x, y: x + y
print(add(8, 2))

nums = [1,2,3,4]
square = list(map(lambda x: x **2, nums))
print(square)

nums = [1, 2, 3, 4, 5, 6]
evens = list(filter(lambda x: x % 2 == 0, nums))
print(evens)

pairs = [(1, 2), (4, 1), (3, 3)]
sort = sorted(pairs, key = lambda x: x[1])
print(sort)

# map function
# map(function, iterable, ...)
num = [1, 2, 3, 4, 5]
square = map(lambda x: x**2, num)
print(list(square))

names = ['john', 'sam', 'linda']
upper_names = map(str.upper, names)
print(list(upper_names))

a = [1, 2, 3]
b = [4, 5, 6]
sum_ab = map(lambda x, y: x + y, a, b)
print(list(sum_ab))

string_numbers = ['1', '2', '3']
integers = map(int, string_numbers)
print(list(integers))

words = ["python", "data", "science", "analytics"]
lengths = map(len, words)
print(list(lengths))
