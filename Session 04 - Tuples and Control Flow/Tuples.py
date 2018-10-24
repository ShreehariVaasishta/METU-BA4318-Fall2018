# Python supports tuples in many flavors

# tuples are used to create a fixed size indexed container
weekdays = ("Monday", "Tuesday", "Wednesday", "Thursday", "Friday")
print("Zero-day:", weekdays[0])
print("Number of days:", len(weekdays), "Is there a Sunday in weekdays?", "Sunday" in weekdays)
weekend = ("Saturday", "Sunday")
wholeweek = weekdays + weekend
print("Whole week:", wholeweek)

# The default way, a list is used as a mixed-type way  to store related data in an indexed structure
boxdimensions = [ 24, 25, 30]
identity = ["Bora", "Güngören", "Instructor", "Business Administration", 251256]
print("The size of the tuples are ", len(boxdimensions), ", and ", len(identity), "respectively")
# lists have indices so
print("Zeroth item: ", boxdimensions[0])
boxvolume = boxdimensions[0] * boxdimensions[1] * boxdimensions[2]
print("Box volume is: ", boxvolume)
# indexes are a bit flexible in python. The python list is organized as "circular"
boxvolume = boxdimensions[-1] * boxdimensions[-2] * boxdimensions[-3]
print("Box volume is: ", boxvolume)
# There is also a nice feature known as slicing
namedata = identity[0:2]
# create a slice starting from and including index 0 up until but not including index 2
print("Name: ", namedata[0], " Surname: ", namedata[1])
restof = identity[2:] # leaving out the second index means go to the end of the list
# leaving out the first index would mean start from the beginning of the list
# Since Python is type-flexible you can assign a list to an item in another list
boxinfo = [ boxdimensions, None, namedata]
boxinfo[1] = boxvolume
# We can simply append values to the end of a list
address = "METU"
boxinfo.append(address)
print ("Dimensions:", boxinfo[0], " Volume: ", boxinfo[1], " to be delivered to:", boxinfo[2])
print("The address to deliver to: ", boxinfo[3])
# to merge two lists we use extend
x1 = [1,2,3]
x2 = [9,8,7]
x1.extend(x2)
print ("Extended list:", x1)
# We can insert items in a list
phone = "+903122101234"
print (identity)
identity.insert(4,phone)
print("Inserted", identity[4], "just before", identity[5])
print (identity)
# we can delete list items or slices using the del command
print(x1)
del x1[2:4] # delete items with indexes starting from 2 and less than 4
print(x1)
# Sorting the list is easy
x1.sort()
print(x1)
# create a sorted copy of the list
copyx1 = sorted(x1)
reversex1 = sorted(x1, reverse=True)
# We can do a quick check operation with the in operator
print("Is there any 9 in the list x1? ", 9 in x1)
print("The index of 8 in the list x1?", x1.index(8))
# print("The index of 9 in the list x1?", x1.index(9))
# There are min and max operators
print("Minimum value in x1: ", min(x1), " and max value: ", max(x1))
# We can create a list with the same content easily
fivezeroes = [0] * 5
print(fivezeroes)
# slicing and nesting lists are shallow copy operations
# so when you create a shallow copy the nested lists get to be shared
# if you need deep copy search use copy.deepcopy
original=[ [0,1,2], 1]
shallow = original[:]
import copy
deep = copy.deepcopy(original)
shallow[0][0] = 5
print("Original's version: ", original[0])
print("Deep's version: ", deep[0])
# we can convert a tuple to a list
weekdayslist = list(weekdays)
#We can convert a string into a list of characters
hellochars = list("Hello")
print(hellochars)
