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


def pxltX(X,dimension):
    if len (dimension) == 0:
        return 0
    clone = list(dimension)
    clone.sort()
    index = 0
    size = len(clone)
    for xi in clone:
        if xi > X :
            index = clone.index(xi)
            break
    if index == 0:
        # index is still 0, not updated
        # then X is greater than all
        return 1.0
    prob = float (index) / float (size)
    return prob

def pxyltXY(X,Y,points):
    xes, ys = zip(*points)
    px = pxltX(X, xes)
    py = pxltX(Y, ys)
    pxy = px * py
    return pxy