
---

## 🧩 LEVEL 2 — Python Basics with Examples

---

### 🔹 **1. Variable**

Variable ek container hota hai jo value ko store karta hai.

```python
# Example of variables
name = "Ankit"
age = 21
pi = 3.14

print(name)
print(age)
print(pi)
```

---

### 🔹 **2. Assignment Operator (=)**

Value ko variable me assign karne ke liye use hota hai.

```python
x = 10      # x me 10 store hua
y = x + 5   # y me 15 store hua
print("x =", x)
print("y =", y)
```

---

### 🔹 **3. Keywords**

Reserved words jo Python me predefined meaning rakhte hain.

```python
# Example of keywords
# True, False, if, else, while, for etc.
is_python_easy = True
if is_python_easy:
    print("Yes! Python is easy.")
```

> 💡 Check all keywords:

```python
import keyword
print(keyword.kwlist)
```

---

### 🔹 **4. Identifier**

Function, class, variable ke names hote hain.

```python
# Valid identifiers
my_name = "John"
_age = 20
marks1 = 88

print(my_name, _age, marks1)
```

---

### 🔹 **5. Literals**

Fixed values (constants) jo change nahi hote.

```python
# Different types of literals
a = 25          # Integer literal
b = 3.44        # Float literal
c = "Python"    # String literal
d = True        # Boolean literal

print(a, b, c, d)
```

---

### 🔹 **6. Datatypes**

Python automatically data ka type identify karti hai.

```python
a = 10          # int
b = 3.14        # float
c = "Ankit"     # string
d = [1, 2, 3]   # list
e = (4, 5, 6)   # tuple
f = {7, 8, 9}   # set
g = {'name': 'John', 'age': 20}  # dict
h = True        # boolean
i = None        # none

print(type(a))
print(type(b))
print(type(c))
print(type(g))
```

---

### 🔹 **7. Variable Naming Rules**

✅ Allowed:

* Letters, digits, underscores
  ❌ Not allowed:
* Start with a digit
* Spaces

```python
# Correct variable names
first_name = "John"
last_name22 = "Doe"
_value = 50

# Wrong examples (will cause error)
# 1name = "Ankit"
# my name = "John"
```

---

### 🔹 **8. Operators**

#### (a) Arithmetic Operators

```python
a = 10
b = 3
print(a + b)  # Addition
print(a - b)  # Subtraction
print(a * b)  # Multiplication
print(a / b)  # Division
print(a % b)  # Modulus
print(a **2)  # Power (a to the power 2)
```

---

#### (b) Assignment Operators

```python
x = 5
x += 3   # x = x + 3
print(x) # 8

x *= 2
print(x) # 16
```

---

#### (c) Comparison Operators

```python
a = 10
b = 20
print(a == b)  # False
print(a != b)  # True
print(a > b)   # False
print(a <= b)  # True
```

---

#### (d) Logical Operators

```python
x = True
y = False

print(x and y)  # False
print(x or y)   # True
print(not x)    # False
```

---

### 🔹 **9. Type Casting (Data Type Conversion)**

Ek data type ko dusre me convert karte hain.

```python
# String to int
a = "10"
b = int(a)
print(b + 5)  # 15

# Int to float
c = float(5)
print(c)  # 5.0
```

---

### 🔹 **10. type() Function**

Data ka type identify karta hai.

```python
x = 45
print(type(x))  # <class 'int'>

y = "Python"
print(type(y))  # <class 'str'>
```

---

### 🔹 **11. input() Function**

User se input lene ke liye use hota hai (always returns string).

```python
name = input("Apna naam likhiye: ")
print("Namaste", name)

age = input("Apni umar likhiye: ")
print("Aapki umar hai", age)
```

> 💡 Convert input to int:

```python
age = int(input("Enter your age: "))
print("Next year you will be:", age + 1)
```

---
