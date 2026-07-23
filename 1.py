
# n = int(input("which table you want : -"))

# for i in range(1,11):
#     print(f"{n} * {i} = {n*i}")



# n = int(input("please tell your number :- ") )

# fact = 1

# for i in range(1,n+1):
#     fact = fact * i

# print(f"your factorial is {fact}")



# n = int(input("check your number is perfect or not :- "))
# sum = 0
# for i in range(1,n):
#     if n%i == 0:
#         sum = sum + i

# if sum == n:
#     print("your number is perfect")
# else:
#     print("not a perfect number")


# for i in range(10):
#     print("Hello World")

#     i = 1
# while i <= 10:
#     print("Hello World")
#     i += 1

# print(("Hello World\n") * 10)

# [print("Hello World") for _ in range(10)]

n = int(input ("check your number is prime or not :- ") )

count = 0

for i in range(1,n+1):
    if n%i == 0:
        count = count + 1

if count == 2:
    print("your number is prime")
else:
    print("your number is not prime")
