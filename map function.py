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
