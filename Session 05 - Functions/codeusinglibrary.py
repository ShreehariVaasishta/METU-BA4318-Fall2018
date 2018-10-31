# first code using mylibrary
# we import functions from the library
# note that importing is importing the "namespace"

# method 1 - import library name, and refer to functions with the library name
# analogy: function name = name, library name = family name

import mylibrary

var = -5
abs = mylibrary.absolute(var)
print("variable: ", var, " absolute: ", abs)
abs= mylibrary.absolute(x=var)

# method 2 - import both library name and function name
# analogy: your inlaws are now your family

from mylibrary import manhattan, sumofnumbers

dist = manhattan(x1=1,y1=1,x2=0,y2=0)
print("Manhattan distance: ", dist)

route = [(1,1), (0,0), (2,4), (5,-2)]

size = len(route)
current = 0
totaldistance = 0
while current < size - 1 :
    currentpoint = route[current]    
    nextpoint = route[current+1]
    print("current point: ", currentpoint, " next point: ", nextpoint)
    nextstep = manhattan(x1=currentpoint[0], y1=currentpoint[1], x2=nextpoint[0], y2=nextpoint[1])
    totaldistance = totaldistance + nextstep
    current = current + 1
print ("Total distance: ", totaldistance)

previouspoint = route[0]
totaldistance = 0
for currentpoint in route[1:]:
    nextstep = manhattan(x1=currentpoint[0], y1=currentpoint[1], x2=previouspoint[0], y2=previouspoint[1])
    totaldistance = totaldistance + nextstep
    previouspoint = currentpoint

# from mylibrary import sumofnumbers 

result = sumofnumbers(1,2,3,4,5)
print("Result: ", result)

# method 3 - import everything from a library
from mylibrary import *
area1 = circlearea(radius=10,pi=3.14159)
area2 = circlearea(radius=10) # default value for pi is 3
print ("Area 1: ", area1, " Area 2: ", area2)

globalize(5)
# print("xlocal", xlocal) # xlocal is not defined outside
# print("xglobal", xglobal) # xglobal is accessible only in the library?