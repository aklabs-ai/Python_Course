# Python Data Types — Complete Notes

## 1. What is a Data Type?

A **data type** defines the kind of value a variable holds and what operations can be performed on it. Python is **dynamically typed**, meaning you don't declare a type explicitly — the interpreter determines it automatically based on the assigned value. You can check any variable's type using the built-in `type()` function.

```python
x = 10
print(type(x))   # <class 'int'>
```

---

## 2. Categories of Python Data Types

Python's built-in data types can be grouped as follows:

| Category | Types |
|---|---|
| **Numeric** | `int`, `float`, `complex` |
| **Sequence** | `str`, `list`, `tuple`, `range` |
| **Mapping** | `dict` |
| **Set** | `set`, `frozenset` |
| **Boolean** | `bool` |
| **Binary** | `bytes`, `bytearray`, `memoryview` |
| **None type** | `NoneType` |

---

## 3. Numeric Types

### `int` (Integer)
Whole numbers, positive or negative, with no size limit (Python automatically handles arbitrarily large integers).
```python
a = 10
b = -25
c = 1_000_000    # underscores allowed for readability
```

### `float` (Floating Point)
Numbers with a decimal point, used for real numbers.
```python
pi = 3.14159
temperature = -12.5
```

### `complex` (Complex Numbers)
Numbers with a real and imaginary part, written as `a + bj`.
```python
z = 3 + 4j
print(z.real, z.imag)   # 3.0 4.0
```

**Explanation:** `int` has unlimited precision (unlike languages like Java, where integers overflow at fixed sizes). `float` uses double-precision (64-bit) representation, which can sometimes introduce small rounding errors (e.g., `0.1 + 0.2` ≈ `0.30000000000000004`). `complex` is rarely used except in scientific/engineering computations.

---

## 4. Sequence Types

### `str` (String)
An immutable sequence of Unicode characters, enclosed in single, double, or triple quotes.
```python
name = "Alice"
message = 'Hello'
paragraph = """This is
a multi-line string."""
```

### `list`
A **mutable**, ordered collection that can hold mixed data types.
```python
fruits = ["apple", "banana", "cherry"]
mixed = [1, "two", 3.0, True]
```

### `tuple`
An **immutable**, ordered collection.
```python
coordinates = (10, 20)
```

### `range`
Represents an immutable sequence of numbers, commonly used in loops.
```python
r = range(1, 5)   # represents 1, 2, 3, 4
```

**Explanation:** "Immutable" means once created, the object's content can't be changed (strings and tuples). "Mutable" means it can be modified after creation (lists). This distinction affects performance and how these objects behave when passed around in a program.

---

## 5. Mapping Type

### `dict` (Dictionary)
A **mutable** collection of **key-value pairs**, unordered before Python 3.7 but insertion-ordered from 3.7+.
```python
student = {"name": "Ravi", "age": 22, "grade": "A"}
print(student["name"])   # Ravi
```

**Explanation:** Keys must be unique and immutable (e.g., strings, numbers, tuples), while values can be of any type, including other dictionaries or lists.

---

## 6. Set Types

### `set`
A **mutable**, unordered collection of **unique** elements (no duplicates allowed).
```python
numbers = {1, 2, 3, 3, 2}
print(numbers)   # {1, 2, 3} - duplicates automatically removed
```

### `frozenset`
An **immutable** version of a set.
```python
frozen = frozenset([1, 2, 3])
```

**Explanation:** Sets are useful for membership testing (`in` checks are fast) and eliminating duplicates automatically. `frozenset` is used when you need a set that can't be changed (e.g., as a dictionary key, since regular sets are unhashable).

---

## 7. Boolean Type

### `bool`
Represents one of two values: `True` or `False`. Internally, `bool` is a subclass of `int` (`True == 1`, `False == 0`).
```python
is_valid = True
is_empty = False
print(True + True)   # 2 (because True behaves as 1)
```

---

## 8. Binary Types

Used for handling raw binary data (e.g., file I/O, network data).
```python
b = bytes([65, 66, 67])       # immutable byte sequence -> b'ABC'
ba = bytearray([65, 66, 67])  # mutable byte sequence
```

**Explanation:** These are less commonly used in everyday scripting but essential when working with binary files, images, or network protocols.

---

## 9. `NoneType`

Represents the **absence of a value**. There is only one instance of `None` in Python.
```python
result = None
print(type(result))   # <class 'NoneType'>
```

**Explanation:** `None` is often used as a placeholder for "no value yet" — e.g., a function that doesn't explicitly `return` anything returns `None` by default.

---

## 10. Checking and Converting Types (Type Casting)

```python
x = "10"
print(type(x))          # <class 'str'>

y = int(x)               # convert string to int
z = float(x)              # convert string to float
s = str(25)                # convert int to string
```

**Explanation:** `int()`, `float()`, `str()`, `bool()`, `list()`, `tuple()`, `set()`, `dict()` are all built-in functions used to explicitly convert one data type into another — called **type casting** or **type conversion**. This is important because operations often require specific compatible types (e.g., you can't add a string and an integer directly).

---

## 11. Mutable vs Immutable — Quick Reference

| Mutable (can change after creation) | Immutable (cannot change) |
|---|---|
| `list` | `int`, `float`, `complex` |
| `dict` | `str` |
| `set` | `tuple` |
| `bytearray` | `bool` |
| | `frozenset` |
| | `bytes` |

---

## Examples with Solutions & Explanations

### Example 1: Identifying data types
**Problem:** Given several variables, print each one's type.

```python
a = 42
b = 3.14
c = "Python"
d = [1, 2, 3]
e = (4, 5)
f = {"key": "value"}
g = {1, 2, 3}
h = True
i = None

for var in [a, b, c, d, e, f, g, h, i]:
    print(var, "->", type(var))
```

**Output:**
```
42 -> <class 'int'>
3.14 -> <class 'float'>
Python -> <class 'str'>
[1, 2, 3] -> <class 'list'>
(4, 5) -> <class 'tuple'>
{'key': 'value'} -> <class 'dict'>
{1, 2, 3} -> <class 'set'>
True -> <class 'bool'>
None -> <class 'NoneType'>
```

**Explanation:** The `type()` function inspects each variable and returns its class, confirming Python's dynamic typing — no explicit declarations were needed anywhere.

---

### Example 2: Type conversion in action
**Problem:** Take two numbers as string input, convert them to integers, and show what happens with and without conversion.

```python
num1 = "5"
num2 = "10"

# Without conversion (string concatenation)
print(num1 + num2)          # "510"

# With conversion (numeric addition)
print(int(num1) + int(num2))  # 15
```

**Output:**
```
510
15
```

**Explanation:** Without conversion, `+` on two strings performs **concatenation** (joining), not addition. After converting both to `int`, `+` performs true numeric addition — this highlights why type awareness matters in Python.

---

### Example 3: Mutable vs immutable behavior
**Problem:** Demonstrate the difference between mutable (`list`) and immutable (`tuple`) types by attempting to modify each.

```python
my_list = [1, 2, 3]
my_list[0] = 100        # allowed
print(my_list)           # [100, 2, 3]

my_tuple = (1, 2, 3)
my_tuple[0] = 100        # ERROR: TypeError: 'tuple' object does not support item assignment
```

**Explanation:** Lists allow direct item assignment because they're mutable. Tuples raise a `TypeError` on the same operation because they're immutable — once created, their contents are locked, which makes tuples useful for data that shouldn't change (e.g., fixed coordinates, constant records).

---

### Example 4: Sets automatically removing duplicates
**Problem:** Given a list with duplicate values, use a set to extract only unique values.

```python
numbers = [1, 2, 2, 3, 4, 4, 4, 5]
unique_numbers = set(numbers)
print(unique_numbers)
```

**Output:**
```
{1, 2, 3, 4, 5}
```

**Explanation:** Converting a `list` to a `set` automatically discards duplicate values, since sets by definition only store unique elements. This is a common, efficient way to deduplicate data.

---

### Example 5: Using a dictionary to model real-world data
**Problem:** Create a dictionary to represent a product with a name, price, and stock quantity, then update the stock.

```python
product = {
    "name": "Laptop",
    "price": 55000,
    "in_stock": 10
}

print(f"{product['name']} costs ₹{product['price']}, {product['in_stock']} in stock.")

# Update stock after a sale
product["in_stock"] -= 1
print("Updated stock:", product["in_stock"])
```

**Output:**
```
Laptop costs ₹55000, 10 in stock.
Updated stock: 9
```

**Explanation:** Dictionaries are ideal for representing structured, real-world entities with named fields (like a product or a student record). Since `dict` is mutable, we can update `in_stock` directly using key access.

---

## Extra Practice Questions

1. Create one variable for each of the following types: `int`, `float`, `str`, `bool`, `list`, `tuple`, `dict`, `set`, and print each one's type using `type()`.
2. Write a program that takes a user's age as input (string by default) and converts it to `int`, then prints whether they are eligible to vote (age >= 18).
3. Create a list of 5 numbers with duplicates, convert it to a set to remove duplicates, then convert it back to a sorted list.
4. Demonstrate (with code and a comment explaining the error) why you cannot change an element inside a `tuple`.
5. Create a dictionary representing a "book" (title, author, price, pages). Print a formatted sentence using all four values with an f-string.
6. Write code to check if `True + True + False` equals `2`, and explain in a comment why this works given `bool` is a subclass of `int`.
7. Create a `frozenset` from a list of 5 elements, then attempt to add an element to it and observe/explain the error.
8. Write a program that takes two numbers as input, adds them as strings (concatenation) first, then converts and adds them as integers — print both results to show the difference.
9. Create a nested data structure: a list of dictionaries, where each dictionary represents a student with `name` and `marks`. Print each student's name and marks using a loop.
10. Explain (in comments) the difference between `None`, `False`, and `0` — are they equal? Are they the same type? Write code using `==` and `type()` to verify your explanation.

---

*Type the next topic name, or type **stop** to end.*
