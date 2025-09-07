#variables
#I looked this up, grabs pi from python library and makes it a variable
import math
pi = math.pi

# Functions
def circle():
    radius1 = float(input("Enter the radius: "))
    area1 = pi*radius1**2
    print(f"The area of the circle with radius {radius1:.4f} is {area1:.4f}")
def rectangle():
    width = float(input("Enter the width: "))
    height1 = float(input("Enter the height: "))
    area2 = width * height1
    print(f"The area of the rectangle {width} x {height1} is {area2:.4f}")
def triangle():
    base = float(input("Enter the base: "))
    height2 = float(input("Enter the height: "))
    area3 = (base*height2)/2
    print(f"The area of the triangle with base {base} and height {height2} is {area3:.4f}")

# Input
def begin():
    a = input("Would you like to calculate a circle (c), a triangle (t), or a rectangle (r): ")
    if a == "c": 
        circle()
    elif a == "t":
        triangle()
    elif a == "r":
        rectangle()
    else:
        print("Invalid input")
    b = input("Would you like to begin again? (y or n) ")
    if(b == "y"): begin()
    elif(b == "n"): print("Thank you for using our program!")
    else: print("Invalid input")
begin()
    




