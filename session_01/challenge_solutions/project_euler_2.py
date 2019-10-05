a = 1  # First term
b = 2  # Second term
c = 0
sum = 0

while b < 4000000:
    if b % 2 == 0:
        sum += b  # Add b to the sum if it is even
    c = a + b  # Calculate value of next term
    a = b
    b = c

print(sum)