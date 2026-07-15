'''

---

# 📚 Lesson 10: Tuples & Dictionaries

## 📦 First, Let's Learn Tuples

---

# What is a Tuple?

### Real-life Example

Think about your **Aadhaar Card**.

It contains information like:

* Name: Rohit Kumar
* Date of Birth: 15/08/2004
* Aadhaar Number: 1234-5678-9012

This information usually **does not change**.

A **Tuple** is just like that. Once it is created, **its values cannot be changed**.

```python
# List - Can be changed ✅
fruits_list = ["Apple", "Banana", "Mango"]
fruits_list[0] = "Orange"

# Tuple - Cannot be changed ❌
fruits_tuple = ("Apple", "Banana", "Mango")
fruits_tuple[0] = "Orange"   # Error
```

---

# Creating Tuples

```python
# String tuple
colors = ("Red", "Green", "Blue")

# Integer tuple
coordinates = (10, 20)

# Mixed tuple
student = ("Rohit", 20, "BCA", 85.5)

# Single element tuple
single = (42,)
not_tuple = (42)

# Tuple without parentheses
point = 10, 20

print(type(point))
print(type(colors))
```

Output

```
<class 'tuple'>
<class 'tuple'>
```

---

# Tuple Properties

```python
coordinates = (10, 20, 30, 40, 50)

print(coordinates[0])
print(coordinates[-1])

print(coordinates[1:4])

print(len(coordinates))

for item in coordinates:
    print(item)

print(30 in coordinates)
print(99 in coordinates)

nums = (1, 2, 2, 3, 2, 4)

print(nums.count(2))
print(nums.index(3))
```

Output

```
10
50
(20, 30, 40)
5
10
20
30
40
50
True
False
3
3
```

---

# Tuple Unpacking ⭐

```python
student = ("Rohit", 20, "Siwan", "BCA")

name, age, city, course = student

print(name)
print(age)
print(city)
print(course)

x, y = (10, 20)

print(f"X = {x}, Y = {y}")

a = 5
b = 10

a, b = b, a

print(a, b)
```

Output

```
Rohit
20
Siwan
BCA
X = 10, Y = 20
10 5
```

---

# List vs Tuple

| Feature  | List []         | Tuple ()      |
| -------- | --------------- | ------------- |
| Mutable  | ✅ Yes           | ❌ No          |
| Speed    | Slightly slower | Faster        |
| Use Case | Changing data   | Fixed data    |
| Example  | Shopping cart   | Date of Birth |
| Methods  | Many            | Few           |

Example

```python
months = (
    "Jan","Feb","Mar","Apr","May","Jun",
    "Jul","Aug","Sep","Oct","Nov","Dec"
)

days = (
    "Mon","Tue","Wed","Thu",
    "Fri","Sat","Sun"
)

cart = ["Apple", "Milk"]
students = ["Rohit", "Amit"]
```

---

# 📖 Dictionaries

---

# What is a Dictionary?

### Real-life Example

Think about an English Dictionary.

```
Apple → A fruit
Water → A liquid
Computer → An electronic machine
```

Every **word** has a **meaning**.

Similarly, a Python Dictionary stores data as

```
Key → Value
```

Example

```python
student = {
    "name": "Rohit Kumar",
    "age": 20,
    "city": "Siwan",
    "course": "BCA",
    "percentage": 87.5
}

print(student)
```

---

# Creating Dictionaries

```python
empty = {}

student = {
    "name": "Rohit",
    "roll": 101,
    "marks": 85.5
}

mixed = {
    "language": "Python",
    1: "One",
    (1,2): "Tuple Key"
}

print(type(student))
```

Output

```
<class 'dict'>
```

---

# Accessing Values

```python
student = {
    "name": "Rohit",
    "age": 20,
    "city": "Siwan"
}

print(student["name"])

print(student.get("name"))

print(student.get("phone"))

print(student.get("phone", "Not Available"))
```

Output

```
Rohit
Rohit
None
Not Available
```

---

# Add and Update Values

```python
student = {
    "name": "Rohit",
    "age": 20
}

student["city"] = "Siwan"

student["course"] = "BCA"

student["age"] = 21

student.update({
    "age":22,
    "state":"Bihar"
})

print(student)
```

Output

```
{
'name':'Rohit',
'age':22,
'city':'Siwan',
'course':'BCA',
'state':'Bihar'
}
```

---

# Remove Values

```python
student = {
    "name":"Rohit",
    "age":20,
    "city":"Siwan"
}

student.pop("city")

del student["age"]

print(student)

student.clear()

print(student)
```

Output

```
{'name': 'Rohit'}
{}
```

---

# Dictionary Methods

```python
student = {
    "name":"Rohit",
    "age":20,
    "city":"Siwan"
}

print(student.keys())

print(student.values())

print(student.items())

print("name" in student)

print("phone" in student)

print(len(student))
```

Output

```
dict_keys(['name', 'age', 'city'])
dict_values(['Rohit', 20, 'Siwan'])
dict_items([('name','Rohit'),('age',20),('city','Siwan')])
True
False
3
```

---

# Looping Through Dictionaries

```python
student = {
    "name":"Rohit",
    "age":20,
    "city":"Siwan"
}

for key in student:
    print(key)

for key,value in student.items():
    print(key, value)
```

---

# Real World Program 1

## Phone Book

```python
phone_book = {}

while True:

    print("\n1.Add Contact")
    print("2.Search Contact")
    print("3.Delete Contact")
    print("4.Show Contacts")
    print("5.Exit")

    choice = input("Enter choice: ")

    if choice == "1":
        name = input("Enter Name: ")
        number = input("Enter Number: ")
        phone_book[name] = number

    elif choice == "2":
        name = input("Enter Name: ")
        print(phone_book.get(name,"Contact Not Found"))

    elif choice == "3":
        name = input("Enter Name: ")
        phone_book.pop(name,None)

    elif choice == "4":
        for name,number in phone_book.items():
            print(name,number)

    elif choice == "5":
        break
```

---

# Real World Program 2

## Student Report Card

```python
students = {
    "Rohit":{"Math":85,"Science":90,"English":78},
    "Amit":{"Math":72,"Science":68,"English":85},
    "Priya":{"Math":95,"Science":92,"English":88}
}

for student,marks in students.items():

    total = sum(marks.values())

    average = total / len(marks)

    print(student)
    print("Total =",total)
    print("Average =",average)
```

---

# Common Mistakes

```python
student = {"name":"Rohit"}

print(student.get("phone","Not Found"))

d = {"a":1,"a":2,"a":3}

print(d)

# Output
{'a':3}
```

---

# Interview Questions

1. What is the difference between List and Tuple?
2. What are keys and values in a Dictionary?
3. What is the difference between `dict[key]` and `dict.get(key)`?
4. Can a Dictionary have duplicate keys?
5. What is Tuple Unpacking?
6. What do `keys()`, `values()`, and `items()` return?

---

# 📝 Practice Questions with Answers

## ✅ Answer 1

```python
student = ("Rohit", 20, "Siwan", "BCA")

name, age, city, course = student

print(name)
print(age)
print(city)
print(course)

print(age in student)
```

Output

```
Rohit
20
Siwan
BCA
True
```

---

## ✅ Answer 2

```python
phone = {
    "Brand": "Samsung",
    "Model": "Galaxy S24",
    "Price": 75000,
    "Color": "Black",
    "RAM": "8 GB"
}

print(phone.keys())

print(phone.values())

phone["Price"] = 70000

phone["Battery"] = "5000 mAh"

print(phone)
```

Output

```
dict_keys(['Brand', 'Model', 'Price', 'Color', 'RAM'])
dict_values(['Samsung', 'Galaxy S24', 75000, 'Black', '8 GB'])
{
'Brand':'Samsung',
'Model':'Galaxy S24',
'Price':70000,
'Color':'Black',
'RAM':'8 GB',
'Battery':'5000 mAh'
}
```

---

## ✅ Answer 3

```python
marks = {
    "Maths":85,
    "Science":90,
    "English":78,
    "Hindi":82,
    "Computer":95
}

for subject, mark in marks.items():
    print(subject, mark)

total = sum(marks.values())

average = total / len(marks)

highest = max(marks, key=marks.get)

print("Total =", total)
print("Average =", average)
print("Highest =", highest, marks[highest])
```

Output

```
Maths 85
Science 90
English 78
Hindi 82
Computer 95

Total = 430
Average = 86.0
Highest = Computer 95
```

---

## ✅ Answer 4

```python
sentence = input("Enter a sentence: ")

words = sentence.split()

count = {}

for word in words:
    count[word] = count.get(word, 0) + 1

print(count)
```

Example

Input

```
python is easy python is powerful
```

Output

```
{
'python':2,
'is':2,
'easy':1,
'powerful':1
}
```

---

## ✅ Answer 5

```python
t = (1, 2, 3, 4, 5)
d = {"a": 10, "b": 20, "c": 30}

print(t[1:4])
print(d.get("b"))
print(d.get("z", 0))
print(list(d.keys()))
```

### Output

```
(2, 3, 4)
20
0
['a', 'b', 'c']
```

---

'''