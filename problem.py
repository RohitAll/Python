#1. Add Two Numbers
add = lambda a, b: a + b
print(add(10, 20))

#2. Square of a Number
square = lambda x: x ** 2
print(square(5))

#3. Cube of a Number
cube = lambda x: x ** 3
print(cube(4))

#4. Find Maximum
maximum = lambda a, b: a if a > b else b
print(maximum(15, 9))

#5. Find Minimum
minimum = lambda a, b: a if a < b else b
print(minimum(15, 9))

#6. Check Even or Odd
check = lambda x: "Even" if x % 2 == 0 else "Odd"
print(check(7))

#7. Check Positive or Negative
check = lambda x: "Positive" if x > 0 else "Negative"
print(check(-8))

#8. Multiply Three Numbers
multiply = lambda a, b, c: a * b * c
print(multiply(2, 3, 4))

#9. Find Length of String
length = lambda s: len(s)
print(length("Python"))

#10. Convert to Uppercase
upper = lambda s: s.upper()
print(upper("python"))

#11. Reverse a String
reverse = lambda s: s[::-1]
print(reverse("Python"))

#12. Last Character
last = lambda s: s[-1]
print(last("Python"))

#13. First Character
first = lambda s: s[0]
print(first("Python"))

#14. Sum of List
numbers = [10, 20, 30, 40]
total = lambda lst: sum(lst)
print(total(numbers))

#15. Sort List
numbers = [5, 2, 9, 1, 7]
numbers.sort(key=lambda x: x)
print(numbers)

#16. Sort List of Tuples
students = [("Ram", 70), ("Shyam", 90), ("Mohan", 80)]

students.sort(key=lambda x: x[1])

print(students)

#17. Filter Even Numbers
numbers = [1,2,3,4,5,6,7,8,9,10]

even = list(filter(lambda x: x % 2 == 0, numbers))

print(even)

#18. Double Every Number
numbers = [1,2,3,4,5]

double = list(map(lambda x: x * 2, numbers))

print(double)

#19. Square Every Number
numbers = [1,2,3,4,5]

square = list(map(lambda x: x ** 2, numbers))

print(square)

#20. Filter Names Starting with 'A'
names = ["Amit", "Rahul", "Ankit", "Rohit", "Ajay"]

result = list(filter(lambda x: x.startswith("A"), names))

print(result)