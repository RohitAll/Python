'''
# 📘 Lesson 7: Conditional Statements (if / elif / else) 🔀

## What is a Conditional Statement?

A **conditional statement** allows a program to make decisions based on whether a condition is **True** or **False**.

### 🌍 Real-Life Example

Imagine you wake up in the morning and look outside:

* **If** it is raining → Take an umbrella.
* **Else if** it is sunny → Wear sunglasses.
* **Else** → Go outside normally.

Python follows the same logic using **if**, **elif**, and **else**.

```text
If the condition is True → Do this
Else if another condition is True → Do this
Else → Do something else
```

---

# 1️⃣ Basic if Statement

```python
# Syntax:
# if condition:
#     statement

age = 20

if age >= 18:
    print("You are eligible to vote!")

# Output:
# You are eligible to vote!
```

## Explanation

| Code        | Meaning                                                  |
| ----------- | -------------------------------------------------------- |
| `if`        | Checks a condition                                       |
| `age >= 18` | Condition that returns True or False                     |
| `:`         | Marks the beginning of the block                         |
| Indentation | Code inside the block runs only if the condition is True |

> ⚠️ **Indentation is very important in Python!**

### ❌ Incorrect

```python
if age >= 18:
print("Eligible")
```

### ✅ Correct

```python
if age >= 18:
    print("Eligible")
```

---

# 2️⃣ if / else Statement

```python
age = 15

if age >= 18:
    print("You can vote!")
else:
    print("You cannot vote yet!")

# Output:
# You cannot vote yet!
```

### Example

```python
marks = 45

if marks >= 33:
    print("Congratulations! You Passed!")
else:
    print("Sorry! You Failed!")

# Output:
# Congratulations! You Passed!
```

---

# 3️⃣ if / elif / else Statement

Use this when there are multiple conditions.

```python
marks = 85

if marks >= 90:
    print("Grade: A+")
elif marks >= 80:
    print("Grade: A")
elif marks >= 70:
    print("Grade: B")
elif marks >= 60:
    print("Grade: C")
elif marks >= 33:
    print("Grade: D")
else:
    print("Grade: F")

# Output:
# Grade: A
```

## How it Works

```
marks = 85

85 >= 90 ?  No
85 >= 80 ?  Yes ✅

Print Grade A
Stop checking the remaining conditions.
```

> 💡 Once Python finds the first True condition, it skips all remaining conditions.

---

# 4️⃣ Nested if Statement

An **if statement inside another if statement** is called a Nested if.

```python
age = 20
voter_card = True

if age >= 18:
    print("Age is valid.")

    if voter_card == True:
        print("You can vote.")
    else:
        print("Please apply for a voter card.")
else:
    print("You are under 18.")

# Output:
# Age is valid.
# You can vote.
```

---

# 5️⃣ Using Logical Operators with if

```python
age = 25
income = 50000

# AND
if age >= 18 and income >= 25000:
    print("Eligible for a loan.")

# OR
hobby = "cricket"

if hobby == "cricket" or hobby == "football":
    print("You are a sports lover.")

# NOT
is_holiday = False

if not is_holiday:
    print("Go to school or office today.")
```

---

# 🌟 Real-Life Programs

## Program 1: ATM PIN Verification

```python
print("=== ATM Machine ===")

actual_pin = 1234
entered_pin = int(input("Enter your PIN: "))

if entered_pin == actual_pin:
    print("Correct PIN!")
    print("Balance: Rs. 50,000")
else:
    print("Incorrect PIN!")
```

---

## Program 2: Grade Calculator

```python
print("=== Grade Calculator ===")

name = input("Enter Student Name: ")
marks = float(input("Enter Marks (Out of 100): "))

if marks >= 90:
    grade = "A+"
    remark = "Outstanding!"
elif marks >= 80:
    grade = "A"
    remark = "Excellent!"
elif marks >= 70:
    grade = "B"
    remark = "Very Good!"
elif marks >= 60:
    grade = "C"
    remark = "Good!"
elif marks >= 33:
    grade = "D"
    remark = "Pass"
else:
    grade = "F"
    remark = "Fail! Work Hard."

print("\n===== Result =====")
print(f"Name   : {name}")
print(f"Marks  : {marks}")
print(f"Grade  : {grade}")
print(f"Remark : {remark}")
```

### Sample Output

```
Enter Student Name: Rohit
Enter Marks: 85

===== Result =====
Name   : Rohit
Marks  : 85
Grade  : A
Remark : Excellent!
```

---

## Program 3: Positive, Negative or Zero

```python
num = float(input("Enter a number: "))

if num > 0:
    print("Positive Number")
elif num < 0:
    print("Negative Number")
else:
    print("Zero")
```

---

## Program 4: Season Checker

```python
print("=== Season Checker ===")

month = int(input("Enter Month Number (1-12): "))

if month == 12 or month == 1 or month == 2:
    print("Winter")
elif month >= 3 and month <= 5:
    print("Spring")
elif month >= 6 and month <= 8:
    print("Summer")
elif month >= 9 and month <= 11:
    print("Monsoon")
else:
    print("Invalid Month")
```

---

# ⚠️ Common Mistakes

## Mistake 1

```python
if marks = 85:
```

❌ Wrong

```python
if marks == 85:
```

✅ Correct

---

## Mistake 2

```python
if marks >= 33:
print("Pass")
```

❌ Wrong

```python
if marks >= 33:
    print("Pass")
```

✅ Correct

---

## Mistake 3

```python
if marks >= 33
```

❌ Missing Colon

```python
if marks >= 33:
```

✅ Correct

---

## Mistake 4

```python
name = "rohit"

if name == "Rohit":
```

False because Python is case-sensitive.

Better:

```python
if name.lower() == "rohit":
```

---

# 🎓 Interview / Exam Questions

1. What is a conditional statement?
2. Why is indentation important in Python?
3. What is the difference between **if** and **elif**?
4. What is a Nested if statement?
5. How many **elif** statements can be used in one program?

---

# 📝 Practice Questions with Answers

---

## ✅ Q1. Check Positive, Negative or Zero

### Solution

```python
num = float(input("Enter a number: "))

if num > 0:
    print("Positive Number")
elif num < 0:
    print("Negative Number")
else:
    print("Zero")
```

---

## ✅ Q2. Age Category

### Solution

```python
age = int(input("Enter your age: "))

if age <= 12:
    print("You are a Child.")
elif age <= 17:
    print("You are a Teenager.")
elif age <= 60:
    print("You are an Adult.")
else:
    print("You are a Senior Citizen.")
```

---

## ✅ Q3. Login System

### Solution

```python
username = input("Enter Username: ")
password = input("Enter Password: ")

if username == "admin" and password == "python123":
    print("Login Successful! Welcome!")

elif username == "admin":
    print("Incorrect Password!")

elif password == "python123":
    print("Incorrect Username!")

else:
    print("Both Username and Password are Incorrect!")
```

---

## ✅ Q4. Three Subject Result

### Solution

```python
m1 = int(input("Subject 1 Marks: "))
m2 = int(input("Subject 2 Marks: "))
m3 = int(input("Subject 3 Marks: "))

fail_count = 0

if m1 < 33:
    fail_count += 1

if m2 < 33:
    fail_count += 1

if m3 < 33:
    fail_count += 1

if fail_count == 0:
    print("PASS")
elif fail_count == 1:
    print("COMPARTMENT")
else:
    print("FAIL")
```

---

## ✅ Q5. Predict the Output

### Code

```python
x = 10

if x > 5:
    print("A")
    if x > 8:
        print("B")
else:
    print("C")
```

### Answer

### Output

```
A
B
```

### Explanation

Step-by-step:

1. `x = 10`
2. `10 > 5` → **True**, so Python prints **A**.
3. Inside the first `if`, Python checks `10 > 8`.
4. This is also **True**, so Python prints **B**.
5. The `else` block is skipped because the first `if` condition was already **True**.

---

# 📌 Key Points to Remember

* `if` checks a condition.
* `else` runs when the `if` condition is False.
* `elif` checks another condition if the previous one is False.
* Python uses **indentation** to define code blocks.
* Only the **first True condition** in an `if-elif-else` chain is executed.
* Nested `if` means placing one `if` statement inside another.
* Logical operators (`and`, `or`, `not`) make conditions more powerful.

---

## 🎯 Mini Challenge (Try Yourself)

Write Python programs to:

1. Check whether a number is **Even or Odd**.
2. Find the **Largest of Three Numbers**.
3. Check whether a year is a **Leap Year**.
4. Create a **Simple Calculator** using `if-elif-else`.
5. Check whether a person is eligible for **Driving License**, **Voting**, or **Senior Citizen Benefits** based on age.

These exercises will strengthen your understanding of conditional statements.

'''