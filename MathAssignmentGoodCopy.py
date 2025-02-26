import math

'''
When you see "float" written before an input, it restricts the user
from writing any character other than a number. Unlike an integer,
it allows the number to contain decimals.

When you see text written in blue with an equation sign next to the
text, it creates an undefined number variable. This way, you can 
represent numbers as words and other characters. These variables 
can then be linked to inputs and equations to let the user add a 
number to the equation.

When you see "input" written in yellow text, it creates a text box
next to the text, which the user can respond to. This can allow the
user to answer questions or contribute something to the code (such
as a variable value).

When you see "print" written in yellow, it will create a passage of
text inside the code, which is printed to the terminal. This allows
the author to communicate to the user of the code.
'''

#This allows the user to input what the radius of the sphere is
sph_radius = float(input("Please enter the radius of the sphere: "))

#This is the formula for pi
π = 3.1416

#This is the formula for the volume of a sphere
sphere = 4/3*π*sph_radius**3

#This allows the user to input what the length of the side of the cube is
cube_side = float(input("Please enter the length of a side of the cube: "))

#This is the formula for the volume of a cube
cube = cube_side**3

#This allows the user to input what the radius of the cone is
cone_radius = float(input("Please enter the radius of the cone: "))

cone_height = float(input("Please enter the height of the cone: "))

#This is the formula of the volume of a cone
cone = π*cone_radius**2*cone_height/3

#This allows the user to input what the height of the cylinder is
cyl_height = float(input("Please enter the height of the cylinder: "))

#This allows the user to input what the radius of the cylinder is
cyl_radius = float(input("Please enter the radius of the cylinder: "))

#This is the formula for the volume of a cylinder
cylinder = π*cyl_radius**2*cyl_height

#This string of code is used to present the information to the user
print("--------------------------------------------")
print("The volume of the sphere is: ")
print(sphere)
print(" ")
print("The volume of the cube is: ")
print(cube)
print(" ")
print("The volume of the cone is: ")
print(cone)
print(" ")
print("The volume of the cylinder is: ")
print(cylinder)

'''
This code was written by
Alastar Reginald Davitt Tarry
on 2/26/2025
'''