# Function to calculate semi-perimeter of a triangle
def find_semiperimeter(a, b, c):
    return (a + b + c) / 2

# Function to print area of triangle using Heron's formula
def print_triangle_area(a, b, c):
    s = find_semiperimeter(a, b, c)
    area = (s * (s - a) * (s - b) * (s - c)) ** 0.5
    print(f"The area of a triangle with sides {a}, {b}, and {c} is {area}")


a = float(input("Enter side a: "))  # Accept decimal number inputs
b = float(input("Enter side b: "))  # Accept decimal number inputs
c = float(input("Enter side c: "))  # Accept decimal number inputs

print_triangle_area(a, b, c)  # Print result!

# This will have issues with certain combinations of a, b, c as the program does not check if the triangle is possible
# Degenerate triangles (e.g. a = 1, b = 2, c = 3) will return area 0
# Impossible triangles (e.g. a = 1, b = 2, c = 4) will return with complex number solutions