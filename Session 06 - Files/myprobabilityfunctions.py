""" myprobabilityfunctions - functions to calculate some functions """

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
    prob = float (index) / float (size)
    return prob