from os import path
from myprobabilityfunctions import preparefile
from averages import centerofmass

# create file path
winabspath = "C:\\Users\\gbora\\Desktop"
winprojectdir = "Session 06 - Files"
inputfilename = "test-data.txt"
inpath = path.join(winabspath, winprojectdir, inputfilename)

# process input file
coordinates = preparefile (inpath)

# calculate center of mass
center = centerofmass(coordinates)

# Display result
print("Center of mass:", center)
