# Lesson 3: Data Types 📊
'''
In **Lesson 2**, you learned about **Variables**. Now it's time to understand **what kind of data** can be stored inside those variables!

---

# What is a Data Type?

### Real-life Example

Imagine you have different containers at home:

* 🧂 **Salt container** – only for salt
* 💧 **Water bottle** – only for liquids
* 📦 **Clothes box** – only for clothes

Similarly, Python has different **data types**, and each type is designed to store a specific kind of data.

---

# Main Data Types in Python

```python
# 1. INTEGER (int) - Whole numbers (without decimal)

age = 20
roll_number = 15
marks = 450

# 2. FLOAT (float) - Decimal numbers

height = 5.9
percentage = 85.5
price = 99.99

# 3. STRING (str) - Text

name = "Rohit Kumar"
city = "Siwan"
message = "Hello Python!"

# 4. BOOLEAN (bool) - Only two values: True or False

is_student = True
is_passed = False
has_phone = True
```

---

# Details of Each Data Type

## 1️⃣ INTEGER (int) – Whole Numbers

```python
# Whole numbers (positive or negative)

roll = 42
temperature = -5
population = 1000000

print(roll)         # Output: 42
print(temperature)  # Output: -5

# type() tells the data type

print(type(roll))   # Output: <class 'int'>
```

### Real-life Examples

* Roll number
* Age
* Total marks
* Population

All of these are integers.

---

## 2️⃣ FLOAT (float) – Decimal Numbers

```python
# Numbers with decimal points

price = 49.99
weight = 65.5
pi = 3.14159

print(price)        # Output: 49.99
print(type(price))  # Output: <class 'float'>
```

### Real-life Examples

* Percentage
* Height
* Weight
* Product price

These are all float values.

---

## 3️⃣ STRING (str) – Text Data

```python
# Any text enclosed in single or double quotes

first_name = "Rohit"
last_name = 'Kumar'
address = "Siwan, Bihar"

print(first_name)          # Output: Rohit
print(type(first_name))    # Output: <class 'str'>

# Some useful string methods

print(len("Rohit"))        # Output: 5
print("Rohit".upper())     # Output: ROHIT
print("ROHIT".lower())     # Output: rohit
```

### Real-life Examples

* Name
* Address
* Message
* Email

All of these are strings.

---

## 4️⃣ BOOLEAN (bool) – True or False

```python
# Boolean values can only be True or False.
# Remember: T and F must be capital letters.

is_student = True
is_failed = False

print(is_student)          # Output: True
print(type(is_student))    # Output: <class 'bool'>

# Used for checking conditions

age = 20

print(age > 18)    # Output: True
print(age > 25)    # Output: False
```

### Real-life Example

A light switch has only two states:

* ON
* OFF

Similarly, Boolean values have only:

* True
* False

---

# The `type()` Function – Identify the Data Type

```python
name = "Rohit"
age = 20
height = 5.9
is_student = True

print(type(name))        # <class 'str'>
print(type(age))         # <class 'int'>
print(type(height))      # <class 'float'>
print(type(is_student))  # <class 'bool'>
```

---

# Type Conversion (Converting One Data Type into Another)

```python
# Convert integer to string

age = 20

age_string = str(age)

print(age_string)       # Output: "20"
print(type(age_string)) # <class 'str'>
```

```python
# Convert string to integer

number_text = "50"

number = int(number_text)

print(number + 10)      # Output: 60
```

```python
# Convert integer to float

marks = 85

marks_float = float(marks)

print(marks_float)      # Output: 85.0
```

```python
# Convert float to integer
# The decimal part is removed.

price = 99.99

price_int = int(price)

print(price_int)        # Output: 99
```

> ⚠️ **Common Mistake:** `"50" + 10` will cause an error. Convert the string first using `int("50")`, then perform the addition.

---

# Real-Life Program – Student Report Card

```python
# Student Report Card

student_name = "Rohit Kumar"      # str
roll_number = 101                 # int
maths_marks = 92.5                # float
science_marks = 88.0              # float
is_passed = True                  # bool

total = maths_marks + science_marks
percentage = (total / 200) * 100

print("=== Report Card ===")
print("Name:", student_name)
print("Roll No:", roll_number)
print("Maths:", maths_marks)
print("Science:", science_marks)
print("Total:", total)
print("Percentage:", percentage)
print("Passed:", is_passed)
```

### Output

```text
=== Report Card ===
Name: Rohit Kumar
Roll No: 101
Maths: 92.5
Science: 88.0
Total: 180.5
Percentage: 90.25
Passed: True
```

---

# Common Mistakes ⚠️

```python
# ❌ Mistake 1: Writing numbers inside quotes

age = "20"      # This is a string, not an integer.

# You cannot perform mathematical operations directly.
```

```python
# ❌ Mistake 2: Using lowercase for Boolean values

is_student = true

# Error!
# It should be True (capital T).
```

```python
# ❌ Mistake 3: Adding a string and a number

print("My age is " + 20)       # Error

print("My age is " + str(20))  # Correct
```

---

# 🎓 Important Exam/Interview Questions

1. What are the four main data types in Python?
2. What is the difference between `int` and `float`?
3. What does the `type()` function do?
4. What is type conversion? Give one example.
5. How many Boolean values are there, and what are they?

---

# 📝 Practice Questions

### Q1.

Identify the correct data type for each value:

* `"Bihar"` → ?
* `99` → ?
* `3.14` → ?
* `False` → ?
* `"True"` → ? *(Think carefully!)*

### Q2.

Write a Python program that:

* Creates a variable `price` with the value `150.75`
* Creates a variable `quantity` with the value `3`
* Creates a variable `total` by multiplying `price * quantity`
* Prints all the variables



### Q3.

Use the `type()` function to print the data type of each variable.


---

### Q4.

Perform the following type conversions:

* Convert `"25"` into an integer, add `5`, and print the result.
* Convert `99` into a string and print it with `" marks obtained"`.


### Q5. Exam Question
Will `int("99.5")` work? What will happen? Think carefully before answering!

ans =>

# **Lesson 3 – Practice Questions (Answers)**

---

# ✅ Q1. Identify the Correct Data Type

| Value     | Data Type                                        |
| --------- | ------------------------------------------------ |
| `"Bihar"` | **String (str)**                                 |
| `99`      | **Integer (int)**                                |
| `3.14`    | **Float (float)**                                |
| `False`   | **Boolean (bool)**                               |
| `"True"`  | **String (str)** *(because it is inside quotes)* |

---

# ✅ Q2. Program: Price × Quantity

```python
price = 150.75
quantity = 3

total = price * quantity

print("Price:", price)
print("Quantity:", quantity)
print("Total:", total)
```

### Output

```text
Price: 150.75
Quantity: 3
Total: 452.25
```

---

# ✅ Q3. Print the Data Type

```python
a = 100
b = 3.14
c = "Python"
d = True

print(type(a))
print(type(b))
print(type(c))
print(type(d))
```

### Output

```text
<class 'int'>
<class 'float'>
<class 'str'>
<class 'bool'>
```

---

# ✅ Q4. Type Conversion

### Part 1: Convert `"25"` into an Integer and Add 5

```python
number = int("25")

result = number + 5

print(result)
```

### Output

```text
30
```

---

### Part 2: Convert `99` into a String

```python
marks = str(99)

print(marks + " marks obtained")
```

### Output

```text
99 marks obtained
```

---

# ✅ Q5. Exam Question

### Will `int("99.5")` work?

**Answer:** ❌ **No, it will not work.**

It will raise a **ValueError** because `"99.5"` is a decimal number stored as a string, and `int()` can only convert strings that contain whole numbers.

### Example

```python
number = int("99.5")
```

### Output

```text
ValueError: invalid literal for int() with base 10: '99.5'
```

### Correct Way

```python
number = float("99.5")
print(number)
```

**Output**

```text
99.5
```

Or, if you want an integer:

```python
number = int(float("99.5"))
print(number)
```

**Output**

```text
99

'''