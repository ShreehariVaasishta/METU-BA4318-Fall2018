from os import path
from myprobabilityfunctions import preparefile
from averages import centerofmass

# create file path
#winabspath = "C:\\Users\\gbora\\Desktop"
winabspath = "C:\\Users\\bora\\Dropbox\\METU\\METU BA4318 Fall 2018\\Github Repo\\METU-BA4318-Fall2018"
winprojectdir = "Session 06 - Files"
inputfilename = "test-data.txt"
inpath = path.join(winabspath, winprojectdir, inputfilename)

# process input file
coordinates = preparefile (inpath)

# calculate center of mass
center = centerofmass(coordinates)

# Display result
print("Center of mass:", center)
