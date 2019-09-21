import math

# Function to calculate volume of cone
def find_cone_volume(radius, height):
    volume = 1/3 * math.pi * (radius ** 2) * height
    return volume


radius = float(input("Enter radius: "))  # Accept decimal number inputs
height = float(input("Enter height: "))  # Accept decimal number inputs
volume = find_cone_volume(radius, height)  # Find volume

print(f"The volume of a cone with radius {radius} and height {height} is {volume}")  # Print result!