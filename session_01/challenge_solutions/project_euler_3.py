n = 600851475143
i = 2  # First number to divide n by

while i ** 2 < n:  # Only need to consider up to i^2, due to symmetry
    while n % i == 0:
        n //= i  # Divide n by i while it is divisible (note the integer division, as it is guaranteed to be an integer)
    if i == 2:
        i += 1  # Let the next i be equal to 3
    else:
        i += 2  # Don't need to check for any more even i's after 2 is checked

print(n)  # Remaining n is the largest prime factor