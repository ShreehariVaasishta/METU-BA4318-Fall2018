import os

# Here is an absolute path
winabspath = "C:\\Users\\bora\\Dropbox\\METU\\METU BA4318 Fall 2018"
linabspath = "home/bora/Dropbox/METU/METU BA4318 Fall 2018/"

# Here is a relative path for course github Windows and Linux 
winprojectdir = "Github Repo\\METU-BA4318-Fall2018\\Session 06 - Files"
linprojectdir = "Github Repo/METU-BA4318-Fall2018/Session 06 - Files"

inputfilename = "test-data.txt"
outputfilename = "output.txt"

# Based on you OS, you need to use one of the lines
inpath = os.path.join(winabspath, winprojectdir, inputfilename)
outpath = os.path.join(winabspath, winprojectdir, outputfilename)
#inpath = os.path.join(linabspath, linprojectdir, filename)
#outpath = os.path.join(linabspath, linprojectdir, outputfilename)
print("Input filepath: ", inpath)
print("Output filepath: ", outpath)
linecount = 0
points = []
# open file creating a context so that it is automatically created
# and process line by line in to a list of strings
with open(inpath, 'r') as infileobject:
    lines = infileobject.readlines()
linecount = len(lines)
print("Linecount: ", linecount)
print("First line as a string:", lines[0])

for line in lines:
    columns = line.split()
    x = float(columns[0])
    y = float (columns[1])
    newpoint = (x, y)
    points.append(newpoint)

print("First point: ", points[0])

userx = float ( input("x value (0-1000) :") )
usery = float ( input("y value (0-1000) :") )

xes, ys = zip(*points)
print (len (xes) ) 

from myprobabilityfunctions import pxltX

px = pxltX(userx, xes)
py = pxltX(usery, ys)
pxy = px * py
print (" P(x <", userx, ", y <", usery, " = ", pxy)

# simple output
outfileobject = open(outpath, 'w')
outfileobject.write("Hello world")
outfileobject.close()