from os import path

def readfile (inpath):
    # open file creating a context so that it is automatically created
    # and process line by line in to a list of strings
    with open(inpath, 'r') as infileobject:
        lines = infileobject.readlines()
    points = []
    for line in lines:
        columns = line.split()
        if len(columns) == 2:
            entry = float(columns[0])
            exit = float (columns[1])
            newpoint = (entry, exit)
            # print(newpoint)
            points.append(newpoint)
        else:
            entry = float(columns[0])
            exit = float (2018)
            newpoint = (entry,exit)
            # print(newpoint)
            points.append(newpoint)
    return points

def calculateaverage (points):
    numemp = float( len(points) )
    # print (numemp, "Employees")
    sum = 0.0
    for point in points:
        entry = point[0]
        exit = point[1]
        diff = exit - entry
        # print (diff)
        sum = sum + diff
    average = sum / numemp
    return average

# create file path
path = path.realpath("./")
# windows
path = path.replace("\\", "/")
filepath=path + "/employees.txt"
print(filepath)
#inpath = path.join(filepath)
#print(inpath)

# process input file
years = readfile(filepath)

# calculate average
average = calculateaverage(years)

print("Average turnover: ", average)


