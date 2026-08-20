# Python Comments (Single & Multi-line) — Complete Notes

## 1. What is a Comment?

A **comment** is a piece of text in your code that the Python interpreter **ignores** during execution. Comments are meant for **humans** — to explain what the code does, why a certain approach was used, or to temporarily disable a line of code.

**Why use comments?**
- Improve **readability** for yourself and others.
- Document the **purpose** of code sections.
- **Disable/skip** code temporarily during debugging/testing.
- Help others (or future you) understand the logic quickly.

---

## 2. Single-Line Comments

In Python, a single-line comment starts with a **hash symbol `#`**. Everything after `#` on that line is ignored by the interpreter.

```python
# This is a single-line comment
print("Hello, World!")   # This comment is after code on the same line
```

**Explanation:** 
- The first line is a full-line comment — nothing on it is executed.
- The second line shows an **inline comment** — the code `print("Hello, World!")` still runs, but everything after `#` (` This comment is after code on the same line`) is ignored.

---

## 3. Multi-Line Comments

Python does **not** have a dedicated syntax for multi-line comments like some other languages (e.g., `/* ... */` in C/Java). There are two common approaches:

### Method 1: Multiple `#` symbols (the "official" way)
```python
# This is line one of the comment
# This is line two of the comment
# This is line three of the comment
print("Multi-line comment example")
```

**Explanation:** Each line individually starts with `#`. This is the **recommended** way according to PEP 8 (Python's style guide) for actual comments.

### Method 2: Triple-quoted strings (often misused as comments)
```python
"""
This is technically a multi-line string,
not a true comment, but since it's not assigned
to a variable, it has no effect on execution
and behaves like a comment when not used as a docstring.
"""
print("Hello!")
```

**Explanation:** Triple quotes (`'''...'''` or `"""..."""`) create a string. If this string isn't assigned to a variable and isn't the first statement in a function/class/module (where it would become a **docstring**), Python evaluates it and discards it — effectively acting like a comment. However, technically it IS a string object created in memory, so it's not a "true" comment — it's more of a workaround.

---

## 4. Docstrings vs Comments (Important Distinction)

A **docstring** is a special triple-quoted string placed as the **first statement** inside a module, function, class, or method. Unlike comments, docstrings are **stored** and can be accessed using `.__doc__` or the `help()` function.

```python
def add(a, b):
    """
    This function adds two numbers and returns the result.
    Parameters: a, b (numbers)
    Returns: sum of a and b
    """
    return a + b

print(add.__doc__)
```

**Explanation:** Unlike a regular comment, this docstring can be retrieved at runtime via `add.__doc__`, and tools/IDEs use it to show documentation/help. Comments (`#`) are stripped and never accessible at runtime.

---

## 5. Best Practices for Comments

- Keep comments **clear and concise** — explain "why", not just "what" (the code already shows "what").
- Avoid **redundant** comments that just restate the obvious code.
- Update comments when you update the code (outdated comments are misleading).
- Use comments to mark **TODOs**:
  ```python
  # TODO: Add error handling for invalid input
  ```
- Don't overuse comments — well-named variables/functions often reduce the need for comments.

---

## Examples with Solutions & Explanations

### Example 1: Basic single-line comment
**Problem:** Write a program that calculates the sum of two numbers, with comments explaining each step.

```python
# Define two numbers
a = 10
b = 20

# Calculate their sum
total = a + b

# Print the result
print("Total:", total)
```

**Output:**
```
Total: 30
```

**Explanation:** Each comment explains the purpose of the line(s) below it. Notice comments don't affect execution — the program runs exactly as if the comments weren't there.

---

### Example 2: Inline comment usage
**Problem:** Use inline comments to explain a formula.

```python
radius = 7
area = 3.14159 * radius ** 2  # Formula: pi * r^2
print(area)
```

**Output:**
```
153.93791
```

**Explanation:** The inline comment `# Formula: pi * r^2` clarifies the math being performed, placed right after the relevant code on the same line, separated by at least one space before `#` for readability (PEP 8 recommends 2 spaces).

---

### Example 3: Multi-line comment using `#` on each line
**Problem:** Explain a block of code that checks if a number is even or odd, using proper multi-line comments.

```python
# This program checks whether a number is even or odd.
# It uses the modulus operator (%) to find the remainder
# when dividing by 2. If remainder is 0, the number is even.

num = 15
if num % 2 == 0:
    print("Even")
else:
    print("Odd")
```

**Output:**
```
Odd
```

**Explanation:** Three separate `#` lines together form a "multi-line comment block" explaining the whole program's logic before the code begins.

---

### Example 4: Using triple-quoted string as a comment (and showing it's NOT truly ignored)
**Problem:** Demonstrate the difference between a real comment and a triple-quoted string comment.

```python
"""
This block explains that we are testing string vs comment behavior.
"""
x = 5
# print(x)  <- this line is commented out and won't run
print("x is:", x)
```

**Output:**
```
x is: 5
```

**Explanation:** The triple-quoted string at the top is created as a string object but not used, so it has no visible effect — similar to a comment. The line `# print(x)` is a true comment; that print statement never executes at all.

---

### Example 5: Docstring vs comment
**Problem:** Write a function with both a docstring and internal comments, then access the docstring.

```python
def square(n):
    """Returns the square of a given number n."""
    # Multiply n by itself
    return n * n

print(square(6))
print(square.__doc__)
```

**Output:**
```
36
Returns the square of a given number n.
```

**Explanation:** `square.__doc__` retrieves the docstring text because it's stored as metadata on the function object. The `# Multiply n by itself` comment, however, is discarded during parsing — you can't retrieve it programmatically.

---

## Extra Practice Questions

1. Write a program with at least 3 single-line comments explaining each step of calculating the area of a rectangle.
2. Convert the following into a properly commented version using multiple `#` lines:
   ```python
   x = 10
   y = 20
   print(x + y)
   ```
3. Write a function `divide(a, b)` that includes a docstring explaining what it does, and print its `__doc__`.
4. Create a small program where you use an inline comment to explain a tricky line of code (e.g., a list comprehension).
5. Demonstrate the difference between a comment (`#`) and a docstring by writing a function `greet()` that has both, then try to access each — explain in your own comment why one is accessible at runtime and the other isn't.
6. Write a program to calculate simple interest, and comment out (disable) the line that prints intermediate steps, leaving only the final result printed.
7. Use a triple-quoted string as a temporary "block comment" to disable 4 lines of code at once, and verify the program still runs correctly.
8. Explain in a comment why the following is considered a "bad" comment, then rewrite it as a "good" comment:
   ```python
   x = x + 1  # increment x by 1
   ```
9. Write a `# TODO` comment in a function that currently only has a `pass` statement, describing what needs to be implemented.
10. Create a class `Student` with a class-level docstring and a method with its own docstring. Print both docstrings using `.__doc__`.

---

*Type the next topic name, or type **stop** to end.*
