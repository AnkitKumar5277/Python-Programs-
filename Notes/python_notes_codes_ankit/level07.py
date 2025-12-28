# 🌀 1. While Loop
# 👉 Executes again and again until the condition becomes False.
i = 1
while i<=5:
    print("number:", i)
    i = i + 1

# ⚠️ Infinite While Loop
# 👉 Loop runs forever because condition is always True.
# Infinite loop (Press Ctrl + C to stop)
# while True:
    # print("This will run forever!")

# 🔁 2. For Loop
# 👉 Used to iterate (loop) through a sequence like list, tuple, string, or range.
nums = [1,2,3,4,5]
for num in nums:
    print("current numbers:", num)

# 🔢 3. Range Function
# 👉 Used to create a sequence of numbers.
for i in range(5):
    print(i)

for i in range(2, 6):
    print(i)

for i in range(1, 10, 2):
    print(i)

# 🧩 4. For Loop with Else
# 👉 The else block runs after the loop completes normally (no break used).
for i in range(3):
    print("loop value:", i)
else:
    print("loop finished successfully!")

# 🛑 5. Break Statement
# 👉 Used to exit the loop immediately.
for i in range(1, 6):
    if i == 3:
        break
    print(i)

# 🔄 6. Continue Statement
# 👉 Skips the current iteration and moves to the next one.
for i in range(1, 6):
    if i == 3:
        continue
    print(i)

# 🚫 7. Pass Statement
# 👉 Used as a placeholder when you want no action.
for i in range(5):
    if i == 2:
        pass
    else:
        print(i)

# 🧮 8. f-string
# 👉 Used for formatted output in an easy way.
num = 5
for i in range(1, 6):
    print(f"{num} X {i} = {num * i}")

# 🔤 9. .startswith() Method
# 👉 Checks if a string starts with a given word or character.
word = "Python"
if word.startswith("Py"):
    print("Yes, it starts with 'Py'  ")
else:
    print("no, it doesn't start with 'Py'  ")
