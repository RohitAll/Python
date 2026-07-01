# Q1. Ek Python program likho jo aapka naam print kare.
print("Rohit Kumar")

# Q2. 3 alag lines mein print karo: "I", "Love", "Python"
print("I")
print("Love")
print("Python")

# Q3. Batao - Sahi hai ya Galat, aur kyun:
# print("Namaste")
# print(Namaste)
# Print("Namaste") 

# pahla code sahi hai, dusra code mai  quotes  ("") nahi laga hai is liye galat hai , teesra code mai print Mai P ek capital latter hai jab ki python ek case-sensitive languge hai is liye galat hai

# Q4. print() function ka kaam apne shabdon mein samjhao.
 
# print() ka kam code ko sceen par dhikhana hota hai 


# ✅ Mini Quiz (Lesson 1 se)

# Q1. Python ek _______ language hai.
# Q2. Text data ko Python mein kya kehte hain?
# Q3. Kya Python case-sensitive hai?

# 1 . programing
# 2. string
# 3. haan 



# Q1. Apna khud ka biodata banao - naam, umar, sheher, favourite subject - sab alag-alag variables mein rakho aur print karo.

naam = "Rohit Kumar"
umar = 20
sheher = "Siwan"
favourite_subject = "Maths"

print("=== My Biodata ===")
print("name:", naam)
print("umar:", umar)
print("shehar:", sheher)
print("favourite subject:", favourite_subject)


# Q2. Ye batao - kaunse variable naam sahi hain aur kaunse galat, aur kyun:

# my_name
# 2rollno
# student name
# _marks
# class

# 1. sahi hai
# 2. galat rull kahta hai ki number variable ke aage nahi aasakta hai
# 3. galat rull kahta hai ki variable space nahi aasakta hai
# 4. sahi hai
# 5. galat kyu class ek python Reserved Keyword hai

# Q3. Ek program likho jisme:

# score variable mein pehle 0 rakho aur print karo
# Phir usi score variable mein 100 rakho aur print karo

score = 0
print(score)

score = 100
print(score)

# Q4. Exam question: Python mein variable ka data type pehle se declare karna padta hai? (Haan ya Nahi) - Ek line mein samjhao.

# python mai variable ka data type pehle declare nahi karna padta hai  Python khud automatically data ka type samajh leta hai!

# Q1. Neeche diye gaye values ke liye sahi data type batao:

# "Bihar" → ?
# 99 → ?
# 3.14 → ?
# False → ?
# "True" → ?  (dhyan se socho!)

# 1. string  
# 2. integer
# 3. float
# 4. bool
# 5. string  

# Q2. Ye program likho:

# Ek variable price banao jisme 150.75 rakho
# Ek variable quantity banao jisme 3 rakho
# total variable mein dono multiply karo (price * quantity)
# Sab print karo

price = 150.75
quantity = 3

total = price * quantity

print("price:", price)
print("quantity: ", quantity)
print("totle:", total)

# Q3. type() function use karke in sab ka type print karo:
a = 100
b = 3.14
c = "Python"
d = True

print(type(a))
print(type(b))
print(type(c))
print(type(d))

# Q4. Type conversion karo:

# "25" ko integer mein badlo aur us mein 5 jodo, result print karo
num = "25"
num1 = int(num)

print(num1 + 5)
 
# 99 ko string mein badlo aur " marks mile" ke saath print karo
num2 = 99
num3 = str(num2)

print(num3 + " marks mile")

# Q5. Exam Question: int("99.5") chalega ya nahi? Kya hoga? (Sochke jawab do!)
# Yeh kyu nahi chalega?  decimal point (.) hone se aur string ke andar sirf pure integers (jaise "99") expect karta hai.

