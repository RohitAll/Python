'''
# Lesson 6: User Input (Getting Data from the User) ⌨️

## What is User Input?

Until now, we have **entered data ourselves** in our programs:

```python
name = "Rohit"      # We entered it ourselves
age = 20            # We entered it ourselves
```

But in real-world programs, **the user enters the data**.

### Real-Life Examples

* An ATM asks: **"Enter your PIN"** → You type it.
* Google asks: **"Search anything"** → You type your query.
* WhatsApp lets you **type a message**.

This process is called **User Input**.

---

# input() Function - Basic Usage

```python
# input() function takes input from the user

name = input("Enter your name: ")
print("Hello,", name)
```

### Output

```
Enter your name: Rohit
Hello, Rohit
```

### Line-by-Line Explanation

| Code                         | Meaning                                                       |
| ---------------------------- | ------------------------------------------------------------- |
| `input("Enter your name: ")` | Displays a message and waits for the user to type something.  |
| `name = input(...)`          | Stores whatever the user types into the variable `name`.      |
| `"Enter your name: "`        | This is called a **prompt**. It tells the user what to enter. |

---

# ⚠️ Important: input() Always Returns a STRING

```python
age = input("Enter your age: ")
print(type(age))
```

### Output

```
<class 'str'>
```

Even if the user types:

```
20
```

Python stores it as:

```
"20"
```

which is a **string**, not an integer.

---

# Solution - Type Conversion

### Integer Input

```python
age = int(input("Enter your age: "))
print(type(age))
```

Output

```
<class 'int'>
```

---

### Float Input

```python
height = float(input("Enter your height: "))
print(type(height))
```

Output

```
<class 'float'>
```

---

# Practical Examples

## Example 1 - Greeting Program

```python
name = input("What is your name? ")
city = input("Which city are you from? ")

print(f"Hello {name}!")
print(f"Oh, you are from {city}.")
print(f"Welcome to our program, {name}!")
```

### Output

```
What is your name? Rohit
Which city are you from? Siwan

Hello Rohit!
Oh, you are from Siwan.
Welcome to our program, Rohit!
```

---

## Example 2 - Simple Calculator

```python
print("=== Simple Calculator ===")

num1 = float(input("Enter the first number: "))
num2 = float(input("Enter the second number: "))

print(f"\nAddition       : {num1 + num2}")
print(f"Subtraction    : {num1 - num2}")
print(f"Multiplication : {num1 * num2}")
print(f"Division       : {num1 / num2}")
```

### Output

```
=== Simple Calculator ===

Enter the first number: 10
Enter the second number: 4

Addition       : 14.0
Subtraction    : 6.0
Multiplication : 40.0
Division       : 2.5
```

---

## Example 3 - Rectangle Area Calculator

```python
print("=== Rectangle Area Calculator ===")

length = float(input("Enter the length of the rectangle: "))
width = float(input("Enter the width of the rectangle: "))

area = length * width
perimeter = 2 * (length + width)

print(f"\nLength      : {length}")
print(f"Width       : {width}")
print(f"Area        : {area} square units")
print(f"Perimeter   : {perimeter} units")
```

---

## Example 4 - Student Marks Calculator

```python
print("=== Marks Calculator ===")

name = input("Enter student's name: ")

maths = float(input("Enter Maths marks (out of 100): "))
science = float(input("Enter Science marks (out of 100): "))
english = float(input("Enter English marks (out of 100): "))

total = maths + science + english
percentage = (total / 300) * 100

print("\n" + "=" * 30)
print(f"Name        : {name}")
print(f"Maths       : {maths}")
print(f"Science     : {science}")
print(f"English     : {english}")
print(f"Total       : {total}/300")
print(f"Percentage  : {percentage:.2f}%")
print("=" * 30)
```

### New Trick

```python
{percentage:.2f}
```

means:

Display only **2 digits after the decimal point**.

Example:

```
85.666666 → 85.67
```

---

# Using \n for Better Formatting

```python
print("Line 1\nLine 2\nLine 3")
```

Output

```
Line 1
Line 2
Line 3
```

Example:

```python
name = input("Enter your name: ")

print(f"\nHello {name}!\nWelcome!\n")
```

---

# Common Mistakes

### ❌ Mistake 1 - Forgetting int()

```python
age = input("Age: ")
print(age + 5)
```

This causes an error because `age` is a string.

### ✅ Correct

```python
age = int(input("Age: "))
print(age + 5)
```

---

### ❌ Mistake 2 - Using int() for Decimal Values

```python
height = int(input("Height: "))
```

If the user enters:

```
5.9
```

Python gives an error.

### ✅ Correct

```python
height = float(input("Height: "))
```

---

### ❌ Mistake 3 - Forgetting Space in Prompt

```python
name = input("Name:")
```

Output

```
Name:Rohit
```

### Better

```python
name = input("Name: ")
```

Output

```
Name: Rohit
```

---

# Best Practices

```python
# Use clear prompts
full_name = input("Enter your full name (Example: Rohit Kumar): ")

# Mention units
weight = float(input("Enter your weight (kg): "))

# Separate output
print("\n=== Result ===")

# Use meaningful variable names
student_name = input("Enter student name: ")
```

---

# 🎓 Important Interview/Exam Questions

1. What does the `input()` function do?
2. What data type does `input()` return?
3. How do you take integer input from a user?
4. What is the purpose of the prompt inside `input()`?
5. What does `{value:.2f}` mean in an f-string?

---

# 📝 Practice Questions with Answers

## Q1.

### Question

Write a program that:

* Takes the user's name and age.
* Prints:

```
Hello [name]! You are [age] years old.
```

### Answer

```python
name = input("Enter your name: ")
age = int(input("Enter your age: "))

print(f"Hello {name}! You are {age} years old.")
```

### Sample Output

```
Enter your name: Rohit
Enter your age: 20

Hello Rohit! You are 20 years old.
```

---

## Q2.

### Question

Write a Simple Interest Calculator.

Formula

```
SI = (P × R × T) / 100
```

### Answer

```python
principal = float(input("Enter Principal: "))
rate = float(input("Enter Rate: "))
time = float(input("Enter Time (years): "))

si = (principal * rate * time) / 100

print(f"\nSimple Interest = {si}")
```

### Sample Output

```
Enter Principal: 10000
Enter Rate: 5
Enter Time: 2

Simple Interest = 1000.0
```

---

## Q3.

### Question

Take the user's full name and:

* Print it in CAPITAL letters.
* Print the total number of characters.
* Print the first and last character.

### Answer

```python
full_name = input("Enter your full name: ")

print("Uppercase :", full_name.upper())
print("Characters:", len(full_name))
print("First Character:", full_name[0])
print("Last Character :", full_name[-1])
```

### Sample Output

```
Enter your full name: Rohit Kumar

Uppercase : ROHIT KUMAR
Characters: 12
First Character: R
Last Character : r
```

---

## Q4.

### Question

Create a Temperature Converter.

Formula

```
F = (C × 9/5) + 32
```

### Answer

```python
celsius = float(input("Enter temperature in Celsius: "))

fahrenheit = (celsius * 9 / 5) + 32

print(f"{celsius}°C = {fahrenheit}°F")
```

### Sample Output

```
Enter temperature in Celsius: 25

25.0°C = 77.0°F
```

---

## Q5.

### Question

```python
x = input("Enter a number: ")
print(x + 10)
```

What is the mistake? Correct it and explain.

### Answer

#### Mistake

`input()` always returns a **string**, so Python cannot add a string and an integer.

```python
"10" + 10
```

This causes a **TypeError**.

---

### Correct Code

```python
x = int(input("Enter a number: "))
print(x + 10)
```

### Sample Output

```
Enter a number: 20

30
```

### Explanation

* `input()` returns a string.
* `int()` converts the string into an integer.
* Now Python can perform mathematical addition.

'''