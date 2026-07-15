'''

---

# Lesson 11: Functions (How Functions Work) ⚙️

## What is a Function?

### Real-Life Example

Imagine you make **tea every morning**:

1. Boil water
2. Add tea leaves
3. Add milk
4. Add sugar
5. Pour into a cup

You repeat these **5 steps every day**.

Instead of writing these steps again and again, imagine there is a **"Make Tea"** button. Whenever you press it, the tea is prepared automatically.

That is exactly what a **Function** is.

> **A Function is a reusable block of code that performs a specific task.**

```python
# Without Function

print("Boil water")
print("Tea is ready")

print("Boil water")
print("Tea is ready")

# With Function

def make_tea():
    print("Boil water")
    print("Tea is ready")

make_tea()
make_tea()
make_tea()
```

---

# Creating a Function

### Syntax

```python
def function_name():
    # code
```

Example

```python
def hello():
    print("Hello!")
    print("How are you?")

hello()
hello()
```

---

## Meaning of Each Part

| Code        | Meaning                           |
| ----------- | --------------------------------- |
| `def`       | Defines a function                |
| `hello`     | Function name                     |
| `()`        | Parentheses (used for parameters) |
| `:`         | Starts the function body          |
| Indentation | Code inside the function          |
| `hello()`   | Function call                     |

---

# 1. Parameters (Giving Data to a Function)

```python
def greet(name):
    print(f"Hello, {name}!")
    print(f"Welcome {name}!")

greet("Rohit")
greet("Amit")
greet("Priya")
```

---

## Multiple Parameters

```python
def student_info(name, age, course):
    print(f"Name   : {name}")
    print(f"Age    : {age}")
    print(f"Course : {course}")
    print("-" * 20)

student_info("Rohit", 20, "BCA")
student_info("Amit", 21, "BTech")
student_info("Priya", 19, "BSc")
```

---

# 2. Return Statement

```python
def add(a, b):
    result = a + b
    return result

answer = add(10, 20)
print(answer)

print(add(5, 3))
```

---

## Return vs Print

### Print

```python
def add_print(a, b):
    print(a + b)

result = add_print(5, 3)

print(result)
```

Output

```
8
None
```

### Return

```python
def add_return(a, b):
    return a + b

result = add_return(5, 3)

print(result)
```

Output

```
8
```

> Use **return** when you want to use the result later.

---

# 3. Default Parameters

```python
def greet(name, message="Hello"):
    print(f"{message}, {name}!")

greet("Rohit")
greet("Amit", "Good Morning")
```

---

# 4. Keyword Arguments

```python
def student(name, roll, marks):
    print(f"{roll}. {name}: {marks}%")

student("Rohit", 101, 85)

student(name="Rohit", marks=85, roll=101)
student(roll=101, marks=85, name="Rohit")
```

---

# 5. *args (Variable Number of Arguments)

```python
def total(*numbers):
    total_sum = 0

    for num in numbers:
        total_sum += num

    return total_sum

print(total(1,2))
print(total(1,2,3))
print(total(1,2,3,4,5))
```

---

# Example

```python
def all_names(*names):
    print(f"There are {len(names)} students.")

    for name in names:
        print(name)

all_names("Rohit","Amit","Priya")
```

---

# 6. Local vs Global Variables

```python
school = "DPS School"

def student():
    name = "Rohit"
    print(name)
    print(school)

student()

print(school)
```

---

## Global Keyword

```python
count = 0

def increase():
    global count
    count += 1

increase()
increase()
increase()

print(count)
```

Output

```
3
```

---

# Real-Life Program 1: Calculator

```python
def add(a,b):
    return a+b

def subtract(a,b):
    return a-b

def multiply(a,b):
    return a*b

def divide(a,b):
    if b==0:
        return "Cannot divide by zero"

    return a/b

a=float(input("First Number: "))
b=float(input("Second Number: "))

print(add(a,b))
print(subtract(a,b))
print(multiply(a,b))
print(divide(a,b))
```

---

# Real-Life Program 2: Grade Calculator

```python
def get_grade(marks):

    if marks>=90:
        return "A+"

    elif marks>=80:
        return "A"

    elif marks>=70:
        return "B"

    elif marks>=60:
        return "C"

    elif marks>=33:
        return "D"

    else:
        return "F"

def result(name,marks):

    grade=get_grade(marks)

    status="PASS" if marks>=33 else "FAIL"

    print(name)
    print(marks)
    print(grade)
    print(status)

result("Rohit",85)
```

---

# Real-Life Program 3: Simple Interest

```python
def simple_interest(principal,rate,time):

    si=(principal*rate*time)/100

    total=principal+si

    return si,total

p=float(input("Principal: "))
r=float(input("Rate: "))
t=float(input("Time: "))

interest,total=simple_interest(p,r,t)

print(interest)
print(total)
```

---

# Common Mistakes

### Calling Function Before Defining

❌ Wrong

```python
greet()

def greet():
    print("Hello")
```

---

### Forgetting Return

❌ Wrong

```python
def square(n):
    result=n*n

print(square(5))
```

Output

```
None
```

---

### Code After Return

```python
def add(a,b):

    return a+b

    print("Done")
```

`print("Done")` will never execute.

---

# Interview Questions

1. What is a Function?
2. Why do we use Functions?
3. Difference between Parameters and Arguments.
4. Difference between Return and Print.
5. What are Default Parameters?
6. What are Local and Global Variables?
7. What is `*args`?
8. Can a function return multiple values?

---

# Practice Questions with Answers

## Answer 1

```python
def rectangle_info(length, width):
    area = length * width
    perimeter = 2 * (length + width)
    return area, perimeter

a, p = rectangle_info(10, 5)

print("Area:", a)
print("Perimeter:", p)
```

Output

```
Area: 50
Perimeter: 30
```

---

## Answer 2

```python
def is_palindrome(word):
    return word == word[::-1]

print(is_palindrome("madam"))
print(is_palindrome("racecar"))
print(is_palindrome("python"))
```

Output

```
True
True
False
```

---

## Answer 3

```python
def fahrenheit_to_celsius(f):
    return (f - 32) * 5 / 9

f = float(input("Enter Fahrenheit: "))

c = fahrenheit_to_celsius(f)

print("Celsius:", c)
```

Example

Input

```
212
```

Output

```
100.0
```

---

## Answer 4

```python
def find_max(*numbers):

    maximum = numbers[0]

    for num in numbers:

        if num > maximum:
            maximum = num

    return maximum

print(find_max(10, 20, 50, 15, 80, 45))
```

Output

```
80
```

---

## Answer 5

```python
def mystery(a, b=10):
    return a * b

print(mystery(5))
print(mystery(5, 3))
print(mystery(b=2, a=4))
```

### Output

```
50
15
8
```

### Explanation

#### Line 1

```python
print(mystery(5))
```

* `a = 5`
* `b = 10` (default value)

```
5 × 10 = 50
```

Output

```
50
```

---

#### Line 2

```python
print(mystery(5,3))
```

* `a = 5`
* `b = 3`

```
5 × 3 = 15
```

Output

```
15
```

---

#### Line 3

```python
print(mystery(b=2,a=4))
```

Using **keyword arguments**, so order does not matter.

* `a = 4`
* `b = 2`

```
4 × 2 = 8
```

Output

```
8
```

---

'''