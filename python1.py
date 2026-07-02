'''Q1. Ek program banao jo:

User se naam aur umar lo
f-string use karke print karo:
"Namaste [naam]! Tum [umar] saal ke ho."'''

name = input("apna name dalo: ")
umar = int(input("apna umar dalo: "))

print(f"namaste {name}! Tum {umar} saal ke ho")

'''Q2. Simple Interest Calculator banao:

User se Principal (Mool rakam), Rate (byaj dar), Time (samay) lo
Formula: SI = (P * R * T) / 100
Result print karo'''

principal = int(input("enter ypur Principal: "))
rate = int(input("enter ypur Rate: "))
time = int(input("enter ypur Time: "))

SI = (principal * rate * time) / 100

print(SI)

'''Q3. User se apna poora naam lo aur:

CAPITAL mein print karo
Kitne characters hain batao
Pehla aur aakhri character print karo'''

name = input("apna name dalo: ")

print(name.upper())
print(len(name))
print(name[0])
print(name[-1])

'''Q4. Temperature Converter banao:

User se Celsius mein temperature lo
Fahrenheit mein convert karo
Formula: F = (C * 9/5) + 32
Result print karo jaise: "25°C = 77.0°F"'''

celsius = float(input("Enter temperature in Celsius: "))
fahrenheit = (celsius * 9/5) + 32

print(f"{celsius}°C = {fahrenheit}°F")

'''Q5. Exam Question:
pythonx = input("Number likho: ")
print(x + 10)
Isme kya galti hai? Sahi karo aur explain karo.'''

# Jab aap x + 10 karte hain, toh Python ek text (string) aur ek number (integer) ko aapas mein jod nahi paata, jiski wajah se TypeError aata hai.Sahi Code (Corrected Code)Is galti ko sudharne ke liye aapko input() ke aage int() ya float() lagana hoga taaki text number mein badal jaye:
x = int(input("Number likho: "))
print(x + 10)
#Galti ka Explanation:Galti: Agar user 5 likhta hai, toh Python use "5" (text) samajhta hai. Python mein "5" + 10 mathematically possible nahi hai.Sudhaar: int(...) lagane se "5" badal kar 5 (actual number) ho jata hai. Ab 5 + 10 ka sahi result 15 print hoga.Agar aapko decimal waale numbers (jaise 5.5) ke liye bhi ise sahi karna hai, toh aap int() ki jagah float() ka use kar sakte hai