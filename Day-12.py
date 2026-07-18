'''
# 📘 Lesson 12: Sets (Unique Collection) 🔢

## What is a Set?

### Real-life Example

Imagine you have a list of **student roll numbers**:

```python
roll_numbers = [1, 2, 3, 2, 4, 3, 5, 1]
```

Some roll numbers are repeated.

If you only want **unique roll numbers**, use a **Set**.

```python
roll_numbers = {1, 2, 3, 2, 4, 3, 5, 1}
print(roll_numbers)
```

**Output**

```python
{1, 2, 3, 4, 5}
```

Duplicate values are removed automatically.

---

# Three Important Features of a Set

## 1. No Duplicate Elements

```python
numbers = {1, 2, 2, 3, 3, 3, 4}
print(numbers)
```

Output

```python
{1, 2, 3, 4}
```

---

## 2. Unordered Collection

```python
my_set = {5, 2, 8, 1, 9}
print(my_set)
```

Output can be

```python
{1, 2, 5, 8, 9}
```

or in another order.

The order is **not guaranteed**.

---

## 3. No Indexing

```python
my_set = {10, 20, 30}
print(my_set[0])
```

Output

```python
TypeError
```

Sets do not support indexing.

---

# Creating a Set

## Method 1

```python
fruits = {"Apple", "Banana", "Mango"}
print(type(fruits))
```

Output

```python
<class 'set'>
```

---

## Method 2

```python
numbers = set([1, 2, 3, 4, 5])
print(numbers)
```

Output

```python
{1, 2, 3, 4, 5}
```

---

## Method 3

```python
letters = set("Hello")
print(letters)
```

Output

```python
{'H', 'e', 'l', 'o'}
```

The duplicate **l** is removed.

---

## Empty Set

```python
empty = {}
print(type(empty))
```

Output

```python
<class 'dict'>
```

Correct way

```python
empty = set()
print(type(empty))
```

Output

```python
<class 'set'>
```

---

# Set Methods

## add()

```python
fruits = {"Apple", "Banana", "Mango"}

fruits.add("Orange")
print(fruits)
```

Possible Output

```python
{'Apple', 'Banana', 'Mango', 'Orange'}
```

---

## remove()

```python
fruits.remove("Banana")
```

Removes Banana.

If the element does not exist, it raises **KeyError**.

---

## discard()

```python
fruits.discard("Grapes")
```

If the element does not exist, no error occurs.

---

## pop()

```python
removed = fruits.pop()
print(removed)
```

Removes and returns a random element.

---

## clear()

```python
fruits.clear()
print(fruits)
```

Output

```python
set()
```

---

# Set Operations

```python
class_a = {"Rohit", "Amit", "Priya", "Neha"}
class_b = {"Amit", "Raj", "Priya", "Sara"}
```

---

## Union ( | )

```python
print(class_a | class_b)
```

Output

```python
{'Rohit', 'Amit', 'Priya', 'Neha', 'Raj', 'Sara'}
```

All unique elements.

---

## Intersection ( & )

```python
print(class_a & class_b)
```

Output

```python
{'Amit', 'Priya'}
```

Common elements.

---

## Difference ( - )

```python
print(class_a - class_b)
```

Output

```python
{'Rohit', 'Neha'}
```

Elements only in Class A.

---

## Symmetric Difference ( ^ )

```python
print(class_a ^ class_b)
```

Output

```python
{'Rohit', 'Neha', 'Raj', 'Sara'}
```

Elements present in only one set.

---

# Set Comparison Methods

```python
a = {1,2,3}
b = {1,2,3,4,5}
c = {1,2,3}
```

```python
print(a.issubset(b))
```

Output

```python
True
```

---

```python
print(b.issuperset(a))
```

Output

```python
True
```

---

```python
d = {10,20,30}
print(a.isdisjoint(d))
```

Output

```python
True
```

---

```python
print(a == c)
```

Output

```python
True
```

---

# Looping Through a Set

```python
fruits = {"Apple", "Banana", "Mango", "Orange"}

for fruit in fruits:
    print(fruit)
```

Order is not guaranteed.

---

```python
print("Apple" in fruits)
```

Output

```python
True
```

---

```python
print(len(fruits))
```

Output

```python
4
```

---

# List vs Tuple vs Dictionary vs Set

| Feature          | List | Tuple | Dictionary | Set |
| ---------------- | ---- | ----- | ---------- | --- |
| Ordered          | ✅    | ✅     | ✅          | ❌   |
| Mutable          | ✅    | ❌     | ✅          | ✅   |
| Duplicate Values | ✅    | ✅     | Keys ❌     | ❌   |
| Indexing         | ✅    | ✅     | By Key     | ❌   |

---

# Real-Life Programs

## Program 1 – Remove Duplicates

```python
numbers = [1,5,2,3,2,4,5,1,3,6]

unique_numbers = list(set(numbers))

print("Original:", numbers)
print("Unique:", unique_numbers)
print("Original Count:", len(numbers))
print("Unique Count:", len(unique_numbers))
```

---

## Program 2 – Common Friends

```python
rohit_friends = {"Amit","Priya","Neha","Raj","Sara"}
amit_friends = {"Rohit","Priya","Raj","Kiran","Dev"}

print("Common:", rohit_friends & amit_friends)
print("Only Rohit:", rohit_friends - amit_friends)
print("Only Amit:", amit_friends - rohit_friends)
print("All Friends:", rohit_friends | amit_friends)
```

---

## Program 3 – Voting System

```python
voted = set()

while True:

    voter = input("Enter Voter ID (0 to stop): ")

    if voter == "0":
        break

    if voter in voted:
        print("Already voted.")
    else:
        voted.add(voter)
        print("Vote Registered.")

print("Total Votes:", len(voted))
print(voted)
```

---

# Common Mistakes

❌ Using `{}` for an empty set.

```python
{}
```

creates a dictionary.

Correct way

```python
set()
```

---

❌ Using indexing.

```python
my_set[0]
```

Sets have no indexing.

---

❌ Assuming order.

The order of a set is not fixed.

---

# Interview Questions

1. What is a Set?
2. How is a Set different from a List?
3. Why are duplicate values not allowed in a Set?
4. Why does a Set not support indexing?
5. Explain Union, Intersection, Difference and Symmetric Difference.
6. Difference between remove() and discard().
7. How can you remove duplicates from a List?

---

# ✅ Answers to Practice Questions

## Answer 1

```python
fruits = {"Apple", "Banana", "Orange", "Mango", "Grapes"}

fruits.add("Pineapple")

fruits.discard("Orange")

print("Is Mango present?", "Mango" in fruits)

print("Length:", len(fruits))

print(fruits)
```

---

## Answer 2

```python
rohit_subjects = {"Maths", "Physics", "Computer", "English"}

amit_subjects = {"Physics", "Chemistry", "English", "Biology"}

print("Common Subjects:")
print(rohit_subjects & amit_subjects)

print("Only Rohit's Subjects:")
print(rohit_subjects - amit_subjects)

print("Only Amit's Subjects:")
print(amit_subjects - rohit_subjects)

print("All Subjects:")
print(rohit_subjects | amit_subjects)
```

Output

```python
Common Subjects:
{'Physics', 'English'}

Only Rohit's Subjects:
{'Maths', 'Computer'}

Only Amit's Subjects:
{'Chemistry', 'Biology'}

All Subjects:
{'Maths', 'Physics', 'Computer', 'English', 'Chemistry', 'Biology'}
```

---

## Answer 3

```python
numbers = []

for i in range(10):
    num = int(input("Enter number: "))
    numbers.append(num)

unique_numbers = set(numbers)

duplicates = len(numbers) - len(unique_numbers)

print("Original List:", numbers)

print("Unique Numbers:", unique_numbers)

print("Duplicate Count:", duplicates)
```

---

## Answer 4

```python
sentence1 = input("Enter first sentence: ")
sentence2 = input("Enter second sentence: ")

set1 = set(sentence1.split())
set2 = set(sentence2.split())

print("Common Words:")
print(set1 & set2)

print("Only in First Sentence:")
print(set1 - set2)
```

Example

```
First:
I love Python programming

Second:
I love Java programming

Output

Common Words:
{'I', 'love', 'programming'}

Only in First Sentence:
{'Python'}
```

---

## Answer 5 (Without Running)

```python
a = {1, 2, 3, 4, 5}
b = {4, 5, 6, 7, 8}

print(a | b)
print(a & b)
print(a - b)
print(a ^ b)
print(3 in a)
print(len(a))
```

### Output

```python
{1, 2, 3, 4, 5, 6, 7, 8}

{4, 5}

{1, 2, 3}

{1, 2, 3, 6, 7, 8}

True

5
```

---

# 📍 Course Progress

```
✅ Lesson 1  → Print
✅ Lesson 2  → Variables
✅ Lesson 3  → Data Types
✅ Lesson 4  → Operators
✅ Lesson 5  → Strings
✅ Lesson 6  → User Input
✅ Lesson 7  → If/Else
✅ Lesson 8  → Loops
✅ Lesson 9  → Lists
✅ Lesson 10 → Tuples & Dictionaries
✅ Lesson 11 → Functions
✅ Lesson 12 → Sets
```

## Coming Next

```
⏳ Lesson 13 → File Handling
⏳ Lesson 14 → Exception Handling
⏳ Lesson 15 → Object-Oriented Programming (OOP)
⏳ Lesson 16 → Modules & Libraries
⏳ Lesson 17 → Mini Project 🚀
```


'''