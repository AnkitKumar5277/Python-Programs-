# 🧩 1. String Basics
# String examples
a = 'Hello'        # single quote string
b = "World"        # double quote string
c = '''Python is
fun!'''             # triple quote string (for multi-line text)

print(a)
print(b)
print(c)

# 🧠 2. String is Immutable
s = 'Ankit'
# s[0] = 'M' ❌ This will give error (immutable)
print(s)

# 🔢 3. String Indexing and Slicing
print(s[0])
print(s[1])
print(s[-1])
print(s[0:3])
print(s[:3])
print(s[2:])
print(s[:])

# ➖ 4. Negative Indices
s = "Ankit"
print(s[-1])
print(s[-3])
print(s[-5])

# ⏩ 5. Skip Value in Slicing
print(s[::2])
print(s[::-1])

# 🧰 6. String Functions
s="hello world"
print(len(s))
print(s.endswith("world"))
print(s.capitalize())
print(s.find("world"))
print(s.replace("world","python"))

# ⚙️ 7. Escape Sequence Characters
print("Hello\nWorld")   # \n -> new line
print("Hello\tWorld")   # \t -> tab space
print("hello\\world")
# print("it\s' a nice day")

# 🧮 8. Practice Example (All in One)
name = "ankit kumar"

# capitalize
print(name.capitalize())     # Ankit kumar

# slicing
print(name[:5])              # ankit
print(name.replace("ankit","john"))
print(name[::-1])



