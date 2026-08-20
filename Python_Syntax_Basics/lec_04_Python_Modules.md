# Python Modules — Complete Notes

## 1. What is a Module?

A **module** is simply a file containing Python code (variables, functions, classes, or executable statements) that ends with a `.py` extension. Modules let you logically organize your code into separate files instead of writing everything in one giant script.

**Why use modules?**
- **Reusability** – Write code once, use it in many programs.
- **Organization** – Break a large program into smaller, manageable files.
- **Namespace management** – Avoid naming conflicts between different parts of a program.
- **Maintainability** – Easier to debug and update smaller files.

---

## 2. Types of Modules

1. **Built-in modules** – Come pre-installed with Python (e.g., `math`, `os`, `sys`, `random`, `datetime`).
2. **User-defined modules** – Created by you (any `.py` file you write).
3. **Third-party modules** – Installed via `pip` (e.g., `numpy`, `pandas`, `requests`).

---

## 3. Importing a Module

There are several ways to import a module:

```python
import math                  # import the whole module
import math as m             # import with an alias
from math import sqrt        # import a specific function
from math import sqrt, pi    # import multiple specific items
from math import *           # import everything (not recommended)
```

**Explanation:**
- `import math` → You must use `math.sqrt()` to access functions.
- `import math as m` → Shortens the name; use `m.sqrt()`.
- `from math import sqrt` → You can call `sqrt()` directly without the `math.` prefix.
- `from math import *` → Imports all names into the current namespace. This is discouraged because it can cause naming conflicts and makes it unclear where a function came from.

---

## 4. Creating Your Own Module

Any `.py` file can act as a module. Suppose you create a file named `calculator.py`:

```python
# calculator.py
def add(a, b):
    return a + b

def subtract(a, b):
    return a - b

pi_value = 3.14159
```

Now in another file (in the same directory), you can import and use it:

```python
# main.py
import calculator

print(calculator.add(5, 3))       # Output: 8
print(calculator.subtract(5, 3))  # Output: 2
print(calculator.pi_value)        # Output: 3.14159
```

**Explanation:** Python looks for `calculator.py` in the current directory (and other paths listed in `sys.path`), loads it, and makes its functions/variables accessible through the `calculator` namespace.

---

## 5. The `dir()` Function

`dir()` lists all the names (functions, variables, classes) defined in a module.

```python
import math
print(dir(math))
```

**Explanation:** This is useful to explore what a module offers without checking documentation.

---

## 6. The `__name__` Variable

Every Python file has a built-in variable `__name__`. When a file is run directly, `__name__` equals `"__main__"`. When it's imported as a module, `__name__` equals the module's filename (without `.py`).

```python
# calculator.py
def add(a, b):
    return a + b

if __name__ == "__main__":
    print("Running directly:", add(2, 3))
```

- Running `python calculator.py` → prints `Running directly: 5`
- Importing it (`import calculator`) → the `if` block does NOT execute.

**Explanation:** This pattern lets a file be used both as a standalone script and as a reusable module, since test/demo code only runs when the file is executed directly.

---

## 7. Commonly Used Built-in Modules

| Module | Purpose |
|---|---|
| `math` | Mathematical functions (sqrt, pow, floor, etc.) |
| `random` | Generate random numbers |
| `datetime` | Work with dates and times |
| `os` | Interact with the operating system (files, directories) |
| `sys` | Access system-specific parameters and functions |
| `json` | Work with JSON data |
| `re` | Regular expressions |

---

## 8. Package vs Module

- A **module** is a single `.py` file.
- A **package** is a collection of modules organized in a directory that contains an `__init__.py` file (this marks the directory as a package).

```
mypackage/
    __init__.py
    module1.py
    module2.py
```

```python
from mypackage import module1
```

---

## 9. `pip` — Installing Third-Party Modules

```bash
pip install requests
```

Then use it:

```python
import requests
response = requests.get("https://example.com")
print(response.status_code)
```

---

## Examples with Solutions & Explanations

### Example 1: Using the `math` module
**Problem:** Write a program to calculate the area of a circle using the `math` module.

```python
import math

radius = 5
area = math.pi * math.pow(radius, 2)
print(f"Area of the circle: {area:.2f}")
```

**Output:**
```
Area of the circle: 78.54
```

**Explanation:** `math.pi` gives the accurate value of π, and `math.pow(radius, 2)` calculates radius². We import the `math` module because Python doesn't have π or power functions built into the base language — they live in this module.

---

### Example 2: Using the `random` module
**Problem:** Simulate rolling a six-sided die.

```python
import random

dice_roll = random.randint(1, 6)
print(f"You rolled a {dice_roll}")
```

**Explanation:** `random.randint(1, 6)` returns a random integer between 1 and 6 (inclusive on both ends). Each run may give a different result since it's random.

---

### Example 3: Creating and importing a custom module
**Problem:** Create a module `greetings.py` with a function `greet(name)` that returns a greeting message, then use it in another file.

`greetings.py`:
```python
def greet(name):
    return f"Hello, {name}! Welcome to Python."
```

`main.py`:
```python
import greetings

message = greetings.greet("Riya")
print(message)
```

**Output:**
```
Hello, Riya! Welcome to Python.
```

**Explanation:** We separated the greeting logic into its own file (`greetings.py`). The `main.py` file imports it and calls the function using `module_name.function_name()` syntax. This demonstrates reusability — `greetings.py` could be imported into many other programs.

---

### Example 4: Using `from ... import` with alias
**Problem:** Import only the `sqrt` function from `math` and use an alias.

```python
from math import sqrt as square_root

result = square_root(64)
print(result)
```

**Output:**
```
8.0
```

**Explanation:** `sqrt as square_root` renames the imported function locally. Now we call it directly as `square_root()` without needing the `math.` prefix, and without importing the entire module.

---

### Example 5: Using `__name__ == "__main__"`
**Problem:** Create a module `mathops.py` that has a `multiply()` function and test code that only runs when executed directly.

```python
# mathops.py
def multiply(a, b):
    return a * b

if __name__ == "__main__":
    print("Test:", multiply(4, 5))
```

- Run directly: `python mathops.py` → Output: `Test: 20`
- Imported elsewhere: `import mathops` → No output, only the function becomes available.

**Explanation:** This is a best practice for module design—it separates "library code" (reusable functions) from "script code" (code meant only for testing/demo purposes).

---

## Extra Practice Questions

1. Write a program that imports the `datetime` module and prints today's date.
2. Create a custom module named `stringutils.py` containing a function `reverse_string(s)` that returns the reversed version of a string. Import and use it in another file.
3. Use the `random` module to generate a list of 5 random numbers between 1 and 100.
4. Write a program using the `os` module to print the current working directory.
5. Create a module `shapes.py` with functions to calculate the area of a rectangle and a triangle. Import only the rectangle function using `from shapes import ...`.
6. Explain (in comments) the difference between `import module` and `from module import *`, then demonstrate both with the `math` module.
7. Use `dir()` on the `random` module and list any 5 functions you find interesting.
8. Create two modules, `module_a.py` and `module_b.py`, where `module_b.py` imports and uses a function from `module_a.py`.
9. Write a script that uses `if __name__ == "__main__":` to only run a test print statement when the file is executed directly, not when imported.
10. Install a third-party module of your choice using `pip` (e.g., `requests` or `colorama`) and write a small program demonstrating its use.

---

*Type the next topic name, or type **stop** to end.*
