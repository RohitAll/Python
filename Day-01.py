#Lesson 1: Python Introduction and First Program

'''
## What is Python?
Python is a **programming language**—meaning it is a language used to give instructions to a computer on what tasks to perform.

**Understand it with a real-life example:** Just as you might write down a recipe for a new cook—"first chop the onions, then heat the oil, then add the onions"—we write step-by-step instructions for the computer in Python. The computer follows those instructions.

### Why is Python popular?

- **Easy to learn** - its syntax (the way it is written) is as simple as English
- **Versatile** - you can use it to build websites, perform data analysis, create AI/Machine Learning models, develop games, automate tasks—it can do it all
- **Used by major companies** - Google, Instagram, Netflix, and NASA all use Python

## How do you run Python?

To write Python code, we need an "interpreter" that can read and understand our code. You can use these options:

1. **Online compiler** - such as replit.com or programiz.com (you can run it directly in your browser; no installation required)
2. **Install on your computer** - by downloading it from python.org

For now, I suggest opening any **online Python compiler** in your browser so you can test your code immediately.

## Your First Python Program

There is a tradition in learning programming where the very first program involves printing "Hello World." Let's do it:
'''
#print("Hello World")

'''
Simply write this code and run it. The output will be:

```
Hello World
```

### Line-by-line explanation of this code:

| Code part                   | Meaning |

| | `print(...)`              | This is a Python **built-in function** used to display something (produce output) on the screen. |
| `"Hello World"`             | This is a **string**—meaning text data. Whatever you write inside the double quotes `" "` will be printed exactly as it is. |
| `()` round brackets         | These tell the function: "Process whatever is inside." |

**Real-life analogy:** The `print()` function is like a parrot—it repeats whatever you tell it. `print("Hello World")` essentially means "say this phrase (display it on the screen)."

 Here is another example:
'''

#print("I am learning Python")
#print("This is my second program")

'''
Output:
```
I am learning Python
This is my second program
```

Here, there are two separate `print()` statements, which is why the output appears on two separate lines. Each `print()` automatically starts on a **new line**. 

## Important Points to Remember

- A string is always written inside quotes (`" "` or `' '`).
- Python is **case-sensitive**—meaning `Print` and `print` are different things (`Print` will cause an error because the function name in Python is always the lowercase `print`).
- Each statement (line) is complete in itself.

## Common Mistakes (Beginners' Errors)

1. Forgetting to use quotes: `print(Hello World)` ❌ — will cause an error.
2. Not closing the bracket: `print("Hello World"` ❌ — will cause an error.
3. Writing a capital `P`: `Print("Hello")` ❌ — in Python, it is always lowercase `print`.

## Practice Questions (For You)

Try these yourself and send me the answers; I will check them:

1. Write a Python program that prints your **name**.
print("Rohit Kumar")

2. Write a Python program that prints "I", "Love", and "Python" on 3 separate lines (using three separate `print()` statements).
print("I")
print("Love")
print("python")

3. State which of these code snippets is correct and which is incorrect, and why:
- `print("Namaste")`
- `print(Namaste)`
- `Print("Namaste")`
print("Namaste") ✅ Correct
print(Namaste) ❌ Incorrect - missing quotes
Print("Namaste") ❌ Incorrect - capital P; Python is case-sensitive

4. **Exam/Interview-style question:** What is the function of `print()`? Explain in your own words.
The function of print() is to display code on the screen.

## Mini Quiz (Quick Test)

Answer in one line:
- Q1. Python is a _______ language used to give instructions to a computer.
programming

- Q2. What is text data called in Python?
string

- Q3. Is Python case-sensitive? (Yes/No)
yes
'''