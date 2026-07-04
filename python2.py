'''
Q1. Take a number from the user and check 
whether it is positive, negative, or zero.

'''

num = float(input("Enter Number: "))

if num > 0:
    print(f"{num} Ek Positive hai")
elif num < 0:
    print(f"{num} Ek Negative hai")
else:
    print("Zero Hai")

'''
Q2. Ask the user for their age and display the following:

0-12 → "You are a child"
13-17 → "You are a teenager"
18-60 → "You are an adult"
60+ → "You are a senior citizen" 
'''

umar = int(input("Enter Umar: "))

if umar >= 0 and umar <= 12:
    print("Aap bachche ho")
elif umar >= 13 and umar <= 17:
    print("Aap teenager ho")
elif umar >= 18 and umar <= 60:
    print("Aap adult ho")
elif umar < 60:
    print("Aap senior citizen ho")
else:
    print("Kripya sahi umar darj karein!")

'''
Q3. Create a simple login system:

Correct username: "admin" and password: "python123"
Get the username and password from the user
If both are correct → "Login successful! Welcome!"
If only the password is incorrect → "Incorrect password!"
If only the username is incorrect → "Incorrect username!"
If both are incorrect → "Both username and password are incorrect!"
'''

sahi_username = "admin"
sahi_password = "python123"

username = (input("Enter Username: "))
password = (input("Enter Password: "))

if username == sahi_username and password == sahi_password:
    print("Login successful! Welcome!")
elif username == sahi_username and password != sahi_password:
    print("Galat password!")
elif username != sahi_username and password == sahi_password:
    print("Galat username!")
else:
    print("Username aur password dono galat!")

'''
Q4. Take marks for three subjects from the user:

Pass in all three (>=33) → "PASS"
Fail in any one → "COMPARTMENT"
Fail in two or three → "FAIL"
'''

sub1 = float(input("Enter Sub1 Marks: "))
sub2 = float(input("Enter Sub2 Marks: "))
sub3 = float(input("Enter Sub3 Marks: "))

fail_count = 0

if sub1 < 33:
    fail_count += 1
if sub2 < 33:
    fail_count += 1
if sub3 < 33:
    fail_count += 1

if fail_count == 0:
    print("PASS")
elif fail_count == 1:
    print("COMPARTMENT")
else:
    print("FAIL")

