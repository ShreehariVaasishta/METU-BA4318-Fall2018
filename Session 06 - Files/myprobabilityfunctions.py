""" myprobabilityfunctions - functions to calculate some functions """

def preparefile (inpath):
    # open file creating a context so that it is automatically created
    # and process line by line in to a list of strings
    with open(inpath, 'r') as infileobject:
        lines = infileobject.readlines()
    points = []
    for line in lines:
        columns = line.split()
        x = float(columns[0])
        y = float (columns[1])
        newpoint = (x, y)
        points.append(newpoint)
    return points

# Calculates the value of the CDF at x=X, xhich is p(x<X)
# Given the assumption that the list dimension contains
# a sample from which a PDF can be constructed.
# Uses a naive frequency interpration of probability
def pxltX(X,dimension):
    if len (dimension) == 0:
        return 0   
    clone = list(dimension)
    clone.sort()
    if X < clone[0]:
        return 0.0
    elif X > clone[len(clone)-1]:
        return 1.0
    index = 0
    size = len(clone)
    for xi in clone:
        if xi > X :
            index = clone.index(xi)
            break
    # frequency interpretation of probability
    prob = float (index) / float (size)
    return prob

# Calculates a joint CDF for X,Y which is P(x<X, y<Y)
# Makes the naive assumption that P(x<X, y<Y) = P(x<X) * P (y<Y)
# The list point contains 2-dimensional tuples (x,y)
def pxyltXY(X,Y,points):
    # deconstructs the list into two separate lists
    xes, ys = zip(*points)
    # reuses existing functions
    px = pxltX(X, xes)
    py = pxltX(Y, ys)
    pxy = px * py
    return pxy
