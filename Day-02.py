#LESSON 2: Variables

'''
Lesson 2: Variables (Chare/Dabba) 📦

What is a variable?
Let's understand it with a real-life example:
Imagine you have a container at home. You can put anything in it—salt, sugar, or rice—and attach a label to indicate what is inside.
In Python, a variable is just like that container: we use it to store data (information) and give it a name.
'''
#naam = "Rohit Kumar"
#umar = 20
#sheher = "Patna"

'''
Here:
'Name' is a box containing "Rohit Kumar"
'Age' is a box containing 20
'City' is a box containing "Patna"

Creating a variable

 Variable banane ka tarika:
 variable_naam = value
'''

#naam = "Rohit"       # String variable (text)
#umar = 20            # Integer variable (poori sankhya)
#height = 5.9         # Float variable (dashamlav wali sankhya)
#student = True       # Boolean variable (Haan/Nahi)

'''
Meaning of each line:

Line                     | Meaning
name = "Rohit"           | Store the text "Rohit" in the container named 'name'
age = 20                 | Store the number 20 in the container named 'age'
height = 5.9             | Store 5.9 in the container named 'height'
student = True           | Store True (yes) in the container named 'student'
=                        | This is the assignment operator – meaning "store in the container"

Printing the variable
'''

#name = "Rohit Kumar"
#age = 20
#shehar = "Patna"

#print(name) # Output: Rohit Kumar
#print(age) # output: 20
#print(city) # output: patna
'''
💡 Note: You don't use quotes when printing a variable—you just write the variable's name!

Changing the value of a variable
'''
# Variable ki khoobsoorti ye hai ki iska value change ho sakta hai!

# score = 10
# print(score)    # Output: 10

# score = 50      # Value badal di
# print(score)    # Output: 50

# score = 100     # Phir se badal di
# print(score)    # Output: 100
'''
Real-life example: Just like a scoreboard in cricket—where the runs keep increasing—the score variable changes in the same way!
Variable Naming Rules
# ✅ VALID variable names:
student_name = "Rohit"    # You can use an underscore (_)
age2 = 20                 # A number can be at the end
_city = "Delhi"           # It can start with an underscore
myName = "Rohit"          # camelCase is also fine

# ❌ INVALID variable names:
2age = 20         # Cannot start with a number
my-name = "Rohit" # Cannot use a hyphen (-)
my name = "Rohit" # Cannot contain a space
class = "10th"    # 'class' is a reserved word in Python

A real-life program
# Student Biodata Program

Name = "Rohit Kumar"
Age = 20
City = "Patna"
Course = "BCA"
Percentage = 85.5

print("=== Student Biodata ===")
print(name)
print(age)
print(city)
print(course)
print(percentage)

Output:
===Student Biodata===
Rohit Kumar
20
Patna
bca
85.5

Best Practices (Good Habits) 💡
# ✅ Accha: Meaningful naam do
student_age = 20
total_marks = 450

# ❌ Bura: Meaningless naam
a = 20
x = 450

# ✅ Accha: snake_case use karo (Python standard)
first_name = "Rohit"
last_name = "Kumar"

🎓 Important Exam/Interview Questions

What is a variable?
What is the syntax for declaring a variable in Python?
What are the rules for naming variables? (Cannot start with a number, no spaces, no reserved words)
Do you have to declare the variable type in Python? (Answer: No! Python automatically determines it—this is called Dynamic Typing)


📝 Practice Questions
Q1. Create your own biodata—store your name, age, city, and favorite subject in separate variables and print them.
name = "Rohit Kumar"
umar = 20
sheher = "Siwan"
favourite_subject = "Maths " # ⚠️ Spelling mistake

print("=== My Biodata ===")
print("name:", name)
print("umar:", umar)
print("shehar:", sheher)
print("favourite subject:", favourite_subject)

Q2. Identify which variable names are valid and which are invalid, and explain why:
my_name
2rollno
student name
_marks
class
yes
no
no
yes
no

Q3. Write a program that:

First, assigns 0 to a variable named `score` and prints it.
Then, assigns 100 to the same `score` variable and prints it.


Q4. Exam question: Do you have to declare a variable's data type beforehand in Python? (Yes or No) – Explain in one line.
"In Python, you don't have to declare the variable's data type beforehand."
That's right! But keep one important term in mind:

This is called "Dynamic Typing" – Python automatically figures out the data type itself!

📊 Lesson 2 Summary - Yaad Rakho:

Variable = Data store karne ka dabba
= matlab "dabbe mein rakho" (assignment)
Variable naam number se shuru nahi ho sakta
Variable naam mein space nahi hoti
Reserved keywords variable naam nahi ban sakte
Python mein Dynamic Typing hoti hai - type khud detect hoti hai
'''