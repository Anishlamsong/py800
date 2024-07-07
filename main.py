import math
def volume(r):
    return 4/3*math.pi*r**3
radius = float(input("Enter the value of r:"))
vol = volume(r=radius)
print(f"The volume of a sphere is: {vol}")
