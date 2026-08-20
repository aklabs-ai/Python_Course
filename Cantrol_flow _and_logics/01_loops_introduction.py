"""
=====================================================================
 01. INTRODUCTION TO LOOPS IN PYTHON
=====================================================================

WHAT IS A LOOP?
---------------
A loop lets you execute a block of code repeatedly, instead of writing
the same statements again and again. Python provides two main types
of loops:

    1. for loop    -> used when you know how many times to iterate,
                       or you're iterating over a sequence
                       (list, string, tuple, range, dict, etc.)

    2. while loop   -> used when you want to repeat as long as a
                        CONDITION remains True (number of iterations
                        may not be known in advance)

This file introduces both loop types with their basic syntax,
followed by simple problems and practice exercises.
=====================================================================
"""

print("=" * 60)
print("PART A: THE FOR LOOP")
print("=" * 60)

# ---------------------------------------------------------------
# Basic syntax:
#     for item in sequence:
#         # code block
# ---------------------------------------------------------------

# Example 1: Looping over a range of numbers
print("\n-- Example 1: for loop with range() --")
for i in range(5):          # generates 0, 1, 2, 3, 4
    print("i =", i)

# Example 2: range(start, stop, step)
print("\n-- Example 2: range(start, stop, step) --")
for i in range(2, 11, 2):   # 2,4,6,8,10
    print(i, end=" ")
print()

# Example 3: Looping over a list
print("\n-- Example 3: for loop over a list --")
fruits = ["apple", "banana", "mango", "grapes"]
for fruit in fruits:
    print("Fruit:", fruit)

# Example 4: Looping over a string (iterates character by character)
print("\n-- Example 4: for loop over a string --")
for ch in "Python":
    print(ch, end=" | ")
print()

# Example 5: Using enumerate() to get index + value together
print("\n-- Example 5: enumerate() --")
for index, fruit in enumerate(fruits):  # enumerate() saves you from manually tracking a counter variable — it gives you the index and the value together in each loop iteration.
    print(f"Index {index}: {fruit}") # f-string (a way to insert variables directly into text).

# Example 6: Looping over a dictionary
print("\n-- Example 6: for loop over a dictionary --")
student = {"name": "KS", "branch": "Mechanical", "sem": 5}
for key, value in student.items():
    print(f"{key} -> {value}")


print("\n" + "=" * 60)
print("PART B: THE WHILE LOOP")
print("=" * 60)

# ---------------------------------------------------------------
# Basic syntax:
#     while condition:
#         # code block  (must eventually make condition False,
#         #               otherwise it becomes an infinite loop!)
# ---------------------------------------------------------------

# Example 1: Basic counter-based while loop
print("\n-- Example 1: basic while loop --")
count = 1
while count <= 5:
    print("count =", count)
    count += 1     # IMPORTANT: without this, the loop never ends

# Example 2: While loop that sums numbers until a condition is met
print("\n-- Example 2: summing until a limit --")
total = 0
n = 1
while total < 20:
    total += n
    n += 1
print("Final total:", total, "| stopped at n =", n)

# Example 3: While loop with user-like input simulation
print("\n-- Example 3: sentinel-controlled while loop --")
readings = [12, 45, 67, -1, 34]   # -1 acts as a "stop" sentinel
idx = 0
while readings[idx] != -1:
    print("Reading:", readings[idx])
    idx += 1
print("Stopped because sentinel value -1 was found")


print("\n" + "=" * 60)
print("FOR vs WHILE - WHEN TO USE WHICH?")
print("=" * 60)
print("""
Use a FOR loop when:
    - You know the number of iterations in advance
    - You are iterating over a collection (list, string, dict, range)

Use a WHILE loop when:
    - The number of iterations depends on a condition that changes
      during execution (not known beforehand)
    - You are waiting for a certain event/state to occur
""")


print("=" * 60)
print("SOLVED PROBLEMS")
print("=" * 60)

# Problem 1: Print first 10 natural numbers using a for loop
print("\n-- Problem 1: First 10 natural numbers (for loop) --")
for i in range(1, 11):
    print(i, end=" ")
print()

# Problem 2: Sum of first N natural numbers using a while loop
print("\n-- Problem 2: Sum of first N natural numbers (while loop) --")
N = 10
s, i = 0, 1
while i <= N:
    s += i
    i += 1
print(f"Sum of first {N} natural numbers = {s}")

# Problem 3: Print multiplication table of a number using a for loop
print("\n-- Problem 3: Multiplication table of 7 --")
num = 7
for i in range(1, 11):
    print(f"{num} x {i} = {num * i}")

# Problem 4: Count digits of a number using a while loop
print("\n-- Problem 4: Count digits of a number --")
number = 348621
temp = number
digit_count = 0
while temp > 0:
    temp //= 10
    digit_count += 1
print(f"Number of digits in {number} = {digit_count}")


print("\n" + "=" * 60)
print("PRACTICE EXERCISES (try these yourself)")
print("=" * 60)
print("""
1. Print all even numbers between 1 and 50 using a for loop.
2. Print the squares of numbers from 1 to 10 using a for loop.
3. Using a while loop, print numbers from 10 down to 1 (countdown).
4. Find the factorial of a number using a for loop.
5. Using a while loop, keep doubling a number starting from 1 until
   it exceeds 1000, and print each value.

Try writing the solutions below this comment block!
""")

# ---- write your practice solutions here ----
