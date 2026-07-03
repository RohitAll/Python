for i in range(1 ,11):
    print(i)

for i in range(1, 11):
    if i % 2 == 0:
        print(i)

for i in range(1, 11):
    if i % 2 != 0:
        print(i)

total_sum = 0
print("Numbers enter karte jao (Stop karne ke liye '0' dabayein):")

while True:
    num = int(input("Enter a number: "))

    if num == 0:
        break
    total_sum += num
print("---")
print(f"Sabhi enter kiye gaye numbers ka kul jod (Sum) hai: {total_sum}")

num = int(input("Enter number: "))

for i in range(1, 11):
    print(f"{num} X {i} = {num * i}")      


n = 5

for i in range(1, n + 1):
    for j in range(1, i + 1):
        print(j, end=" ")
    print()
        

number = 42
chances = 0

print("--- Welcome to the Number Guessing Game! ---")
print("Maine ek number socha hai (1 se 100 ke beech). Guess karo!")

while True:

    guess = int(input("\nApna guess enter karein: "))
    chances += 1

    if guess == number:
        print(f"🎉 Shabash! Tumne {chances} chances mein sahi guess kiya!")
        break
    elif guess > number:
        print("❌ Zyada hai! Thoda chota number socho.")
    else:
        print("❌ Kam hai! Thoda bada number socho.")

