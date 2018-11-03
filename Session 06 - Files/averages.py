""" averages - functions related to averages """

# find the 2 dimensional center of mass for 
# set of points provided as a list of tuples
def centerofmass(listoftuples):
    listx, listy = zip(*listoftuples)
    avgx = getavg(listx)
    avgy = getavg(listy)
    tuple = (avgx,avgy)
    return tuple
    
# calculate simple arithmetic average of the numbers
# in the provided list.
def getavg(alist):
    size=len(alist)
    sum=0.0
    for item in alist:
        sum = sum + item
    avg = float (sum) / float (size)
    return avg