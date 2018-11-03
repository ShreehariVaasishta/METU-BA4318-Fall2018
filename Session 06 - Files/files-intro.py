import os

# Here is an absolute path
winabspath = "C:\\Users\\gbora\\Desktop"
linabspath = "home/bora/Dropbox/METU/METU BA4318 Fall 2018/"

# Here is a relative path for course github Windows and Linux 
winprojectdir = "Session 06 - Files"
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

from myprobabilityfunctions import preparefile
points = preparefile (inpath)

userx = float ( input("x value (0-1000) :") )
usery = float ( input("y value (0-1000) :") )

from myprobabilityfunctions import pxyltXY
pxy = pxyltXY(userx, usery, points)
print (" P(x <", userx, ", y <", usery, " = ", pxy)

# simple output
outfileobject = open(outpath, 'w')
outfileobject.write("Probabilities")
result = " P(x <" + str (userx) + ", y <" + str (usery) + " = " + str(pxy)
outfileobject.write(result)
outfileobject.close()