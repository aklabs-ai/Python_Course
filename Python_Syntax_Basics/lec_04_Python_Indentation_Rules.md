# Python Indentation Rules — Complete Notes

## 1. What is Indentation?

**Indentation** refers to the spaces or tabs at the beginning of a line of code. In most programming languages (like C, Java, C++), indentation is just for readability and has no effect on how the code runs — code blocks are defined using curly braces `{}`.

**Python is different.** Python uses **indentation** itself to define **blocks of code** (instead of curly braces or keywords like `begin`/`end`). This makes indentation **mandatory and syntactically significant** — incorrect indentation will cause errors or change your program's logic.

---

## 2. Why Does Python Use Indentation?

- It forces clean, readable code (no more debates about brace placement).
- It removes the need for extra symbols (`{`, `}`, `;`), making code visually simpler.
- It was a deliberate design choice by Python's creator, Guido van Rossum, to enforce consistent formatting across all Python code.

---

## 3. Basic Rules of Indentation

1. **A colon `:`** at the end of a line (after `if`, `for`, `while`, `def`, `class`, `try`, `else`, `elif`, `with`, etc.) signals that an indented block follows.
2. All statements within the same block **must be indented at the same level**.
3. Indentation is typically **4 spaces** per level (PEP 8 recommendation — Python's official style guide).
4. You **cannot mix tabs and spaces** in the same block — this raises a `TabError` in Python 3.
5. Reducing (dedenting) the indentation level ends the current block and returns to the previous block level.
6. Inconsistent indentation within the same block raises an `IndentationError`.

---

## 4. Example of Correct Indentation

```python
def greet(name):
    if name == "":
        print("Hello, stranger!")
    else:
        print(f"Hello, {name}!")
    print("Have a nice day!")

greet("Aarav")
```

**Explanation:**
- `if name == "":` block is indented once (4 spaces) inside `greet()`.
- `else:` block is at the same indentation level as `if`, but its own body is indented one level deeper.
- `print("Have a nice day!")` is back at the function's indentation level (not inside `if`/`else`), so it always executes regardless of the condition.

**Output:**
```
Hello, Aarav!
Have a nice day!
```

---

## 5. Example of Incorrect Indentation (Errors)

```python
def greet(name):
    if name == "":
    print("Hello, stranger!")   # ERROR: expected an indented block
```

**Explanation:** After `if name == "":`, Python expects the next line to be indented (to form the `if` block). Since `print(...)` is at the same level as `if`, Python raises:
```
IndentationError: expected an indented block after 'if' statement
```

Another example — inconsistent indentation:
```python
def show():
    print("Line 1")
      print("Line 2")   # ERROR: unexpected indent
```

**Explanation:** `print("Line 2")` has more indentation than `print("Line 1")` without any block-opening statement (like `if`, `for`) before it, so Python doesn't know why it's indented further. This raises:
```
IndentationError: unexpected indent
```

---

## 6. Nested Indentation

Blocks can be nested inside other blocks, with each level indented further.

```python
for i in range(3):
    print("Outer loop:", i)
    for j in range(2):
        print("  Inner loop:", j)
```

**Output:**
```
Outer loop: 0
  Inner loop: 0
  Inner loop: 1
Outer loop: 1
  Inner loop: 0
  Inner loop: 1
Outer loop: 2
  Inner loop: 0
  Inner loop: 1
```

**Explanation:** The outer `for` loop body is indented once (4 spaces). The inner `for` loop, being inside the outer loop's body, is also indented once relative to it — so its own body is indented twice (8 spaces) relative to the `for i` line.

---

## 7. Tabs vs Spaces

Python 3 does **not allow mixing tabs and spaces** for indentation within the same block — doing so raises a `TabError`.

```python
def func():
    print("Using spaces")
	print("Using a tab")   # TabError: inconsistent use of tabs and spaces
```

**Explanation:** Even though both lines might "look" aligned in some editors, Python detects the mixed whitespace characters and refuses to run, since it can't reliably determine indentation level. **Best practice: always use 4 spaces per indentation level, and configure your editor to convert tabs to spaces automatically.**

---

## 8. Indentation with Single-Line Blocks

For very simple, single-statement blocks, Python allows writing the statement on the same line as the colon (though PEP 8 discourages this for readability):

```python
if True: print("This works but is not recommended")
```

**Explanation:** This is valid syntax, but it reduces readability and doesn't scale well for multi-statement blocks. Best practice is to always use proper indentation on a new line.

---

## 9. Empty Blocks — the `pass` Statement

If you want a block to do nothing (e.g., a placeholder for future code), you cannot leave it truly empty — Python requires **something** in an indented block. Use `pass`:

```python
def future_function():
    pass   # TODO: implement later

if True:
    pass
else:
    print("This won't run")
```

**Explanation:** `pass` is a null operation — it does nothing, but it satisfies Python's requirement that every block have at least one statement, preventing an `IndentationError`.

---

## Examples with Solutions & Explanations

### Example 1: Correct if-elif-else indentation
**Problem:** Write a program to check if a number is positive, negative, or zero.

```python
num = -5

if num > 0:
    print("Positive number")
elif num < 0:
    print("Negative number")
else:
    print("Zero")
```

**Output:**
```
Negative number
```

**Explanation:** `if`, `elif`, and `else` are all at the same indentation level (they belong to the same conditional structure), while their respective print statements are indented one level deeper, marking them as the body of each branch.

---

### Example 2: Nested if inside a for loop
**Problem:** Print only even numbers from 1 to 10 using a `for` loop and nested `if`.

```python
for num in range(1, 11):
    if num % 2 == 0:
        print(num, "is even")
```

**Output:**
```
2 is even
4 is even
6 is even
8 is even
10 is even
```

**Explanation:** The `if` statement is indented inside the `for` loop's block. The `print()` statement is indented one level further, inside the `if` block. This nested structure means: for each number, check the condition, and only print if true.

---

### Example 3: Function with multiple indentation levels
**Problem:** Write a function that classifies a student's grade based on marks, using nested conditionals.

```python
def grade(marks):
    if marks >= 90:
        result = "A"
    else:
        if marks >= 75:
            result = "B"
        else:
            result = "C"
    return result

print(grade(95))
print(grade(80))
print(grade(60))
```

**Output:**
```
A
B
C
```

**Explanation:** Notice three levels of indentation: the function body (level 1), the `if`/`else` block (level 1, since directly inside function), and the nested `if`/`else` inside `else` (level 2). Each level of nesting adds one more indentation step (commonly 4 more spaces).

---

### Example 4: Fixing an IndentationError
**Problem:** The following code has an indentation error. Identify and fix it.

**Broken code:**
```python
def check(x):
    if x > 0:
        print("Positive")
      print("Checked")   # inconsistent indentation
```

**Fixed code:**
```python
def check(x):
    if x > 0:
        print("Positive")
    print("Checked")
```

**Explanation:** In the broken version, `print("Checked")` had 6 spaces (a level between the `if` block's 8 spaces and the function's 4 spaces), which doesn't match any valid block level — causing an `IndentationError`. In the fix, it's aligned with `if x > 0:` (4 spaces), meaning it runs after the `if` block completes, regardless of whether `x > 0` was true.

---

### Example 5: Using `pass` for an empty block
**Problem:** Write a function stub for a feature you haven't implemented yet, ensuring the code still runs without errors.

```python
def calculate_tax(income):
    pass   # TODO: implement tax calculation logic

def calculate_discount(price):
    if price > 1000:
        pass   # TODO: add discount logic for expensive items
    else:
        print("No discount available")

calculate_tax(50000)
calculate_discount(500)
```

**Output:**
```
No discount available
```

**Explanation:** `calculate_tax()` runs without error even though it does nothing, thanks to `pass`. Similarly, the `if price > 1000:` branch does nothing (via `pass`) when true, but the `else` branch still executes normally when the condition is false.

---

## Extra Practice Questions

1. Write a program using a `for` loop and an `if-else` block to print "Even" or "Odd" for numbers 1 to 5, ensuring correct indentation.
2. Identify and fix the indentation error in the following code:
   ```python
   def greet():
   print("Hello!")
   ```
3. Write a function with three levels of nested `if` statements (e.g., checking age category: child, teen, adult, senior) and use correct indentation throughout.
4. Create a `while` loop with a nested `if` block that prints numbers from 1 to 10 but stops (using `break`) when it reaches 7.
5. Write a program with a `try-except` block, ensuring the `except` body is properly indented.
6. Explain (in your own words, as a comment) why the following code raises an `IndentationError`:
   ```python
   for i in range(5):
   print(i)
   ```
7. Write a function `check_password(pwd)` that uses nested `if` blocks to check length (`>= 8`), presence of a digit, and presence of an uppercase letter — with proper indentation for each condition.
8. Create a class `Animal` with two methods (`eat` and `sleep`), ensuring correct indentation for the class body and each method body.
9. Rewrite the following single-line `if` into a properly indented multi-line block:
   ```python
   if 5 > 3: print("Five is greater")
   ```
10. Write a nested loop (`for` inside `for`) that prints a small multiplication table (1 to 3), paying close attention to indentation for the inner vs outer loop.

---

*Type the next topic name, or type **stop** to end.*
