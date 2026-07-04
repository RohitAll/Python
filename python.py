'''Q1. Apna poora naam ek string mein likho aur:

Poora naam CAPITAL mein print karo
Poora naam small mein print karo
Naam ke kitne characters hain print karo
Naam ka pehla aur aakhri character print karo '''

name = "Rohit kumar"

print(name.upper())
print(name.lower())
print(len(name))
print(name[0])
print(name[-1])

'''Q2. Is string se kaam karo:
pythondate = "26-01-1950"

Slicing use karke din, mahina, aur saal alag alag print karo'''

date = "26-01-1950"

din = date[0:2]
mahina = date[3:5]
saal = date[6:]

print(f"din: {din} \nmahina: {mahina} \nsaal: {saal}")

'''Q3. f-string use karke apna biodata print karo:

Naam, umar, sheher, course - sab ek saath ek sentence mein'''

name = "rohit kumar"
umar = 20
sheher =  "siwan"
course = "BCA"
print("name:", name)
print("umar:", umar)
print("sheher:", sheher)
print("course:", course)

'''Q4. Ye program likho:
pythontext = "   python programming   "

Space hatao
Title case mein print karo
"programming" ko "language" se replace karo'''

text = "   python programming   "


clean_text = text.strip()    
print(clean_text) 

title_text = clean_text.title()
print(title_text)

replaced_text = clean_text.replace("programming", "language") 
print(replaced_text)                   

# Q5. Exam Question:
s = "Hello World"
print(s[6:]) #World
print(s[:5]) #Hello
print(s[-5:]) #World 
