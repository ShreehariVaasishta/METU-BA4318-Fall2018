# In-class example. Calculate the area of a donut.

# 1- define function to calculate area given two radii
from mylibrary import circlearea, absolute
def donutarea(inner,outer, donutpi=3):
    innerarea = circlearea(inner, pi = donutpi)
    outerarea = circlearea(outer, pi = donutpi)
    diff = absolute( outerarea - innerarea )
    return diff

# 2- get user input
outer = float ( input("Please enter outer radius:") )
inner = float ( input("Please enter inner radius:") )

# 3- calculate and display result
area = donutarea(inner,outer,pi=3.14)
print("Area is: ", area)