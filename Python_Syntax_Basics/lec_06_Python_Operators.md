# Python Operators — Complete Notes

## 1. What is an Operator?

An **operator** is a special symbol (or keyword) that performs an operation on one or more values (called **operands**), producing a result. For example, in `5 + 3`, `+` is the operator, and `5` and `3` are the operands.

Python operators are grouped into several categories:

1. Arithmetic Operators
2. Comparison (Relational) Operators
3. Assignment Operators
4. Logical Operators
5. Bitwise Operators
6. Membership Operators
7. Identity Operators

---

## 2. Arithmetic Operators

Used to perform mathematical calculations.

| Operator | Meaning | Example | Result |
|---|---|---|---|
| `+` | Addition | `5 + 3` | `8` |
| `-` | Subtraction | `5 - 3` | `2` |
| `*` | Multiplication | `5 * 3` | `15` |
| `/` | Division (always returns float) | `5 / 2` | `2.5` |
| `//` | Floor Division (rounds down to nearest whole) | `5 // 2` | `2` |
| `%` | Modulus (remainder) | `5 % 2` | `1` |
| `**` | Exponentiation (power) | `5 ** 2` | `25` |

```python
a, b = 5, 2
print(a + b)   # 7
print(a / b)   # 2.5
print(a // b)  # 2
print(a % b)   # 1
print(a ** b)  # 25
```

**Explanation:** Note that `/` always produces a `float` result, even if the division is exact (e.g., `4 / 2` → `2.0`), while `//` performs division and rounds **down** to the nearest whole number (floor), which is different from simple truncation for negative numbers (e.g., `-7 // 2` → `-4`, not `-3`).

---

## 3. Comparison (Relational) Operators

Used to compare two values; always return a `bool` (`True`/`False`).

| Operator | Meaning | Example | Result |
|---|---|---|---|
| `==` | Equal to | `5 == 5` | `True` |
| `!=` | Not equal to | `5 != 3` | `True` |
| `>` | Greater than | `5 > 3` | `True` |
| `<` | Less than | `5 < 3` | `False` |
| `>=` | Greater than or equal to | `5 >= 5` | `True` |
| `<=` | Less than or equal to | `5 <= 3` | `False` |

```python
print(10 == 10)   # True
print(10 != 5)     # True
print(10 > 15)      # False
```

**Explanation:** These are heavily used in `if` conditions and loops to control program flow based on comparisons between values.

---

## 4. Assignment Operators

Used to assign values to variables, often combined with an arithmetic operation as shorthand.

| Operator | Example | Equivalent To |
|---|---|---|
| `=` | `x = 5` | Assign 5 to x |
| `+=` | `x += 3` | `x = x + 3` |
| `-=` | `x -= 3` | `x = x - 3` |
| `*=` | `x *= 3` | `x = x * 3` |
| `/=` | `x /= 3` | `x = x / 3` |
| `//=` | `x //= 3` | `x = x // 3` |
| `%=` | `x %= 3` | `x = x % 3` |
| `**=` | `x **= 3` | `x = x ** 3` |

```python
x = 10
x += 5    # x is now 15
x *= 2    # x is now 30
print(x)  # 30
```

**Explanation:** Compound assignment operators are shorthand — they modify the variable "in place" conceptually, reducing repetition and making updates like counters more concise.

---

## 5. Logical Operators

Used to combine multiple boolean expressions.

| Operator | Meaning | Example | Result |
|---|---|---|---|
| `and` | True if **both** conditions are true | `(5 > 3) and (2 < 4)` | `True` |
| `or` | True if **at least one** condition is true | `(5 > 3) or (2 > 4)` | `True` |
| `not` | Reverses the boolean value | `not (5 > 3)` | `False` |

```python
age = 20
has_id = True

if age >= 18 and has_id:
    print("Entry allowed")
else:
    print("Entry denied")
```

**Output:**
```
Entry allowed
```

**Explanation:** `and` requires **both** `age >= 18` and `has_id` to be `True` for the overall condition to be `True`. Python also uses **short-circuit evaluation** — in `A and B`, if `A` is `False`, `B` is never even evaluated (since the result is guaranteed `False`); similarly, in `A or B`, if `A` is `True`, `B` is skipped.

---

## 6. Bitwise Operators

Operate on the binary representations of integers, bit by bit.

| Operator | Meaning | Example | Result |
|---|---|---|---|
| `&` | AND | `5 & 3` | `1` |
| `\|` | OR | `5 \| 3` | `7` |
| `^` | XOR | `5 ^ 3` | `6` |
| `~` | NOT (bitwise complement) | `~5` | `-6` |
| `<<` | Left shift | `5 << 1` | `10` |
| `>>` | Right shift | `5 >> 1` | `2` |

```python
print(5 & 3)    # 5=101, 3=011 -> 001 = 1
print(5 | 3)    # 101 | 011 -> 111 = 7
print(5 << 1)   # shifts bits left by 1 -> 10
```

**Explanation:** Bitwise operators work at the binary level (e.g., `5` in binary is `101`, `3` is `011`). `&` keeps bits that are `1` in **both** numbers, `|` keeps bits that are `1` in **either** number, `<<`/`>>` shift bits left/right (effectively multiplying/dividing by powers of 2). These are commonly used in low-level programming, flags, and performance-critical code.

---

## 7. Membership Operators

Check whether a value exists within a sequence (string, list, tuple, set, dict).

| Operator | Meaning | Example | Result |
|---|---|---|---|
| `in` | True if value is found | `"a" in "apple"` | `True` |
| `not in` | True if value is NOT found | `"z" in "apple"` | `False` (so `not in` → `True`) |

```python
fruits = ["apple", "banana", "cherry"]
print("banana" in fruits)       # True
print("mango" not in fruits)    # True
```

**Explanation:** `in`/`not in` are extremely common for checking existence — e.g., validating whether user input matches an allowed option, or whether a key exists in a dictionary.

---

## 8. Identity Operators

Check whether two variables point to the **exact same object in memory** (not just equal in value).

| Operator | Meaning | Example |
|---|---|---|
| `is` | True if same object | `a is b` |
| `is not` | True if not the same object | `a is not b` |

```python
a = [1, 2, 3]
b = [1, 2, 3]
c = a

print(a == b)    # True  (same values)
print(a is b)     # False (different objects in memory)
print(a is c)      # True  (c refers to the same object as a)
```

**Explanation:** `==` checks **value equality** (do they look the same?), while `is` checks **identity** (are they literally the same object in memory?). This distinction matters especially with mutable objects like lists — two separate lists can have identical contents but still be different objects.

---

## 9. Operator Precedence (Order of Evaluation)

When multiple operators appear in one expression, Python follows a defined precedence (highest to lowest, simplified):

1. `()` — Parentheses (always evaluated first)
2. `**` — Exponentiation
3. `+x`, `-x`, `~x` — Unary plus/minus/bitwise NOT
4. `*`, `/`, `//`, `%` — Multiplication/division group
5. `+`, `-` — Addition/subtraction
6. Comparison operators (`==`, `!=`, `>`, `<`, etc.)
7. `not`
8. `and`
9. `or`

```python
result = 5 + 3 * 2      # 3*2 evaluated first -> 5+6 = 11
result2 = (5 + 3) * 2    # parentheses force addition first -> 8*2 = 16
```

**Explanation:** When in doubt, use parentheses `()` to make evaluation order explicit and code more readable — relying purely on memorized precedence rules can lead to subtle bugs.

---

## Examples with Solutions & Explanations

### Example 1: Arithmetic operators in a real calculation
**Problem:** Calculate the total cost, floor-divided quantity per box, and remainder items when packing 23 items into boxes of 5.

```python
total_items = 23
box_size = 5

full_boxes = total_items // box_size
remaining_items = total_items % box_size

print(f"Full boxes: {full_boxes}, Remaining items: {remaining_items}")
```

**Output:**
```
Full boxes: 4, Remaining items: 3
```

**Explanation:** `//` gives the number of complete boxes (integer division, rounded down), and `%` gives what's left over that doesn't fill a complete box — a classic real-world use of floor division and modulus together.

---

### Example 2: Comparison and logical operators combined
**Problem:** Determine if a person is eligible for a loan based on age (18-60) and a minimum credit score (>= 650).

```python
age = 35
credit_score = 700

eligible = (age >= 18 and age <= 60) and (credit_score >= 650)
print("Eligible for loan:", eligible)
```

**Output:**
```
Eligible for loan: True
```

**Explanation:** Two range checks (`age >= 18 and age <= 60`) are combined with a credit score check using `and` — the overall result is `True` only if **all three** conditions hold, demonstrating how logical operators chain multiple business rules.

---

### Example 3: Assignment operators for a running total
**Problem:** Simulate a shopping cart where the total price is updated using `+=` as items are added.

```python
total = 0
total += 250   # add item 1
total += 499   # add item 2
total -= 50     # apply a discount
print(f"Final total: ₹{total}")
```

**Output:**
```
Final total: ₹699
```

**Explanation:** `+=` and `-=` incrementally update `total` without needing to rewrite `total = total + ...` each time — a very common pattern for accumulating values (totals, counters, scores) in loops.

---

### Example 4: Membership operator for input validation
**Problem:** Check if a user-selected day is a valid weekday.

```python
valid_days = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday"]
user_day = "Sunday"

if user_day in valid_days:
    print(f"{user_day} is a weekday.")
else:
    print(f"{user_day} is NOT a weekday.")
```

**Output:**
```
Sunday is NOT a weekday.
```

**Explanation:** `in` checks whether `"Sunday"` exists inside the `valid_days` list. Since it doesn't, the `else` branch runs — this pattern is widely used for validating input against a set of allowed values.

---

### Example 5: `is` vs `==` with mutable objects
**Problem:** Demonstrate the practical difference between `is` and `==` using two separate but equal lists.

```python
list_a = [1, 2, 3]
list_b = [1, 2, 3]
list_c = list_a

print("list_a == list_b:", list_a == list_b)   # True (same values)
print("list_a is list_b:", list_a is list_b)     # False (different objects)
print("list_a is list_c:", list_a is list_c)      # True (same object, c is a reference to a)

list_a.append(4)
print("list_c after modifying list_a:", list_c)   # [1, 2, 3, 4] - c reflects the change!
```

**Output:**
```
list_a == list_b: True
list_a is list_b: False
list_a is list_c: True
list_c after modifying list_a: [1, 2, 3, 4]
```

**Explanation:** `list_c = list_a` doesn't create a new list — it makes `list_c` **point to the same object** as `list_a`. So modifying `list_a` also affects what `list_c` shows, since they're literally the same object in memory. This is a critical concept for understanding mutable object behavior in Python.

---

## Extra Practice Questions

1. Write a program that takes two numbers as input and prints the results of all 7 arithmetic operators (`+`, `-`, `*`, `/`, `//`, `%`, `**`) applied to them.
2. Write a program to check if a given year is a leap year using the modulus operator (a year is a leap year if divisible by 4, but not by 100, unless also divisible by 400).
3. Use assignment operators to simulate a bank account: start with a balance of 1000, then apply a deposit (`+=`), a withdrawal (`-=`), and an interest calculation (`*=` by 1.05). Print the balance after each step.
4. Write a program that checks if a number is between 10 and 100 (inclusive) using comparison and logical operators (`and`).
5. Given two lists of numbers, write a program to check (without using loops) whether a specific number exists in either list, using `in` and `or`.
6. Demonstrate bitwise operators by writing a program that checks if a number is even or odd using `&` (hint: `n & 1`).
7. Write a program that creates two variables holding the same string value, then verify using `==` and `is` whether they are equal in value and/or identical in memory (note: Python may or may not "intern" small strings — explain what you observe).
8. Simulate a simple traffic light rule checker: given a boolean `is_red_light` and `is_pedestrian_crossing`, use logical operators to decide if a car should stop (`True` if red light OR pedestrian is crossing).
9. Write an expression using multiple operators without parentheses (e.g., `10 + 2 * 3 - 4 / 2`), predict the result on paper first, then verify using Python and explain the precedence that led to that result.
10. Create two separate dictionaries with identical key-value pairs, then use `==` and `is` to compare them — explain the difference in outcome, similar to the list example above.

---

*Type the next topic name, or type **stop** to end.*
