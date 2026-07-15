'''
---

# Lesson 8: Loops 🔄

## What is a Loop?

### Real-life Example

Imagine your teacher says:

> **"Write 'I will not talk in class' 100 times."**

Without a loop:

```python
print("I will not talk in class")
print("I will not talk in class")
print("I will not talk in class")
# ...You would have to write it 100 times! 😫
```

Using a loop:

```python
for i in range(100):
    print("I will not talk in class")
```

Only **2 lines of code**! 😊

---

# Types of Loops in Python

Python has **2 types of loops**:

1. 🔵 **for loop** – Use when you know how many times to repeat.
2. 🟢 **while loop** – Use when you want to repeat until a condition becomes False.

---

# 1. for Loop

```python
# Syntax

for variable in sequence:
    # Code
```

Example:

```python
for i in range(5):
    print(i)
```

Output

```
0
1
2
3
4
```

---

## Understanding range()

```python
range(5)         # 0,1,2,3,4

range(1,6)       # 1,2,3,4,5

range(0,10,2)    # 0,2,4,6,8

range(10,0,-1)   # 10,9,8...1
```

---

## Real-Life Examples

### Print numbers from 1 to 10

```python
for i in range(1,11):
    print(i)
```

---

### Multiplication Table of 5

```python
for i in range(1,11):
    print(f"5 x {i} = {5*i}")
```

---

### Countdown

```python
for i in range(10,0,-1):
    print(i)

print("Happy New Year! 🎉")
```

---

# for Loop with String

```python
name = "Rohit"

for character in name:
    print(character)
```

Output

```
R
o
h
i
t
```

---

# for Loop with List

```python
fruits = ["Apple","Banana","Mango","Orange"]

for fruit in fruits:
    print(f"Fruit: {fruit}")
```

Output

```
Fruit: Apple
Fruit: Banana
Fruit: Mango
Fruit: Orange
```

---

# 2. while Loop

```python
count = 1

while count <= 5:
    print(count)
    count += 1
```

Output

```
1
2
3
4
5
```

---

## How it Works

```
count = 1

1 <= 5 ? Yes → Print 1

2 <= 5 ? Yes → Print 2

3 <= 5 ? Yes → Print 3

4 <= 5 ? Yes → Print 4

5 <= 5 ? Yes → Print 5

6 <= 5 ? No → Stop
```

---

# Infinite Loop ⚠️

Wrong

```python
count = 1

while count <= 5:
    print(count)
```

The value of `count` never changes, so the loop **never stops**.

Correct

```python
count = 1

while count <= 5:
    print(count)
    count += 1
```

---

# Loop Control Statements

## break

Stops the loop immediately.

```python
for i in range(1,11):

    if i == 5:
        break

    print(i)
```

Output

```
1
2
3
4
```

---

### Example

```python
for attempt in range(1,4):

    pin = int(input("Enter PIN: "))

    if pin == 1234:
        print("Correct PIN!")
        break

    else:
        print("Wrong PIN!")
```

---

## continue

Skips only the current iteration.

```python
for i in range(1,11):

    if i % 2 == 0:
        continue

    print(i)
```

Output

```
1
3
5
7
9
```

---

# Nested Loops

A loop inside another loop.

```python
for table in range(1,6):

    print(f"\nTable of {table}")

    for i in range(1,11):

        print(f"{table} x {i} = {table*i}")
```

---

# Real-Life Programs

## Program 1 – Sum Calculator

```python
n = int(input("Enter a number: "))

total = 0

for i in range(1,n+1):
    total += i

print(total)
```

---

## Program 2 – ATM

```python
correct_pin = 1234

chances = 3

while chances > 0:

    pin = int(input("Enter PIN: "))

    if pin == correct_pin:
        print("Welcome!")
        break

    else:
        chances -= 1

        if chances > 0:
            print("Wrong PIN")

        else:
            print("Account Locked")
```

---

## Program 3 – Star Pattern

```python
rows = int(input("Enter rows: "))

for i in range(1,rows+1):

    print("* " * i)
```

Output (5 rows)

```
*
* *
* * *
* * * *
* * * * *
```

---

## Program 4 – Factorial

```python
n = int(input("Enter a number: "))

factorial = 1

for i in range(1,n+1):

    factorial *= i

print(factorial)
```

---

# for vs while

| Situation                            | Use   |
| ------------------------------------ | ----- |
| Number of repetitions is known       | for   |
| Working with lists                   | for   |
| Working with strings                 | for   |
| Repeat until condition becomes False | while |
| User input dependent                 | while |
| Unknown number of repetitions        | while |

---

# Common Mistakes

### Mistake 1

```python
for i in range(1,10):
    print(i)
```

This prints **1 to 9**, not 10.

Correct

```python
for i in range(1,11):
    print(i)
```

---

### Mistake 2

```python
while count <= 5:
    print(count)
```

Forgot to update `count`.

Infinite loop!

---

### Mistake 3

Wrong indentation

```python
for i in range(5):
print(i)
```

Correct

```python
for i in range(5):
    print(i)
```

---

# Interview Questions

1. What is the difference between **for** and **while** loops?
2. What numbers are generated by `range(1,10)`?
3. What is the difference between **break** and **continue**?
4. What is an infinite loop? How can you avoid it?
5. What is a nested loop? Give an example.

---

# Practice Questions

### Q1

Using a **for loop**

* Print numbers from 1 to 10.
* Print even numbers from 1 to 10.
* Print odd numbers from 1 to 10.

---

### Q2

Using a **while loop**

Keep taking numbers from the user until they enter **0**.

After entering 0, print the **sum** of all numbers entered.

---

### Q3

Take a number from the user and print its multiplication table.

---

### Q4

Using nested loops, print

```
1
1 2
1 2 3
1 2 3 4
1 2 3 4 5
```

---

### Q5

Create a Number Guessing Game.

* Secret number = 42
* Keep asking until the correct guess.
* Show hints:

  * Too High
  * Too Low
* Print:

  * "Congratulations! You guessed it in X attempts."

---

### Exam Question

```python
for i in range(3):

    for j in range(3):

        print(i, j)
```

Without running the code,

* How many lines will be printed?
* What will the output be?

---

# ✅ Answers to Practice Questions

## Answer 1

```python
# Numbers 1 to 10

for i in range(1,11):
    print(i)

print()

# Even Numbers

for i in range(2,11,2):
    print(i)

print()

# Odd Numbers

for i in range(1,11,2):
    print(i)
```

---

## Answer 2

```python
total = 0

while True:

    number = int(input("Enter a number (0 to stop): "))

    if number == 0:
        break

    total += number

print("Sum =", total)
```

---

## Answer 3

```python
number = int(input("Enter a number: "))

for i in range(1,11):

    print(f"{number} x {i} = {number*i}")
```

---

## Answer 4

```python
for i in range(1,6):

    for j in range(1,i+1):

        print(j, end=" ")

    print()
```

Output

```
1
1 2
1 2 3
1 2 3 4
1 2 3 4 5
```

---

## Answer 5

```python
secret = 42

attempts = 0

while True:

    guess = int(input("Enter your guess: "))

    attempts += 1

    if guess == secret:
        print(f"Congratulations! You guessed it in {attempts} attempts.")
        break

    elif guess > secret:
        print("Too High!")

    else:
        print("Too Low!")
```

---

# Answer to Exam Question

Code

```python
for i in range(3):
    for j in range(3):
        print(i, j)
```

### Total Output Lines

```
3 × 3 = 9 lines
```

### Output

```
0 0
0 1
0 2
1 0
1 1
1 2
2 0
2 1
2 2
```

---

🎯 **Key Takeaway:** Loops are one of the most important concepts in Python. Once you master **for loops**, **while loops**, **break**, **continue**, and **nested loops**, you'll be able to solve most beginner-to-intermediate programming problems with confidence.

'''