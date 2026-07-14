'''
# Lesson 4: Operators 🔢

## What is an Operator?

**Real-life example:**

Just like a calculator has `+`, `-`, `×`, and `÷` buttons to perform operations on numbers, Python has **operators** that perform operations on data!

---

# Three Main Types of Operators in Python

1. ➕ **Arithmetic Operators** – Used for mathematical calculations
2. 🔍 **Comparison Operators** – Used to compare values
3. 🔗 **Logical Operators** – Used to apply logical conditions

---

# 1️⃣ Arithmetic Operators

```python
a = 20
b = 6

print(a + b)   # Addition       → Output: 26
print(a - b)   # Subtraction    → Output: 14
print(a * b)   # Multiplication → Output: 120
print(a / b)   # Division       → Output: 3.3333...
print(a // b)  # Floor Division → Output: 3 (whole number only)
print(a % b)   # Modulus        → Output: 2 (remainder)
print(a ** b)  # Exponent       → Output: 64000000 (20 raised to the power of 6)
```

## Meaning of Each Operator

| Operator | Name             | Example   | Result     |
| -------- | ---------------- | --------- | ---------- |
| `+`      | Addition         | `10 + 3`  | `13`       |
| `-`      | Subtraction      | `10 - 3`  | `7`        |
| `*`      | Multiplication   | `10 * 3`  | `30`       |
| `/`      | Division         | `10 / 3`  | `3.333...` |
| `//`     | Floor Division   | `10 // 3` | `3`        |
| `%`      | Modulus          | `10 % 3`  | `1`        |
| `**`     | Exponent (Power) | `2 ** 3`  | `8`        |

---

## 💡 Understanding Floor Division and Modulus

```python
# Real-life example:
# There are 10 candies to distribute among 3 children.

candies = 10
children = 3

each_child = candies // children
print(each_child)      # Output: 3

remaining = candies % children
print(remaining)       # Output: 1
```

> 💡 **Tip:** The `%` operator is commonly used to check whether a number is **even or odd**.

```python
print(10 % 2)   # Output: 0 → Even (divides completely)
print(7 % 2)    # Output: 1 → Odd (remainder is 1)
```

---

# 2️⃣ Comparison Operators

Comparison operators always return **True** or **False**.

```python
a = 10
b = 20

print(a == b)   # Equal to          → False
print(a != b)   # Not equal to      → True
print(a > b)    # Greater than      → False
print(a < b)    # Less than         → True
print(a >= b)   # Greater or equal  → False
print(a <= b)   # Less or equal     → True
```

## Meaning of Each Operator

| Operator | Meaning                  | Example  | Result  |
| -------- | ------------------------ | -------- | ------- |
| `==`     | Equal to                 | `5 == 5` | `True`  |
| `!=`     | Not equal to             | `5 != 3` | `True`  |
| `>`      | Greater than             | `5 > 3`  | `True`  |
| `<`      | Less than                | `5 < 3`  | `False` |
| `>=`     | Greater than or equal to | `5 >= 5` | `True`  |
| `<=`     | Less than or equal to    | `3 <= 5` | `True`  |

> ⚠️ **Common Mistake**
>
> * `=` means **assign a value**
> * `==` means **compare two values**

```python
x = 10          # Assign 10 to x
print(x == 10)  # Check whether x is equal to 10 → True
```

---

# 3️⃣ Logical Operators

```python
a = 10
b = 20
c = 30

# AND - Both conditions must be True
print(a < b and b < c)    # True
print(a < b and b > c)    # False

# OR - At least one condition must be True
print(a > b or b < c)     # True
print(a > b or b > c)     # False

# NOT - Reverses the result
print(not True)           # False
print(not False)          # True
print(not a > b)          # True
```

## Truth Table

| Operator | Meaning                        | Example          | Result  |
| -------- | ------------------------------ | ---------------- | ------- |
| `and`    | Both conditions must be True   | `True and True`  | `True`  |
| `and`    | One False makes result False   | `True and False` | `False` |
| `or`     | At least one condition is True | `True or False`  | `True`  |
| `or`     | Both conditions False          | `False or False` | `False` |
| `not`    | Reverses the result            | `not True`       | `False` |

### Real-life Example

```python
# Passing an exam

maths = 85
science = 72

# Student must pass both subjects
passed = maths >= 33 and science >= 33
print("Passed both subjects:", passed)

# Distinction if at least one subject has 90 or more marks
distinction = maths >= 90 or science >= 90
print("Distinction:", distinction)
```

---

# Assignment Operators (Shortcut Operators) 🔧

```python
# These operators update variable values quickly.

score = 100

score += 10    # score = score + 10   → 110
score -= 20    # score = score - 20   → 90
score *= 2     # score = score * 2    → 180
score //= 3    # score = score // 3   → 60
score **= 2    # score = score ** 2   → 3600

print(score)
```

---

# Real-Life Program – Simple Calculator 🧮

```python
# Simple Calculator Program

num1 = 50
num2 = 8

print("=== Calculator ===")
print("Addition:", num1 + num2)
print("Subtraction:", num1 - num2)
print("Multiplication:", num1 * num2)
print("Division:", num1 / num2)
print("Floor Division:", num1 // num2)
print("Modulus:", num1 % num2)
print("Power:", num1 ** 2)

print("\n=== Comparison ===")
print("num1 > num2 ?", num1 > num2)
print("num1 == num2 ?", num1 == num2)

print("\n=== Logical ===")
print("Both numbers are positive?", num1 > 0 and num2 > 0)
```

---

# Common Mistakes ⚠️

```python
# ❌ Mistake 1: Confusing = and ==
if x = 10:      # Error!
if x == 10:     # ✅ Correct

# ❌ Mistake 2: Performing math on a string
print("10" + 5)        # Error!
print(int("10") + 5)   # ✅ Output: 15

# ❌ Mistake 3: Confusing / and //
print(10 / 2)    # Output: 5.0 (float)
print(10 // 2)   # Output: 5 (integer)
```

---

# 🎓 Important Exam/Interview Questions

1. What is the difference between `/` and `//`?
2. What does the `%` operator do? Give an example.
3. What is the difference between `=` and `==`?
4. When are `and`, `or`, and `not` operators used?
5. What does the `+=` operator mean?

---

# 📝 Practice Questions

### Q1.

Write a program that:

* Takes `a = 17` and `b = 5`
* Uses all arithmetic operators
* Checks whether `17` is even or odd using `%`

---

### Q2.

Write a program that:

* Takes marks of three subjects (choose any values)
* Calculates the total and percentage
* Checks whether the student has passed (`>= 33` in every subject)

---

### Q3.

Predict the output:

```python
x = 15
y = 4

print(x // y)
print(x % y)
print(x ** 2)
print(x == 15)
print(x != y)
```

---

### Q4.

Use logical operators:

* Check whether `age = 20` is **greater than 18 and less than 60**.
* Check whether `marks = 85` is **greater than 90 or greater than 75**.

---

### Q5. Exam Question

What will be the output of the following?

```python
10 / 3
10 // 3
```

## **Answers to Practice Questions (Lesson 4: Operators)**

---

# ✅ Q1. Write a program using all arithmetic operators and check whether 17 is even or odd.

```python
a = 17
b = 5

print("Addition:", a + b)
print("Subtraction:", a - b)
print("Multiplication:", a * b)
print("Division:", a / b)
print("Floor Division:", a // b)
print("Modulus:", a % b)
print("Power:", a ** b)

# Check Even or Odd
if a % 2 == 0:
    print(a, "is Even")
else:
    print(a, "is Odd")
```

### **Output**

```
Addition: 22
Subtraction: 12
Multiplication: 85
Division: 3.4
Floor Division: 3
Modulus: 2
Power: 1419857
17 is Odd
```

---

# ✅ Q2. Write a program to calculate total, percentage, and check whether the student has passed.

```python
math = 75
science = 82
english = 68

total = math + science + english
percentage = total / 3

print("Total Marks:", total)
print("Percentage:", percentage)

if math >= 33 and science >= 33 and english >= 33:
    print("Result: Pass")
else:
    print("Result: Fail")
```

### **Output**

```
Total Marks: 225
Percentage: 75.0
Result: Pass
```

---

# ✅ Q3. Predict the Output

### Program

```python
x = 15
y = 4

print(x // y)
print(x % y)
print(x ** 2)
print(x == 15)
print(x != y)
```

### **Output**

```
3
3
225
True
True
```

### **Explanation**

* `15 // 4 = 3`
* `15 % 4 = 3`
* `15 ** 2 = 225`
* `15 == 15` → `True`
* `15 != 4` → `True`

---

# ✅ Q4. Use Logical Operators

```python
age = 20

print(age > 18 and age < 60)

marks = 85

print(marks > 90 or marks > 75)
```

### **Output**

```
True
True
```

### **Explanation**

* `20 > 18` ✅ and `20 < 60` ✅ → `True`
* `85 > 90` ❌ or `85 > 75` ✅ → `True`

---

# ✅ Q5. What is the output of `10 / 3` and `10 // 3`? Explain the difference.

### Program

```python
print(10 / 3)
print(10 // 3)
```

### **Output**

```
3.3333333333333335
3
```

### **Difference**

| `/` (Division)                         | `//` (Floor Division)                                           |
| -------------------------------------- | --------------------------------------------------------------- |
| Returns the exact division result.     | Returns only the whole number part.                             |
| Output type is `float`.                | Output type is usually `int` (when both operands are integers). |
| Example: `10 / 3 = 3.3333333333333335` | Example: `10 // 3 = 3`                                          |

---

# 🎓 Theory Answers (Important Exam Questions)

### **1. What is the difference between `/` and `//`?**

* `/` returns the exact division result as a **float**.
* `//` returns only the **whole number** by removing the decimal part.

**Example**

```python
10 / 3   # 3.3333333333333335
10 // 3  # 3
```

---

### **2. What does the `%` operator do? Give an example.**

The `%` (Modulus) operator returns the **remainder** after division.

**Example**

```python
10 % 3   # 1
15 % 4   # 3
```

It is commonly used to check whether a number is **even or odd**.

```python
8 % 2    # 0 (Even)
9 % 2    # 1 (Odd)
```

---

### **3. What is the difference between `=` and `==`?**

| `=`                               | `==`                      |
| --------------------------------- | ------------------------- |
| Assignment Operator               | Comparison Operator       |
| Assigns a value to a variable     | Compares two values       |
| Does not return `True` or `False` | Returns `True` or `False` |

**Example**

```python
x = 10
print(x == 10)
```

**Output**

```
True
```

---

### **4. When are `and`, `or`, and `not` operators used?**

* **`and`** → Returns `True` only if **both conditions** are true.
* **`or`** → Returns `True` if **at least one condition** is true.
* **`not`** → Reverses the result (`True` becomes `False`, and `False` becomes `True`).

**Example**

```python
print(5 > 3 and 10 > 8)
print(5 > 10 or 8 > 3)
print(not True)
```

**Output**

```
True
True
False
```

---

### **5. What does the `+=` operator mean?**

The `+=` operator adds a value to the existing variable and stores the updated result in the same variable.

**Example**

```python
score = 100
score += 20
print(score)
```

**Output**

```
120
```

**Equivalent Code**

```python
score = score + 20
```

The `+=` operator is simply a shorter and cleaner way to write the same operation.


'''