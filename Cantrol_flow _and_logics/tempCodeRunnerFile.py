print("\n-- Problem 4: Count digits of a number --")
number = 348621
temp = number
digit_count = 0
while temp > 0:
    temp //= 10
    digit_count += 1
print(f"Number of digits in {number} = {digit_count}")