import mysamplefunctions

variable = -5
print("variable is:", variable)
abs = mysamplefunctions.absolute(variable)
print ("absolute value is:", abs)

from mysamplefunctions import areatriangle

w = 5
h = 10
print("area is:", areatriangle(width=w, height=h) )

from mysamplefunctions import areacircle, summation

radius = 10
area1 = areacircle(radius)
area2 = areacircle(radius, 3)
area3 = areacircle(radius, pi = 3.14)
print("area1: ", area1, "area2: ", area2, "area3: ", area3)

total1 = summation (1,2,3,4,5)
print("total1:", total1)

from mysamplefunctions import *

mynumbers = [1,2,3,4,5]
total3 = sumbylist (mynumbers)
print("total3:", total3)

total4 = summation (1,2,3,4,5)
print("total4:", total4)
