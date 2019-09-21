# Function to calculate semi-perimeter of a triangle
def find_semiperimeter(a, b, c):
    return (a + b + c) / 2

# Function to determine if it is possible to construct a triangle with sides a, b, c
def is_possible_triangle(a, b, c):
    if (a + b > c) and (a + c > b) and (b + c > a):  # Triangle inequality
        return True
    return False

# Function to print area of triangle using Heron's formula
def print_triangle_area(a, b, c):
    s = find_semiperimeter(a, b, c)
    if is_possible_triangle(a, b, c):
        area = (s * (s - a) * (s - b) * (s - c)) ** 0.5
        print(f"The area of a triangle with sides {a}, {b}, and {c} is {area}")
    else:
        print(f"Cannot form a triangle with sides {a}, {b}, and {c}!")


a = float(input("Enter side a: "))  # Accept decimal number inputs
b = float(input("Enter side b: "))  # Accept decimal number inputs
c = float(input("Enter side c: "))  # Accept decimal number inputs

print_triangle_area(a, b, c)  # Print result!