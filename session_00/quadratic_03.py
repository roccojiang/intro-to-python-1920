# Solve quadratic formula for ax^2 + bx + c, given from user input

a = int(input("Enter a: "))
b = int(input("Enter b: "))
c = int(input("Enter c: "))

x1 = (-b + (b**2 - 4 * a * c)**0.5) / (2 * a)
x2 = (-b - (b**2 - 4 * a * c)**0.5) / (2 * a)

print(f"The solutions to {a}x^2 + {b}x + {c} are {x1} and {x2}")

# Try a=1, b=2, c=1... What happens to the two solutions?