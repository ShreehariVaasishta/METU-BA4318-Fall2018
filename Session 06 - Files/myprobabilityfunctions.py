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
    if index == 0:
        # index is still 0, not updated
        # then X is greater than all
        return 1.0
    prob = float (index) / float (size)
    return prob