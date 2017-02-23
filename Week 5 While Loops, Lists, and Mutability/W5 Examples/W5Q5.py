## What is the sum of the odd numbers from 1523 through 10503, inclusive? Hint: write a while loop to accumulate the sum and print it. Then copy and paste that sum. For maximum learning, do it with a for loop as well, using range.

## while loop
total = 0
i = 1523

while i <= 10503:
    total = total + i
    i = i + 2

print(total)

## for loop using range
total2 = 0

for i2 in range(1523, 10503 + 2, 2):
    total2 = total2 + i2

print(total2)

