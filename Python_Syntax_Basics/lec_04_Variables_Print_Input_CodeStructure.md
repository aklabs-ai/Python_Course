# Python: Variables & Naming Conventions, Print Statements & Output, Input from Users, Basic Code Structure — Complete Notes

---

# PART 1: Variables & Naming Conventions

## 1. What is a Variable?

A **variable** is a named location in memory used to store a value. In Python, you don't need to declare a variable's type explicitly — Python figures it out automatically based on the value assigned (this is called **dynamic typing**).

```python
x = 10
name = "Alice"
price = 99.99
is_active = True
```

**Explanation:** Each variable is created the moment you assign a value to it using `=`. Python automatically determines the type: `x` becomes an `int`, `name` a `str`, `price` a `float`, and `is_active` a `bool`. There's no need to write something like `int x = 10;` as you would in Java/C++.

---

## 2. Rules for Naming Variables (Mandatory)

1. Must start with a **letter** (a-z, A-Z) or an **underscore** `_` — not a digit.
2. Can only contain **letters, digits, and underscores** (no spaces, no special characters like `@`, `-`, `%`).
3. **Case-sensitive** — `age`, `Age`, and `AGE` are three different variables.
4. Cannot be a Python **reserved keyword** (e.g., `if`, `for`, `class`, `True`, `None`).

```python
valid_name = "OK"       # valid
_valid = "OK"            # valid (starts with underscore)
name2 = "OK"              # valid (digit not at start)

2name = "Invalid"        # INVALID - starts with a digit -> SyntaxError
my-name = "Invalid"      # INVALID - hyphen not allowed -> SyntaxError
class = "Invalid"        # INVALID - 'class' is a reserved keyword -> SyntaxError
```

**Explanation:** Python's parser strictly enforces these identifier rules. Breaking rule 1 or 2 causes a `SyntaxError` immediately; using a reserved keyword as a variable name also causes a `SyntaxError` since the interpreter expects that word to have special meaning.

---

## 3. Naming Convention Best Practices (PEP 8 Style Guide)

| Convention | Used for | Example |
|---|---|---|
| `smale_case` | Variables and function names | `total_price`, `user_age` |
| `UPPER_CASE` | Constants (values that shouldn't change) | `MAX_LIMIT = 100` |
| `PascalCase` | Class names | `class StudentRecord:` |
| `_leading_underscore` | "Internal use" convention (weak privacy signal) | `_internal_value` |
| `__double_leading_underscore` | Name-mangling in classes (stronger privacy signal) | `__secret` |

**Explanation:** These aren't enforced by Python itself (except reserved keyword restrictions) — they are **community conventions** (from PEP 8) that make code consistent and readable across projects.

### Good vs Bad Naming
```python
# Good - descriptive and follows snake_case
total_marks = 450
student_name = "Riya"

# Bad - unclear, single letters (except for loop counters/short scopes), inconsistent casing
tm = 450
StudentName = "Riya"   # PascalCase should be reserved for classes, not variables
```

---

## 4. Multiple Assignment

```python
a, b, c = 1, 2, 3          # assign different values in one line
x = y = z = 0               # assign the same value to multiple variables
```

**Explanation:** The first line unpacks values positionally — `a` gets `1`, `b` gets `2`, `c` gets `3`. The second line chains assignment — all three variables (`x`, `y`, `z`) point to the same value `0`.

---

# PART 2: Print Statements & Output

## 1. The `print()` Function

`print()` is used to display output to the console/terminal.

```python
print("Hello, World!")
print(42)
print(3.14)
print(True)
```

**Explanation:** `print()` can take any data type and automatically converts it to a readable string representation for display.

---

## 2. Printing Multiple Values

```python
name = "Aarav"
age = 21
print("Name:", name, "Age:", age)
```

**Output:**
```
Name: Aarav Age: 21
```

**Explanation:** Multiple arguments passed to `print()`, separated by commas, are automatically joined with a **single space** by default.

---

## 3. `sep` and `end` Parameters

```python
print("A", "B", "C", sep="-")          # custom separator
print("Hello", end=" ")                 # custom ending (default is newline "\n")
print("World")
```

**Output:**
```
A-B-C
Hello World
```

**Explanation:** `sep` changes what's placed **between** multiple arguments (default is a space). `end` changes what's placed **after** the entire print statement (default is a newline `\n`) — here it's a space instead, so the next `print()` continues on the same line.

---

## 4. f-strings (Formatted String Literals) — Modern & Recommended

```python
name = "Meera"
score = 95.5
print(f"{name} scored {score} marks.")
```

**Output:**
```
Meera scored 95.5 marks.
```

**Explanation:** Prefixing a string with `f` allows embedding variables/expressions directly inside `{}` — cleaner and faster than older methods like `%` formatting or `.format()`.

### Other formatting methods (for comparison)
```python
print("{} scored {} marks.".format(name, score))     # .format() method
print("%s scored %.1f marks." % (name, score))         # % formatting (older style)
```

---

# PART 3: Input from Users

## 1. The `input()` Function

`input()` pauses the program and waits for the user to type something, then returns it **as a string**.

```python
name = input("Enter your name: ")
print("Hello,", name)
```

**Explanation:** Whatever the user types (before pressing Enter) is captured and stored in the `name` variable. The prompt text `"Enter your name: "` is displayed to guide the user.

---

## 2. Important: `input()` Always Returns a String

```python
age = input("Enter your age: ")
print(type(age))   # <class 'str'>, even if user types "25"
```

**Explanation:** Even if the user enters a number, Python stores it as text (`str`). To use it as a number, you must **convert (typecast)** it explicitly.

```python
age = int(input("Enter your age: "))    # convert to integer
height = float(input("Enter your height: "))  # convert to float
```

**Explanation:** `int()` and `float()` convert the string input into numeric types so you can perform mathematical operations on it. If the user types something non-numeric (like "abc") when `int()` is expected, Python raises a `ValueError`.

---

## 3. Taking Multiple Inputs

```python
x, y = input("Enter two numbers separated by space: ").split()
print(int(x) + int(y))
```

**Explanation:** `.split()` breaks the input string into a list based on whitespace (by default). Unpacking assigns each piece to `x` and `y`, which are then converted to integers before adding.

---

# PART 4: Basic Code Structure

## 1. A Typical Python Script Structure

```python
# 1. Import statements (if needed)
import math

# 2. Constants / global variables
PI = 3.14159

# 3. Function definitions
def calculate_area(radius):
    return PI * radius ** 2

# 4. Main logic / execution
if __name__ == "__main__":
    r = float(input("Enter radius: "))
    area = calculate_area(r)
    print(f"Area: {area:.2f}")
```

**Explanation:** This is a common, organized structure:
1. **Imports** at the top bring in needed modules.
2. **Constants/global variables** are defined early (often in `UPPER_CASE`).
3. **Functions** encapsulate reusable logic.
4. The `if __name__ == "__main__":` block contains the code that runs when the script is executed directly — separating "library code" from "script/execution code".

---

## 2. Statements Execute Top to Bottom

Python executes code **sequentially**, line by line, from top to bottom (unless control flow like loops, conditionals, or function calls redirect execution).

```python
print("Step 1")
print("Step 2")
print("Step 3")
```

**Output:**
```
Step 1
Step 2
Step 3
```

**Explanation:** There's no ambiguity — Python runs each line in the order it's written, which is why the order you write statements matters.

---

## Examples with Solutions & Explanations

### Example 1: Variables with proper naming
**Problem:** Store a student's name, age, and GPA using appropriately named variables, and print them.

```python
student_name = "Kabir"
student_age = 20
student_gpa = 8.7

print("Student Name:", student_name)
print("Age:", student_age)
print("GPA:", student_gpa)
```

**Output:**
```
Student Name: Kabir
Age: 20
GPA: 8.7
```

**Explanation:** Each variable uses `snake_case` and is descriptively named (`student_name` instead of just `n`), making the code self-explanatory — a core naming best practice.

---

### Example 2: Using `sep` and `end` in `print()`
**Problem:** Print a date in `DD-MM-YYYY` format using `sep`, and print two messages on the same line using `end`.

```python
day, month, year = 15, 8, 2026
print(day, month, year, sep="-")

print("Loading", end="...")
print("Done!")
```

**Output:**
```
15-8-2026
Loading...Done!
```

**Explanation:** `sep="-"` joins the three numbers with hyphens instead of spaces. `end="..."` replaces the default newline after "Loading", so "Done!" appears right after it on the same line.

---

### Example 3: Taking user input and performing a calculation
**Problem:** Ask the user for two numbers and print their sum.

```python
num1 = int(input("Enter first number: "))
num2 = int(input("Enter second number: "))
total = num1 + num2
print(f"The sum is: {total}")
```

**Sample interaction:**
```
Enter first number: 10
Enter second number: 15
The sum is: 25
```

**Explanation:** Both inputs are converted from string to `int` using `int()` before adding — if we skipped this conversion, `num1 + num2` would perform **string concatenation** instead (e.g., `"10" + "15"` → `"1015"`), which is a very common beginner mistake.

---

### Example 4: f-strings for clean output formatting
**Problem:** Ask the user for their name and favorite number, then greet them and show the number squared, using f-strings.

```python
name = input("What's your name? ")
number = int(input("Give me your favorite number: "))

print(f"Hi {name}! The square of {number} is {number ** 2}.")
```

**Sample interaction:**
```
What's your name? Zara
Give me your favorite number: 7
Hi Zara! The square of 7 is 49.
```

**Explanation:** The f-string embeds the `name` variable and even a full **expression** (`number ** 2`) directly inside `{}` — Python evaluates the expression and inserts the result into the string automatically.

---

### Example 5: Organized basic code structure
**Problem:** Write a small, well-structured script that calculates simple interest, following the standard structure (imports, constants, functions, main block).

```python
# Constants
RATE_DEFAULT = 5  # default interest rate in %

# Function definition
def simple_interest(principal, rate, time):
    return (principal * rate * time) / 100

# Main logic
if __name__ == "__main__":
    p = float(input("Enter principal amount: "))
    t = float(input("Enter time (years): "))
    interest = simple_interest(p, RATE_DEFAULT, t)
    print(f"Simple Interest: {interest:.2f}")
```

**Sample interaction:**
```
Enter principal amount: 1000
Enter time (years): 2
Simple Interest: 100.00
```

**Explanation:** The constant `RATE_DEFAULT` is declared in `UPPER_CASE` at the top. The reusable logic lives inside `simple_interest()`. The `if __name__ == "__main__":` block handles user interaction — keeping the calculation function reusable/importable separately from the input/output logic.

---

## Extra Practice Questions

1. Create 5 variables (name, age, city, is_student, height) with proper `snake_case` naming and print all of them using a single `print()` statement with a custom `sep`.
2. Identify which of these variable names are invalid and explain why: `2cool`, `my-var`, `_hidden`, `class`, `totalAmount`.
3. Write a program that takes a user's name and age as input, then prints: `"<name> will turn 30 in <30-age> years"` (perform the subtraction, converting age to int first).
4. Use `f-strings` to print a formatted receipt showing an item name, quantity, and total price (quantity × price) from 3 separate inputs.
5. Write a program using `end=""` in multiple `print()` calls to build a small ASCII shape (e.g., a triangle of stars) on the same or controlled lines.
6. Take two numbers as input on the same line (space-separated), split and convert them, then print their product.
7. Rewrite the following using proper naming conventions (currently using bad names):
   ```python
   a = "John"
   b = 45000
   C = True
   ```
8. Write a small structured script (imports if needed, constants, a function, and a `if __name__ == "__main__":` block) that converts a user-input temperature from Celsius to Fahrenheit.
9. Explain, in a comment, why `input()` always returns a string, and demonstrate with code what happens if you try to add two un-converted inputs.
10. Create constants for `TAX_RATE` and `DISCOUNT_RATE` in `UPPER_CASE`, then write a function that calculates a final price using both, taking the original price as input from the user.

---

*Type the next topic name, or type **stop** to end.*
