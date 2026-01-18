# 💻 My First Python Assistant - Fully Interactive Version

# 1. Welcome Message
print("👋 Welcome to Python Assistant!")
print("This assistant will display your info and help you with basic math.\n")

# 2. Input Section - Personal Info
print("📥 Enter Your Details:")
name = input("Enter your name: ")
age = input("Enter your age: ")
friend1 = input("Enter Friend 1 name: ")
friend2 = input("Enter Friend 2 name: ")
friend3 = input("Enter Friend 3 name: ")

# 3. Display User Profile
print("\n📄 Your Profile:")
print("Name:", name)
print("Age:", age)
print("Friends Info:", friend1, 234, friend2)
print("All Contacts:", friend1, 234, friend2, friend3)
print("Formatted Contacts:", end=" ")
print(friend1, 234, friend2, sep="-", end="**")
print(friend3, 234, friend2, friend1)

# 4. Separator
print("\n" + "-"*50)

# 5. Input Section - Calculator
print("🧮 Mini Calculator:")
num1 = float(input("Enter first number: "))
num2 = float(input("Enter second number: "))

# 6. Perform Operations
print(f"{num1} + {num2} =", num1 + num2)
print(f"{num1} - {num2} =", num1 - num2)
print(f"{num1} * {num2} =", num1 * num2)
if num2 != 0:
    print(f"{num1} / {num2} =", num1 / num2)
else:
    print("Division by 0 is not allowed.")

# 7. Exit Message
print("\n✅ Thank you for using Python Assistant!")
print(f"Goodbye, {name}! 👋")
