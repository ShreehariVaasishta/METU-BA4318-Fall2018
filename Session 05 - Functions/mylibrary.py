""" mylibrary - my first library """
# filename should be same as library name (for ease of locating)
# we define the functions in the library
def absolute(x):
    if x >= 0 :
        return x
    else:
        return -x

def manhattan(x1,y1,x2,y2):
    deltax = absolute(x1-x2)
    deltay = absolute(y1-y2)
    distance = deltax + deltay
    return distance

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

def circlearea(radius, pi=3):
    return radius * radius * pi

def globalize(x):
    xlocal = x
    global xglobal
    xglobal = x
    return x