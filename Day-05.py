# Lesson 5: String Operations (Working with Text) 📝

## What is a String? (Quick Revision)
'''
In **Lesson 3**, we learned that a **String = Text data** written inside quotation marks.

```python
name = "Rohit Kumar"
city = "Siwan"
```

In this lesson, we will learn **what we can do with strings**.

---

# 1️⃣ String Concatenation (Joining Strings) 🔗

```python
# Real-life example: Joining first name and last name

first_name = "Rohit"
last_name = "Kumar"

# Use the + operator to join strings
full_name = first_name + " " + last_name
print(full_name)    # Output: Rohit Kumar
```

### Explanation of each line:

| Code                     | Meaning                   |
| ------------------------ | ------------------------- |
| `first_name + last_name` | Joins both strings        |
| `" "`                    | Adds a space between them |

```python
# More examples

city = "Siwan"
state = "Bihar"

address = city + ", " + state
print(address)      # Output: Siwan, Bihar

# Joining a number with a string
age = 20
message = "My age is: " + str(age)   # Convert number to string first
print(message)      # Output: My age is: 20
```

---

# 2️⃣ String Repetition 🔁

```python
# Use the * operator to repeat a string

print("Ha" * 3)         # Output: HaHaHa
print("-" * 20)         # Output: --------------------
print("Python! " * 2)   # Output: Python! Python!
```

### Real-life use

```python
# Creating a separator line

print("=" * 30)
print("    Student Report Card    ")
print("=" * 30)
```

**Output**

```
==============================
    Student Report Card
==============================
```

---

# 3️⃣ String Length - `len()` Function 📏

```python
# len() returns the total number of characters in a string

name = "Rohit Kumar"
print(len(name))        # Output: 11

# Spaces are also counted
print(len("Hello"))     # Output: 5
print(len("Hi There"))  # Output: 8
print(len(""))          # Output: 0
```

### Real-life use

```python
# Password length check

password = "abc123"
print(len(password))    # Output: 6

# Password is less than 8 characters, so it is weak.
```

---

# 4️⃣ String Indexing 🎯

```python
# Every character has an index.
# Index starts from 0.

name = "Rohit"
#Index: 01234

print(name[0])   # Output: R (first character)
print(name[1])   # Output: o (second character)
print(name[4])   # Output: t (fifth character)

# Negative indexing starts from the end

print(name[-1])  # Output: t (last character)
print(name[-2])  # Output: i (second last character)
```

### Real-life example

```python
# Getting the first and last digit of a mobile number

mobile = "9876543210"

print(mobile[0])     # Output: 9
print(mobile[-1])    # Output: 0
```

> ⚠️ **Common Mistake**

```python
name = "Rohit"

print(name[5])   # ❌ Error! Valid indexes are 0 to 4.
```

---

# 5️⃣ String Slicing ✂️

```python
# string[start:end]
# Returns characters from start to end-1

name = "Rohit Kumar"
#Index: 01234567891011

print(name[0:5])    # Output: Rohit
print(name[6:11])   # Output: Kumar
print(name[0:3])    # Output: Roh

# Shortcuts

print(name[:5])     # Output: Rohit
print(name[6:])     # Output: Kumar
print(name[:])      # Output: Rohit Kumar
```

### Real-life example

```python
# Extracting day, month, and year from a date

date = "15-08-1947"

day = date[0:2]
month = date[3:5]
year = date[6:]

print("Day:", day)
print("Month:", month)
print("Year:", year)
```

**Output**

```
Day: 15
Month: 08
Year: 1947
```

---

# 6️⃣ String Methods 🛠️

```python
text = "rohit kumar"

# Uppercase and lowercase
print(text.upper())        # Output: ROHIT KUMAR
print(text.lower())        # Output: rohit kumar
print(text.title())        # Output: Rohit Kumar
print(text.capitalize())   # Output: Rohit kumar

# Removing spaces

text2 = "   Hello Python   "

print(text2.strip())       # Output: Hello Python
print(text2.lstrip())      # Output: Hello Python
print(text2.rstrip())      # Output:    Hello Python

# Replacing text

text3 = "I love Java"

print(text3.replace("Java", "Python"))
# Output: I love Python

# Counting characters

text4 = "banana"

print(text4.count("a"))    # Output: 3

# Finding text

text5 = "Rohit Kumar"

print(text5.find("Kumar")) # Output: 6
```

---

# 7️⃣ String Formatting - f-Strings 🌟

This is the **most modern** and **recommended** way to insert variables into a string.

```python
name = "Rohit"
age = 20
city = "Siwan"

message = f"My name is {name}, I am {age} years old, and I live in {city}."

print(message)
```

**Output**

```
My name is Rohit, I am 20 years old, and I live in Siwan.
```

### More examples

```python
marks = 85.5

result = f"Your marks are {marks} and your percentage is {marks}%."

print(result)
```

Output

```
Your marks are 85.5 and your percentage is 85.5%.
```

### You can also perform calculations inside f-strings

```python
a = 10
b = 20

print(f"The sum of {a} and {b} is {a + b}")
```

Output

```
The sum of 10 and 20 is 30
```

---

# Real-Life Program - Student ID Card 🪪

```python
# Student ID Card

name = "Rohit Kumar"
roll = 101
course = "BCA"
year = 2
percentage = 87.5

print("=" * 35)
print("      STUDENT ID CARD      ")
print("=" * 35)

print(f"Name       : {name}")
print(f"Roll No    : {roll}")
print(f"Course     : {course}")
print(f"Year       : {year}")
print(f"Percentage : {percentage}%")
print(f"Initial    : {name[0]}.")

print("=" * 35)
```

**Output**

```
===================================
      STUDENT ID CARD
===================================
Name       : Rohit Kumar
Roll No    : 101
Course     : BCA
Year       : 2
Percentage : 87.5%
Initial    : R.
===================================
```

---

# Common Mistakes ⚠️

```python
# ❌ Mistake 1: Index starts from 0, not 1

name = "Rohit"

print(name[1])    # Output: o, not R
```

```python
# ❌ Mistake 2: Joining a string with a number

print("Age: " + 20)        # Error
print("Age: " + str(20))   # Correct
print(f"Age: {20}")        # Better
```

```python
# ❌ Mistake 3: Forgetting parentheses after a method

name = "rohit"

print(name.upper)     # Prints the function object
print(name.upper())   # Correct: ROHIT
```

---

# 🎓 Important Exam & Interview Questions

1. Why does string indexing start from **0**?
2. What does the `len()` function do?
3. In slicing `[start:end]`, is the **end index included or excluded**?
4. What is an **f-string**, and why is it used?
5. What do the `strip()`, `replace()`, and `find()` methods do?

---

# 📝 Practice Questions

### Q1.

Store your full name in a string and:

* Print it in **UPPERCASE**
* Print it in **lowercase**
* Print the total number of characters
* Print the first and last character

---

### Q2.

Use this string:

```python
date = "26-01-1950"
```

Using slicing, print:

* Day
* Month
* Year

---

### Q3.

Use an **f-string** to print your biodata in one sentence.

Include:

* Name
* Age
* City
* Course

---

### Q4.

Write a program:

```python
text = "   python programming   "
```

* Remove extra spaces
* Convert it to Title Case
* Replace `"programming"` with `"language"`

---

### Q5. Exam Question

Without running the code, predict the output.

```python
s = "Hello World"

print(s[6:])
print(s[:5])
print(s[-5:])
```

---

## **Answers to Practice Questions – Lesson 5: String Operations**

---

# ✅ Q1. Full Name Operations

```python
name = "Rohit Kumar"

# Print in uppercase
print(name.upper())

# Print in lowercase
print(name.lower())

# Print total number of characters
print(len(name))

# Print first character
print(name[0])

# Print last character
print(name[-1])
```

### **Output**

```
ROHIT KUMAR
rohit kumar
11
R
r
```

---

# ✅ Q2. Extract Day, Month, and Year

```python
date = "26-01-1950"

day = date[0:2]
month = date[3:5]
year = date[6:]

print("Day:", day)
print("Month:", month)
print("Year:", year)
```

### **Output**

```
Day: 26
Month: 01
Year: 1950
```

---

# ✅ Q3. Biodata Using f-String

```python
name = "Rohit Kumar"
age = 20
city = "Siwan"
course = "BCA"

print(f"My name is {name}. I am {age} years old. I live in {city} and I am studying {course}.")
```

### **Output**

```
My name is Rohit Kumar. I am 20 years old. I live in Siwan and I am studying BCA.
```

---

# ✅ Q4. String Methods

```python
text = "   python programming   "

# Remove extra spaces
text = text.strip()

# Convert to Title Case
print(text.title())

# Replace programming with language
print(text.replace("programming", "language"))
```

### **Output**

```
Python Programming
python language
```

---

# ✅ Q5. Predict the Output

### **Code**

```python
s = "Hello World"

print(s[6:])
print(s[:5])
print(s[-5:])
```

### **Answer**

```
World
Hello
World
```

### **Explanation**

* `s[6:]` → Prints from index **6** to the end → **World**
* `s[:5]` → Prints from the beginning to index **4** → **Hello**
* `s[-5:]` → Prints the last **5** characters → **World**

                                                    
'''
