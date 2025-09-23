# Python-basics
A collection of my practice and insights gained throughout the course: python-programming-a-step-by-step-programming-course(Udemy)

About Python:
- Simple & Readable: Known for its clean, English-like syntax that is easy to learn and read.

- Interpreted: Code is executed line-by-line, which makes debugging easier.

- High-Level: You don't manage memory manually; it handles complex tasks behind the scenes.

- Dynamically Typed: You don't need to declare a variable's type (e.g., x = 5 instead of int x = 5).

Python Applications:
- Python is used in game development (e.g., Pygame for 2D games), desktop GUI applications (using Tkinter, PyQt, wxPython), and networking/cybersecurity (network automation, penetration testing, forensic analysis).

Remeber:
- What are f-strings?
  
f-strings (formatted string literals) were introduced in Python 3.6.

You prefix a string with f or F, and then you can embed variables or expressions inside {} directly.

    - Readable & clean – You don’t need to break strings or call str() manually.
  
      print(f"Hello {name}, you are {age} years old.")
  
  
    - Supports expressions inside {} – Not just variables, you can do calculations too.
  
      print(f"Area of rectangle: {length * breadth}")
  
      Output:
      Area of rectangle: 200
  
  
    - Formatting options – You can control how values look (decimal places, alignment, etc.):
      pi = 3.14159
      print(f"Pi rounded to 2 decimals: {pi:.2f}")
  
      Output:
  
      Pi rounded to 2 decimals: 3.14
  
  
    - Faster than str.format() – because it’s evaluated at runtime and optimized.



- Using , inside print()

The comma separates multiple arguments in print().

It automatically adds a space between them.

Works with different data types (string, int, float, etc.) without needing conversion.

    name = "Tanushree"
    age = 22
    print("My name is", name, "and I am", age, "years old")


Output: My name is Tanushree and I am 22 years old


- Using + inside print()

+ is string concatenation, so both sides must be strings.


-If you want to join a string with a number, you must explicitly convert the number using str().

    name = "Tanushree"
    age = 22
    print("My name is " + name + " and I am " + str(age) + " years old")

output: My name is Tanushree and I am 22 years old

- In Python, input() always returns a string, no matter what you type. You convert it to suitable data type. Eg:
number = input("Enter a number: ")   
number = int(number)

Then you can perform operations



