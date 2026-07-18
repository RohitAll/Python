'''
# 📘 Lesson 9: Lists 📋

## What is a List?

### Real-Life Example

Imagine you are going grocery shopping and make a **shopping list**:

* Milk
* Bread
* Eggs
* Rice
* Lentils

A **List** in Python works the same way. It allows you to store **multiple values inside a single variable**.

```python
# Without a list (Not recommended)
item1 = "Milk"
item2 = "Bread"
item3 = "Eggs"
item4 = "Rice"
item5 = "Lentils"

# Using a list (Recommended)
shopping = ["Milk", "Bread", "Eggs", "Rice", "Lentils"]
```

---

# Creating a List

```python
# Syntax
# list_name = [item1, item2, item3, ...]

# List of strings
fruits = ["Apple", "Banana", "Mango"]

# List of integers
marks = [85, 92, 78, 95, 88]

# List of floats
prices = [10.5, 20.99, 5.75]

# Mixed data types
student = ["Rohit", 20, "BCA", 85.5, True]

# Empty list
empty = []

print(fruits)
print(marks)
```

---

# 1️⃣ List Indexing (Accessing Elements)

```python
fruits = ["Apple", "Banana", "Mango", "Orange", "Grapes"]

# Index:      0         1         2         3          4

print(fruits[0])     # Apple
print(fruits[2])     # Mango
print(fruits[-1])    # Grapes
print(fruits[-2])    # Orange
```

---

# 2️⃣ List Slicing

```python
marks = [85, 92, 78, 95, 88, 76, 90]

print(marks[0:3])
print(marks[2:5])
print(marks[:3])
print(marks[3:])
print(marks[::2])
print(marks[::-1])
```

---

# 3️⃣ List Methods 🛠️

## Adding Items

```python
fruits = ["Apple", "Banana"]

# Add item at the end
fruits.append("Mango")

# Insert at a specific position
fruits.insert(1, "Orange")

# Add another list
more_fruits = ["Grapes", "Pineapple"]
fruits.extend(more_fruits)

print(fruits)
```

---

## Removing Items

```python
fruits = ["Apple", "Banana", "Mango", "Orange"]

fruits.remove("Banana")

fruits.pop()

fruits.pop(0)

fruits.clear()

print(fruits)
```

---

## Other Useful Methods

```python
numbers = [5, 2, 8, 1, 9, 3, 7]

numbers.sort()

numbers.sort(reverse=True)

numbers.reverse()

print(len(numbers))

nums = [1, 2, 2, 3, 2, 4]
print(nums.count(2))

fruits = ["Apple", "Banana", "Mango"]
print(fruits.index("Banana"))

print("Apple" in fruits)
print("Grapes" in fruits)
```

---

# 4️⃣ Using Loops with Lists

```python
students = ["Rohit", "Amit", "Priya", "Neha"]

# Method 1
for student in students:
    print(f"Hello, {student}!")

# Method 2
for i in range(len(students)):
    print(f"{i+1}. {students[i]}")

# Method 3 (Best)
for index, student in enumerate(students, 1):
    print(f"{index}. {student}")
```

---

# 5️⃣ Modifying List Elements

```python
fruits = ["Apple", "Banana", "Mango"]

fruits[1] = "Orange"

print(fruits)

fruits[0:2] = ["Grapes", "Pineapple"]

print(fruits)
```

---

# 🌟 Real-Life Programs

## Program 1 – Student Marks Analyzer

```python
marks = [85, 92, 78, 95, 88, 76, 90]

print("=== Marks Analyzer ===")
print(f"Marks         : {marks}")
print(f"Subjects      : {len(marks)}")
print(f"Total Marks   : {sum(marks)}")
print(f"Average Marks : {sum(marks)/len(marks):.2f}")
print(f"Highest Marks : {max(marks)}")
print(f"Lowest Marks  : {min(marks)}")

marks.sort(reverse=True)

print(f"Sorted Marks  : {marks}")
```

---

## Program 2 – Shopping Cart

```python
cart = []

print("=== Shopping Cart ===")

while True:

    print("\n1. Add Item")
    print("2. Remove Item")
    print("3. View Cart")
    print("4. Checkout")

    choice = input("Enter your choice: ")

    if choice == "1":

        item = input("Enter item name: ")
        cart.append(item)
        print(f"{item} added successfully!")

    elif choice == "2":

        if len(cart) == 0:
            print("Cart is empty!")

        else:

            item = input("Enter item to remove: ")

            if item in cart:
                cart.remove(item)
                print(f"{item} removed successfully!")
            else:
                print("Item not found!")

    elif choice == "3":

        if len(cart) == 0:
            print("Cart is empty!")

        else:

            print("\nShopping Cart")

            for i, item in enumerate(cart, 1):
                print(f"{i}. {item}")

    elif choice == "4":

        print(f"{len(cart)} items checked out successfully!")
        break
```

---

## Program 3 – Taking Input from User

```python
student_names = []

n = int(input("How many students? "))

for i in range(n):

    name = input(f"Enter name of student {i+1}: ")
    student_names.append(name)

print("\nClass List")

for index, name in enumerate(student_names, 1):
    print(f"{index}. {name}")

print(f"\nTotal Students: {len(student_names)}")
```

---

# Built-in Functions

```python
numbers = [5, 2, 8, 1, 9, 3]

print(len(numbers))
print(sum(numbers))
print(max(numbers))
print(min(numbers))
print(sorted(numbers))
```

---

# Common Mistakes ⚠️

```python
# Index Error
fruits = ["Apple", "Banana", "Mango"]

print(fruits[3])   # Error

# append vs extend

list1 = [1,2,3]

list1.append([4,5])

list1.extend([4,5])

# Copy Problem

list1 = [1,2,3]

list2 = list1

list2.append(4)

print(list1)

# Correct Copy

list2 = list1.copy()

list2.append(4)

print(list1)
```

---

# 🎓 Interview / Exam Questions

1. What is a List in Python? How do you create one?
2. What is the difference between `append()` and `extend()`?
3. What is the difference between `remove()` and `pop()`?
4. What does the `in` operator do in a list?
5. What is the purpose of the `enumerate()` function?
6. How do you correctly copy a list?

---

# 📝 Practice Questions

## Q1

Create a list containing five subject names.

* Print the entire list.
* Print the first and last subject.
* Add one new subject at the end.
* Replace the second subject with another subject.

---

## Q2

Take five numbers from the user and store them in a list.

* Find the sum.
* Find the average.
* Find the maximum and minimum values.
* Print the sorted list in ascending order.

---

## Q3

Create the following list:

```python
numbers = [4, 7, 2, 9, 1, 5, 8, 3, 6]
```

Using loops:

* Print only the even numbers.
* Print only the numbers greater than 5.

---

## Q4

Create a To-Do List program.

* User can add tasks.
* User can remove completed tasks.
* User can view all tasks.
* Program exits when the user enters `"quit"`.

---

## Q5

Without running the program, predict the output.

```python
nums = [10, 20, 30, 40, 50]

print(nums[1:4])
print(nums[-1])
print(nums[::-1])
```

---

# ✅ Answers

## Answer 1

```python
subjects = ["English", "Math", "Science", "Computer", "History"]

print(subjects)

print(subjects[0])

print(subjects[-1])

subjects.append("Geography")

subjects[1] = "Physics"

print(subjects)
```

**Output**

```
['English', 'Math', 'Science', 'Computer', 'History']
English
History
['English', 'Physics', 'Science', 'Computer', 'History', 'Geography']
```

---

## Answer 2

```python
numbers = []

for i in range(5):
    num = int(input("Enter a number: "))
    numbers.append(num)

print("Numbers:", numbers)
print("Sum:", sum(numbers))
print("Average:", sum(numbers)/len(numbers))
print("Maximum:", max(numbers))
print("Minimum:", min(numbers))

numbers.sort()

print("Sorted:", numbers)
```

---

## Answer 3

```python
numbers = [4, 7, 2, 9, 1, 5, 8, 3, 6]

print("Even Numbers:")

for num in numbers:
    if num % 2 == 0:
        print(num)

print("Numbers Greater Than 5:")

for num in numbers:
    if num > 5:
        print(num)
```

**Output**

```
Even Numbers:
4
2
8
6

Numbers Greater Than 5:
7
9
8
6
```

---

## Answer 4

```python
todo = []

while True:

    task = input("Enter task (type quit to stop): ")

    if task.lower() == "quit":
        break

    todo.append(task)

print("\nYour Tasks")

for i, task in enumerate(todo, 1):
    print(f"{i}. {task}")

remove = input("\nEnter completed task: ")

if remove in todo:
    todo.remove(remove)

print("\nRemaining Tasks")

for i, task in enumerate(todo, 1):
    print(f"{i}. {task}")
```

---

## Answer 5

### Code

```python
nums = [10, 20, 30, 40, 50]

print(nums[1:4])
print(nums[-1])
print(nums[::-1])
```

### Output

```text
[20, 30, 40]
50
[50, 40, 30, 20, 10]
```

---

🎯 **Congratulations!** You have completed **Lesson 9: Lists**. Lists are one of the most important data structures in Python and are used extensively in Data Analysis, Machine Learning, Web Development, Automation, and many real-world applications.

'''