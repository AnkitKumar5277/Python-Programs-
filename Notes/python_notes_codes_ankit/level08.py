# 🧩 1️⃣ Function Definition and Calling
# Concept: Function ek reusable block of code hota hai jise baar-baar use kar sakte hain.

# Function definition
def greet():
    print("Hello! Welcome to Python functions.")

# Function call
greet()

# 🧮 2️⃣ Function with Parameters and Return Value
# Concept: Function me hum input parameters le sakte hain aur output return kar sakte hain.
# Function with parameters
def number(a, b):
    return a + b
result = number(10, 5)
print("sum is: ", result)

# ⚙️ 3️⃣ Built-in Functions
# Concept: Python ke andar already kuch functions diye gaye hote hain jaise len(), print(), type(), etc.
text = "Python"
numbers = [10, 20, 30, 40]
print(len(text))
print(type(numbers))   # data type check
print(sum(numbers))    # sum of list elements

# 👨‍💻 4️⃣ User Defined Function
# Concept: Jab hum khud ka function banate hain.
def greet_user(name):
    print("Good day,",name)
greet_user("Ankit")

# 🧾 5️⃣ Function with Arguments and Return
# Concept: Function input leta hai aur ek value return karta hai.
def multiply(x, y):
    return x * y
product = multiply(4, 5)
print("Multiplication is : ", product)

# 🎯 6️⃣ Default Parameter Value (Default Argument)
# Concept: Agar koi argument pass na ho to ek default value use hoti hai.
def greet(name = "Stranger"):
    print("Good day,", name)
greet("Ankit")
greet()

# 🧠 7️⃣ Return Statement
# Concept: Function se value return karne ke liye use hota hai.
def square(num):
    return num * num
result = square(6)
print("Square is:", result)

# 🔁 8️⃣ Recursion (Function Calling Itself)
# Concept: Jab ek function apne aap ko call karta hai.
# Example – Factorial using recursion
def factorial(n):
    if n == 1:
        return 1
    else:
        return n * factorial(n -1)
print("factorial of 5 is:", factorial(5))

# 🧱 9️⃣ Base Condition in Recursion
# Concept: Recursion me base condition stopping point hota hai.
def countdown(n):
    if n==0:
        print("Time's up!")
    else:
        print(n)
        countdown(n-1)

countdown(5)

# ✂️ 🔟 strip() Function
# Concept: String ke starting aur ending spaces remove karta hai.
this = "    my name is ankit kumar  "
print("before strip:", this)
print("after strip", this.strip)



