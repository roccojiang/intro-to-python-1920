import math

# Function to calculate area of circle
def find_circle_area(radius):
    area = math.pi * (radius ** 2)
    return area


radius = float(input("Enter radius: "))  # Accept decimal numbers
area = find_circle_area(radius)  # Find area

print(f"The area of a circle with radius {radius} is {area}")  # Print result!