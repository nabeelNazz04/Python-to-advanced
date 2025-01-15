import math

x=3.14
y=7.9
z=6.9

print(round(x))
print(abs(y))
print(pow(2,3))
print(f"{max(x,y,z)},{min(x,y,z)}")

print(math.pi)
print(math.e)
print(math.ceil(z))
print(math.floor(z))

radius=float(input("Enter the radius of a circle: "))
area=(math.pi)*pow(radius,2)
print(f"Area is:{area}")