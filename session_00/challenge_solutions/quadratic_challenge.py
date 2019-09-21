# CHALLENGE!
# Print out all real number solutions (rounded to nearest 2 dp) for all quadratic equations that can be formed from 0 < a, b, c ≤ 5
# After that, print the total number of real solutions found

def find_discriminant(a, b, c):
    return b**2 - 4 * a * c

def print_solutions(a, b, c):
    discriminant = find_discriminant(a, b, c)

    if discriminant > 0:
        x1 = (-b + (b**2 - 4 * a * c)**0.5) / (2 * a)
        x2 = (-b - (b**2 - 4 * a * c)**0.5) / (2 * a)
        print(f"The solutions to {a}x^2 + {b}x + {c} are {x1:.2f} and {x2:.2f}") 
    elif discriminant == 0:
        x = (-b + (b**2 - 4 * a * c)**0.5) / (2 * a)
        print(f"The solution to {a}x^2 + {b}x + {c} is {x:.2f}")
    else:
        print(f"There are no real solutions to {a}x^2 + {b}x + {c}")


count = 0
for a in range(1, 6):
    for b in range(1, 6):
        for c in range(1, 6):
            discriminant = find_discriminant(a, b, c)
            if discriminant >= 0:
                print_solutions(a, b, c)
                count += 1

print("There are", count, "real solutions for all of the possible quadratic equations")