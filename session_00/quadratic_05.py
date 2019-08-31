# Solve quadratic formula for ax^2 + bx + c = 0, given from user input
# Checks for the number of solutions first using the discriminant
# Everything is now sorted into functions!

def find_discriminant(a, b, c):
    return b**2 - 4 * a * c

def print_solutions(a, b, c):
    discriminant = find_discriminant(a, b, c)

    if discriminant > 0:
        x1 = (-b + (b**2 - 4 * a * c)**0.5) / (2 * a)
        x2 = (-b - (b**2 - 4 * a * c)**0.5) / (2 * a)
        print(f"The solutions to {a}x^2 + {b}x + {c} are {x1} and {x2}") 
    elif discriminant == 0:
        x = (-b + (b**2 - 4 * a * c)**0.5) / (2 * a)
        print(f"The solution to {a}x^2 + {b}x + {c} is {x}")
    else:
        print(f"There are no real solutions to {a}x^2 + {b}x + {c}")


a = int(input("Enter a: "))
b = int(input("Enter b: "))
c = int(input("Enter c: "))

print_solutions(a, b, c)