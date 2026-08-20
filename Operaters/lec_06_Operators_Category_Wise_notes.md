# Python Operators — Detailed Category-wise Notes

## 1. Arithmetic Operators: `+`, `-`, `*`, `/`, `//`, `%`, `**`

Used to perform mathematical calculations between two operands.

| Operator | Name | Example | Result |
|---|---|---|---|
| `+` | Addition | `7 + 3` | `10` |
| `-` | Subtraction | `7 - 3` | `4` |
| `*` | Multiplication | `7 * 3` | `21` |
| `/` | True Division | `7 / 3` | `2.333...` |
| `//` | Floor Division | `7 // 3` | `2` |
| `%` | Modulus (remainder) | `7 % 3` | `1` |
| `**` | Exponentiation | `7 ** 3` | `343` |

```python
a, b = 7, 3
print(a + b, a - b, a * b, a / b, a // b, a % b, a ** b)
# Output: 10 4 21 2.3333333333333335 2 1 343
```

**Explanation:** `/` always returns a `float`, even for exact divisions (`8 / 2` → `4.0`). `//` rounds the division result **down** (toward negative infinity) — important for negative numbers: `-7 // 2` gives `-4`, not `-3`. `%` gives the remainder after division, and is commonly used to check divisibility (e.g., `n % 2 == 0` for even numbers).

---

## 2. Logical Operators: `and`, `or`, `not`

Used to combine or invert boolean expressions.

| Operator | Rule | Example | Result |
|---|---|---|---|
| `and` | True only if **both** are True | `True and False` | `False` |
| `or` | True if **at least one** is True | `True or False` | `True` |
| `not` | Inverts the boolean value | `not True` | `False` |

```python
age = 25
has_license = True

can_drive = age >= 18 and has_license
print(can_drive)   # True
```

**Explanation:** Python uses **short-circuit evaluation**: in `A and B`, if `A` is `False`, `B` isn't even checked (result is already `False`). In `A or B`, if `A` is `True`, `B` isn't checked (result is already `True`). This isn't just an optimization — it can matter functionally if `B` has side effects (like calling a function).

```python
def side_effect():
    print("Called!")
    return True

result = False and side_effect()   # "Called!" never printed - short-circuited
```

---

## 3. Comparison Operators: `==`, `!=`, `<`, `>`, `<=`, `>=`

Used to compare two values; the result is always a `bool`.

| Operator | Meaning | Example | Result |
|---|---|---|---|
| `==` | Equal to | `5 == 5` | `True` |
| `!=` | Not equal to | `5 != 3` | `True` |
| `<` | Less than | `3 < 5` | `True` |
| `>` | Greater than | `3 > 5` | `False` |
| `<=` | Less than or equal to | `5 <= 5` | `True` |
| `>=` | Greater than or equal to | `4 >= 5` | `False` |

```python
x, y = 10, 20
print(x == y, x != y, x < y, x > y, x <= y, x >= y)
# Output: False True True False True False
```

**Explanation:** Note that `==` checks **value equality**, not identity (use `is` for identity, covered below). Comparison operators can also be **chained** in Python — e.g., `1 < x < 10` checks both `1 < x` and `x < 10` in one readable expression.

---

## 4. Assignment Operators: `=`, `+=`, `-=`, etc.

Used to assign a value to a variable, optionally combined with an arithmetic operation.

| Operator | Example | Equivalent To |
|---|---|---|
| `=` | `x = 5` | Direct assignment |
| `+=` | `x += 5` | `x = x + 5` |
| `-=` | `x -= 5` | `x = x - 5` |
| `*=` | `x *= 5` | `x = x * 5` |
| `/=` | `x /= 5` | `x = x / 5` |
| `//=` | `x //= 5` | `x = x // 5` |
| `%=` | `x %= 5` | `x = x % 5` |
| `**=` | `x **= 5` | `x = x ** 5` |

```python
score = 100
score += 20   # score is now 120
score -= 30    # score is now 90
score *= 2      # score is now 180
print(score)     # 180
```

**Explanation:** These "compound" operators are shorthand for "update the variable based on its current value." They're heavily used for counters, running totals, and accumulators in loops.

---

## 5. Membership Operators: `in`, `not in`

Check whether a value **exists** within a sequence (string, list, tuple, set, or dict keys).

```python
fruits = ["apple", "banana", "mango"]

print("apple" in fruits)         # True
print("grape" in fruits)           # False
print("grape" not in fruits)         # True

text = "hello world"
print("world" in text)                 # True (substring check for strings)
```

**Explanation:** `in`/`not in` are extremely useful for validation — e.g., checking if user input matches an allowed set of options, or if a substring exists inside a larger string, without writing manual loops.

---

## 6. Identity Operators: `is`, `is not`

Check whether two variables refer to the **exact same object in memory**, not just equal values.

```python
a = [1, 2, 3]
b = [1, 2, 3]
c = a

print(a == b)      # True  - same values
print(a is b)        # False - different objects in memory
print(a is c)          # True  - c refers to the SAME object as a
print(a is not b)        # True
```

**Explanation:** `==` compares **content/value**; `is` compares **identity** (memory location). This distinction is crucial with mutable objects (lists, dicts) — two lists can look identical but be entirely separate objects. `is` is also the recommended way to check for `None`: `if x is None:`.

---

## 7. Bitwise Operators

Operate directly on the **binary (bit-level) representation** of integers.

| Operator | Name | Example | Explanation |
|---|---|---|---|
| `&` | Bitwise AND | `5 & 3` → `1` | `101 & 011 = 001` |
| `\|` | Bitwise OR | `5 \| 3` → `7` | `101 \| 011 = 111` |
| `^` | Bitwise XOR | `5 ^ 3` → `6` | `101 ^ 011 = 110` |
| `~` | Bitwise NOT | `~5` → `-6` | Inverts all bits (equivalent to `-(x+1)`) |
| `<<` | Left Shift | `5 << 1` → `10` | Shifts bits left (multiplies by 2 per shift) |
| `>>` | Right Shift | `5 >> 1` → `2` | Shifts bits right (divides by 2 per shift, floor) |

```python
a, b = 5, 3      # binary: 5 = 101, 3 = 011
print(a & b)       # 1   (101 & 011 = 001)
print(a | b)         # 7   (101 | 011 = 111)
print(a ^ b)           # 6   (101 ^ 011 = 110)
print(~a)                # -6  (bitwise complement of 5)
print(a << 1)              # 10  (101 shifted left -> 1010)
print(a >> 1)                # 2   (101 shifted right -> 010)
```

**Explanation:** These operators are used in low-level programming, performance-critical code, flags/permissions systems, cryptography, and competitive programming — less common in typical everyday scripting but important to understand.

---

## Examples with Solutions & Explanations

### Example 1: Combining arithmetic and assignment operators
**Problem:** Simulate a simple game score tracker where points are added, a penalty is subtracted, and a bonus multiplier is applied.

```python
score = 50
score += 30      # earned points
score -= 10        # penalty
score *= 2           # bonus multiplier
print(f"Final score: {score}")
```

**Output:**
```
Final score: 140
```

**Explanation:** Each compound assignment operator updates `score` step-by-step, avoiding the need to write `score = score + 30` explicitly each time.

---

### Example 2: Logical and comparison operators for validation
**Problem:** Check if a password meets two rules: length >= 8 AND contains at least one digit.

```python
password = "pass1234"
has_min_length = len(password) >= 8
has_digit = any(char.isdigit() for char in password)

is_valid = has_min_length and has_digit
print("Password valid:", is_valid)
```

**Output:**
```
Password valid: True
```

**Explanation:** `len(password) >= 8` is a comparison operation returning a `bool`. `and` combines it with another boolean check (`has_digit`), and the password is only considered valid if **both** conditions hold true.

---

### Example 3: Membership operator for input validation
**Problem:** Check if a user's chosen fruit is available in stock.

```python
stock = {"apple", "banana", "orange"}
user_choice = "mango"

if user_choice in stock:
    print(f"{user_choice} is available!")
else:
    print(f"Sorry, {user_choice} is out of stock.")
```

**Output:**
```
Sorry, mango is out of stock.
```

**Explanation:** `in` checks membership in the `stock` set directly — much cleaner than manually looping through each item to compare.

---

### Example 4: Identity operator with `None`
**Problem:** Write a function that checks if an optional parameter was provided (`None`) using the recommended `is` operator instead of `==`.

```python
def greet(name=None):
    if name is None:
        print("Hello, stranger!")
    else:
        print(f"Hello, {name}!")

greet()          # Hello, stranger!
greet("Zoya")      # Hello, Zoya!
```

**Explanation:** `is None` is the Pythonic and recommended way to check for `None`, since `None` is a singleton object — there's only ever one instance of it in memory, making identity comparison both correct and efficient.

---

### Example 5: Bitwise operator for a practical trick (checking even/odd)
**Problem:** Use the bitwise AND operator to determine if a number is even or odd, instead of the modulus operator.

```python
number = 17

if number & 1 == 0:
    print(f"{number} is even")
else:
    print(f"{number} is odd")
```

**Output:**
```
17 is odd
```

**Explanation:** In binary, the last bit of an odd number is always `1`, and the last bit of an even number is always `0`. `number & 1` isolates just that last bit — if it's `0`, the number is even; if `1`, it's odd. This is a classic low-level trick often faster than `% 2` on some systems, though for readability `% 2` is usually preferred in typical Python code.

---

## Extra Practice Questions

1. Write a program that takes two numbers as input and prints results of all 7 arithmetic operators applied on them.
2. Write a program using `and`/`or`/`not` to check if a number is within the range 1-100 AND is even, printing an appropriate message.
3. Use comparison operators to write a function `compare(a, b)` that prints whether `a` is greater than, less than, or equal to `b`.
4. Simulate a simple inventory system: start with `stock = 50`, then use `-=` to subtract sold items and `+=` to add restocked items, printing the stock after each operation.
5. Given a list of usernames, write a program that checks if a user-entered username already exists using `in`, and prints an appropriate message using `not in` for the negative case.
6. Create two variables pointing to the same list object, and two more pointing to separate but equal lists. Use `is` and `==` to demonstrate the difference between identity and equality.
7. Write a program using bitwise `&`, `|`, and `^` on two numbers of your choice, and manually verify (in comments) the binary math behind each result.
8. Write a function that checks login eligibility: `is_active` (bool) AND (`is_admin` OR `has_permission`) — using `and`/`or` together, and test it with different combinations of `True`/`False`.
9. Use chained comparison operators (e.g., `18 <= age <= 60`) to check if an age falls within a valid working age range, and explain in a comment how chaining simplifies the logic compared to using `and`.
10. Write a program using `<<` and `>>` to double and halve a number respectively, and compare the results with using `* 2` and `// 2` to confirm they match.

---

*Type the next topic name, or type **stop** to end.*
