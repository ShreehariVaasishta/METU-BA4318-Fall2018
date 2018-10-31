# first function in python

def absolute(x):
    if x >= 0 :
        return x
    else:
        return -x

var = -5
abs = absolute(var)
print("variable: ", var, " absolute: ", abs)
abs= absolute(x=var)

def manhattan(x1,y1,x2,y2):
    deltax = absolute(x1-x2)
    deltay = absolute(y1-y2)
    distance = deltax + deltay
    return distance

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
    
def calculateroute(listofpoints):
    route = listofpoints
    previouspoint = route[0]
    totaldistance = 0
    for currentpoint in route[1:]:
        nextstep = manhattan(x1=currentpoint[0], y1=currentpoint[1], x2=previouspoint[0], y2=previouspoint[1])
        totaldistance = totaldistance + nextstep
        previouspoint = currentpoint
    return totaldistance

def sumofnumbers(*numbers):
    # numbers is now a tuple
    if len(numbers) == 0:
        return 0 # how about returning None?
    else:
        sum = 0
        for number in numbers:
            sum = sum + number
        return sum    

result = sumofnumbers(1,2,3,4,5)
print("Result: ", result)

def circlearea(radius, pi=3):
    return radius * radius * pi

area1 = circlearea(radius=10,pi=3.14159)
area2 = circlearea(radius=10) # default value for pi is 3
print ("Area 1: ", area1, " Area 2: ", area2)

def globalize(x):
    xlocal = x
    global xglobal
    xglobal = x
    return x
    
globalize(5)
# print("xlocal", xlocal) # xlocal is not defined outside
print("xglobal", xglobal) # xglobal is accessible
